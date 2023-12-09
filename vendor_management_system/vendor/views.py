from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  .models import vendor,historical_data
from .serializers import vendoreserializers,historicalserilalizers

# Create your views here.
class VendoreListApiView(APIView):

    #GET /api/vendors/: List all vendors.
    def get(self,request):
        vendor_data=vendor.objects.all()
        serializer=vendoreserializers(vendor_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #POST /api/vendors/: Create a new vendor.
    def post(self,request):
        data={
             "id": request.data.get('id'),
        "name":request.data.get('name'),
        "contact_details": request.data.get('contact_details'),
        "address": request.data.get('address'),
        "vendore_code": request.data.get('vendore_code'),
        "on_time_delivery_rate": request.data.get('on_time_delivery_rate'),
        "quality_rating_avg":request.data.get('quality_rating_avg'),
        "average_response_time": request.data.get('average_response_time')
        }

        serializer=vendoreserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

