from django.urls import path
from .views import all_events

urlpatterns = [
    path('', all_events)
]
