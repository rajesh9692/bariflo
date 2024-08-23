from rest_framework import serializers 
from .models import *
from django.contrib.auth.models import User


class signupserializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = '__all__'
        