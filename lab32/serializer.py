from rest_framework import serializers
from .models import Lab32 

class Lab32Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lab32
        fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')