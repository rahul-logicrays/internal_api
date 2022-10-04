from django.shortcuts import render
from .models import SalesHistory
from .serlializers import GetSalesHistorySerializer
from .paginations import CustomPagination
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CustomSearchFilter


class GetSalesHistoryView(ListAPIView):

    queryset = SalesHistory.objects.all()
    serializer_class = GetSalesHistorySerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['tenate_id']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'status': status.HTTP_200_OK,
                         'data': response.data, 'msg': 'Data Retrived.'}
        return response
