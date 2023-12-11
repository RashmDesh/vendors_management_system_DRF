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
    

class VendoreDetailApiView(APIView):

   # GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details
    def get(self,request,vendore_id):
        try:
            vender_instance=vendor.objects.get(id=vendore_id)

            if not vender_instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            serializer=vendoreserializers(vender_instance)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except vendor.DoesNotExist:
            return None

    #PUT /api/vendors/{vendor_id}/: Update a vendor's details    
    def put(self,request,vendore_id):
        try:
            vender_instance=vendor.objects.get(id=vendore_id)

            if not vender_instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            data={
                "name":request.data.get('name'),
                "contact_details": request.data.get('contact_details'),
                "address": request.data.get('address'),
                "vendore_code": request.data.get('vendore_code'),
                "on_time_delivery_rate": request.data.get('on_time_delivery_rate'),
                "quality_rating_avg":request.data.get('quality_rating_avg'),
                "average_response_time": request.data.get('average_response_time')

            }
            
            serializer=vendoreserializers(vender_instance,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except vendor.DoesNotExist:
            return None
        
    
    #DELETE /api/vendors/{vendor_id}/: Delete a vendor
    def delete(self,request,vendore_id):
        try:
            vender_instance=vendor.objects.get(id=vendore_id)

            if not vender_instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            vender_instance.delete()
            return Response({"res":"Object deleted"},status=status.HTTP_200_OK)

        except vendor.DoesNotExist:
            return None



