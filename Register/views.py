

from Register.serializers import UserSerializer

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny



class userModelWiev(APIView):

    permission_classes = (AllowAny,)
    # serializer_class = UserSerializer
    
    
    def post(self,request):
        print("entro")
        user = User.objects.create_user(request.data.get("username"), request.data.get("email"), request.data.get("password"))
        return Response('listo')

