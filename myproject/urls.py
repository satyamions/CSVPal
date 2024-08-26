from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('display/', views.display_data, name='display_data'),
    path('edit_row/', views.edit_row, name='edit_row'),
    path('add_row/', views.add_row, name='add_row'),
    path('add_column/', views.add_column, name='add_column'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('api/signup/', views.signup, name='api_signup'),
    path('api/login/', views.login, name='api_login'),
    path('api/logout/', views.logout, name='api_logout'),
    path('api/upload_csv/', views.upload_csv_api, name='api_upload_csv'),
]
