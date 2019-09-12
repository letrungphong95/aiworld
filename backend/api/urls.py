"""
"""
from .views import predict_label
from django.urls import path

urlpatterns = [
    path('object-label', predict_label)
]
