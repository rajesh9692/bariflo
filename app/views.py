from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import signup
from .serializers import signupserializer
from rest_framework.response import Response

@api_view(['GET'])
def signup_get(request):
    if request.method == 'GET':
        objs = signup.objects.all()
        serializer = signupserializer(objs, many=True)
        return Response({'data': serializer.data})

@api_view(['POST'])
def signup_post(request):
    if request.method == 'POST':
        serializer = signupserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=201)
        return Response({'errors': serializer.errors}, status=400)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email_id')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Email and password are required.'}, status=400)

        try:
            user = signup.objects.get(email_id=email, password=password)
            if user:
                serializer = signupserializer(user)
                return Response({'message': 'Login successful', 'user': serializer.data}, status=200)
        except signup.DoesNotExist:
            return Response({'message': 'Invalid email or password.'}, status=400)
        