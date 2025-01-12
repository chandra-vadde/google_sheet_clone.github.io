# models.py
from django.db import models
from django.contrib.auth.models import User

class Spreadsheet(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cell(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    value = models.TextField(null=True, blank=True)
    formula = models.TextField(null=True, blank=True)
    style = models.JSONField(default=dict)  # Stores formatting information