from rest_framework import serializers
from .models import SalesHistory


class GetSalesHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesHistory
        fields = '__all__'
