import json
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import DynamicData
from .forms import CSVUploadForm
from .serializers import SignupSerializer, LoginSerializer
from django.contrib.auth.views import LoginView

# Views for HTML pages
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            df = pd.read_csv(csv_file)
            csv_data = df.to_dict(orient='records')
            try:
                csv_data_json = json.dumps(csv_data)
                DynamicData.objects.create(csv_data=csv_data_json)
            except (TypeError, ValueError) as e:
                form.add_error(None, f'Error processing CSV data: {e}')
                return render(request, 'upload.html', {'form': form})
            return redirect('display_data')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def display_data(request):
    data = DynamicData.objects.last()
    if data:
        try:
            csv_data = json.loads(data.csv_data)
            df = pd.DataFrame(csv_data)
        except (TypeError, ValueError) as e:
            df = pd.DataFrame()
            print(f'Error loading CSV data: {e}')
    else:
        df = pd.DataFrame()
    
    paginator = Paginator(df.to_dict(orient='records'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    df_page = pd.DataFrame(page_obj.object_list)
    headers = df_page.columns.tolist()
    rows = df_page.values.tolist()
    start_index = (page_obj.number - 1) * paginator.per_page 

    return render(request, 'display.html', {
        'headers': headers,
        'rows': rows,
        'page_obj': page_obj,
        'start_index': start_index
    })

def download_csv(request):
    data = DynamicData.objects.last()
    if data and data.csv_data:
        try:
            if isinstance(data.csv_data, str):
                data.csv_data = json.loads(data.csv_data)
            for row in data.csv_data:
                if isinstance(row, dict):
                    for key, value in row.items():
                        if value == 'null':
                            row[key] = None
                        elif value == 'NaN':
                            row[key] = float('nan')
                        else:
                            row[key] = str(value)
            df = pd.DataFrame(data.csv_data)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            df.to_csv(path_or_buf=response, index=False)
            return response
        except ValueError as e:
            return HttpResponse(f"Error generating CSV: {str(e)}")
    else:
        return HttpResponse("No data available to download.")

def home(request):
    return render(request, 'home.html')

def edit_row(request):
    if request.method == "POST":
        row_index = int(request.POST.get('row_index'))
        updated_values = request.POST.get('updated_values')
        new_values = updated_values.split(',')
        data = DynamicData.objects.last()
        if data:
            try:
                df = pd.DataFrame(json.loads(data.csv_data))
                if row_index >= 0 and row_index < len(df):
                    df.loc[row_index] = new_values
                    data.csv_data = json.dumps(df.to_dict(orient='records'))
                    data.save()
            except (TypeError, ValueError) as e:
                print(f'Error editing row: {e}')
        return redirect('display_data')
    return render(request, 'display.html')

def add_row(request):
    if request.method == 'POST':
        dynamic_data = DynamicData.objects.latest('id')
        try:
            df = pd.DataFrame(json.loads(dynamic_data.csv_data))
            new_row_data = request.POST.get('new_row').split(',')
            new_row_dict = dict(zip(df.columns, new_row_data))
            new_row_df = pd.DataFrame([new_row_dict], columns=df.columns)
            df = pd.concat([df, new_row_df], ignore_index=True)
            dynamic_data.csv_data = json.dumps(df.to_dict(orient='records'))
            dynamic_data.save()
        except (TypeError, ValueError) as e:
            print(f'Error adding row: {e}')
        return redirect('display_data')
    return render(request, 'upload.html')

def add_column(request):
    if request.method == 'POST':
        dynamic_data = DynamicData.objects.latest('id')
        try:
            df = pd.DataFrame(json.loads(dynamic_data.csv_data))
            column_name = request.POST.get('column_name')
            df[column_name] = pd.NA
            dynamic_data.csv_data = json.dumps(df.to_dict(orient='records'))
            dynamic_data.save()
        except (TypeError, ValueError) as e:
            print(f'Error adding column: {e}')
        return redirect('display_data')
    return render(request, 'upload.html')

# Authentication Views
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'  # Redirect to home page after signup

class CustomLoginView(LoginView):
    template_name = 'login.html'

def custom_logout(request):
    if request.user.is_authenticated:
        print("Logging out user:", request.user)
        auth_logout(request)
        print("Session ID before logout:", request.session.session_key)
        request.session.flush()
        print("Session ID after logout:", request.session.session_key)
    else:
        print("User not authenticated.")
    return redirect('home')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        auth_login(request, user)
        return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    auth_logout(request)
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def upload_csv_api(request):
    parser_classes = [MultiPartParser, FormParser]
    if 'csv_file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    csv_file = request.FILES['csv_file']
    try:
        df = pd.read_csv(csv_file)
        csv_data = df.to_dict(orient='records')
        csv_data_json = json.dumps(csv_data)
        DynamicData.objects.create(csv_data=csv_data_json)
        return Response({'detail': 'CSV file uploaded successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
