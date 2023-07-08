from django.urls import path
from .views import exceptionView

urlpatterns = [path("", exceptionView)]
