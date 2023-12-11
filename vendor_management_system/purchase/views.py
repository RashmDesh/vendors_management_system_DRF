from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from purchase.models import purchase
from purchase.serializers import purchaseeserializers



class PurchaseListApiView(APIView):

    #/api/purchase_orders/: List all purchase orders with an option to filter by vendor
    def get(self,request):
        purchase_data=purchase.objects.all()
        serializer=purchaseeserializers(purchase_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #/api/purchase_orders/: Create a purchase order
    def post(self,request):
        data={
            "po_number": request.data.get("po_number"),
            "order_date": request.data.get("order_date"),
            "delivery_date":  request.data.get("delivery_date"),
            "items": request.data.get("items"),
            "quantity": request.data.get("quantity"),
            "status": request.data.get("status"),
            "quality_rating": request.data.get("quality_rating"),
            "issue_date":  request.data.get("issue_date"),
            "acknowledgment_date":  request.data.get("acknowledgment_date"),
            "vendor": request.data.get("vendor")
        }

        serializer=purchaseeserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class PurchaseDetailApiView(APIView):

    #GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    def get(self,request,po_id):
        try:
            instance=purchase.objects.get(id=po_id)

            if not instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            serializer=purchaseeserializers(instance)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except purchase.DoesNotExist:
            return None

    #PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    def put(self,request,po_id):
        try:
            instance=purchase.objects.get(id=po_id)

            if not instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            data={
            "po_number": request.data.get("po_number"),
            "order_date": request.data.get("order_date"),
            "delivery_date":  request.data.get("delivery_date"),
            "items": request.data.get("items"),
            "quantity": request.data.get("quantity"),
            "status": request.data.get("status"),
            "quality_rating": request.data.get("quality_rating"),
            "issue_date":  request.data.get("issue_date"),
            "acknowledgment_date":  request.data.get("acknowledgment_date"),
            "vendor": request.data.get("vendor")
        }
            
            serializer=purchaseeserializers(instance,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except purchase.DoesNotExist:
            return None
        
    
    #DELETE /api/purchase_orders/{po_id}/: Delete a purchase order
    def delete(self,request,po_id):
        try:
            instance=purchase.objects.get(id=po_id)

            if not instance:
                return Response({"res":"Vender does not exist"},status=status.HTTP_400_BAD_REQUEST)
            
            instance.delete()
            return Response({"res":"Object deleted"},status=status.HTTP_200_OK)

        except purchase.DoesNotExist:
            return None

