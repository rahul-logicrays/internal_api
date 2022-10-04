from django.contrib import admin
from django.urls import path

from api.views import UploadFileView

urlpatterns = [
    path("upload/", UploadFileView.as_view(), name="upload"),
]
