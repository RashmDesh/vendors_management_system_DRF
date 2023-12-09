from rest_framework import serializers
from vendor.models import vendor,historical_data


class vendoreserializers(serializers.ModelSerializer):
  
    class Meta:
        model=vendor
        fields="__all__"

class historicalserilalizers(serializers.ModelSerializer):


        class Meta:
             model=historical_data
             fields="__all__"



