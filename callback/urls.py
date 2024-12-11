from django.urls import path
from .views import request_form_view

urlpatterns = [
    path('request/', request_form_view, name='request_form'),
]
