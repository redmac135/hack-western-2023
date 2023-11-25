from django.urls import path
from .views import EntryListAPI

urlpatterns = [
    path("list/", EntryListAPI.as_view()),
]
