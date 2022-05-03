from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from . import models

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['id'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)