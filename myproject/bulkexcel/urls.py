from django.urls import path
from .views import RunCommandView

urlpatterns = [
    path('run-command/', RunCommandView.as_view(), name='run-command'),
]