from dataclasses import field
from urllib import response
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

from django.http import HttpResponse
import csv


class GetSalesHistoryView(ListAPIView):
    """
    This class mapping with SalesHistory and add
    some functionalities like PAGINATION, SEARCHING
    ORDERING.
    """
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


def ExportCsvView(request, id):
    """ 
    This function get "tenate_id" and create "tenate_id.csv"
    file and download it.
    """
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)

    fields_name = ([(field_name.name)
                    for field_name in SalesHistory._meta.get_fields()])

    writer.writerow(fields_name)

    fields_values = ([writer.writerow(field_value) for field_value in SalesHistory.objects.filter(
        tenate_id=id).values_list(
        'tenate_id', 'saleshistory_id', 'sku', 'node', 'channle', 'salesman_email', 'salesman_name', 'actual_sales_volume', 'actual_sales_volume_uom', 'actual_sales_value', 'actual_sales_value_uom')])

    response['Content-Disposition'] = f'attachment; filename="{id}.csv"'
    return response
