from asyncore import read
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from api.models import SalesHistory

from api.serlializers import FileUploadSerializer, SalesHistoryUploadFileSerializer
from rest_framework import status

# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data["file"]
        tenate_id_d = request.data["tenate_id"]
        print("tenate_idtenate_idtenate_id===", tenate_id_d)

        # decoded_file = file.read().decode()
        # upload_products_csv.delay(decoded_file, request.user.pk)
        # io_string = io.StringIO(decoded_file)
        # reader = csv.reader(io_string)
        # for row in reader:
        #     print(row)
        print("===================", file)
        reader = pd.read_csv(file)
        # print(reader)
        for _, row in reader.iterrows():
            print(row["channle"])
            # new_file = SalesHistory(
            #     sku=row["sku"],
            #     tenate_id=tenate_id_d,
            #     node=row["node"],
            #     channle=row["channle"],
            #     salesman_email=row["salesman_email"],
            #     salesman_name=row["salesman_name"],
            #     actual_sales_volume=row["actual_sales_volume"],
            #     actual_sales_volume_uom=row["actual_sales_volume_uom"],
            #     actual_sales_value=row["actual_sales_value"],
            #     actual_sales_value_uom=row["actual_sales_value_uom"],
            # )
            # new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
