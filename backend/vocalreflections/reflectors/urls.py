from django.urls import path
from .views import ReflectorDetailAPI

urlpatterns = [
    path("detail/", ReflectorDetailAPI.as_view()),
]
