from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path('reminder/', ReminderCreateView.as_view(), name='create-reminder'),
]
