from django.urls import path
from .views import EntryListAPI, EntryAudioAPI, EntryCreateAPI

urlpatterns = [
    path("list/", EntryListAPI.as_view()),
    path("audio/<int:pk>/", EntryAudioAPI.as_view()),
    path("create/", EntryCreateAPI.as_view()),
]
