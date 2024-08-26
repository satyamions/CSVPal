from django.db import models
import json

class DynamicData(models.Model):
    csv_data = models.JSONField(null=True, blank=True) 
    