from rest_framework import serializers
from .models import SalesHistory


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SalesHistoryUploadFileSerializer(serializers.Serializer):
    class Meta:
        model = SalesHistory
        fields = "__all__"
