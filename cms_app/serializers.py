from rest_framework import serializers
from .models import WebPage, PageSection, Device, Lead, WalkIn

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class WalkInSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkIn
        fields = '__all__'
