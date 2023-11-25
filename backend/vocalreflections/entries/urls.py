from django.urls import path
from .views import EntryListAPI, EntryAudioAPI

urlpatterns = [
    path("list/", EntryListAPI.as_view()),
    path("audio/<int:pk>/", EntryAudioAPI.as_view()),
]
