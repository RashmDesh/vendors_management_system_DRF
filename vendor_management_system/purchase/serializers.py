from rest_framework import serializers
from purchase.models import purchase


class purchaseeserializers(serializers.ModelSerializer):
  
    class Meta:
        model=purchase
        fields="__all__"
