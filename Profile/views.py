from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# ----------modelos------------
from Profile.models import Profile

#---------------SERIALIZERS--------------------------

from Profile.serializers import ProfileModelSerializer


# ------------vista modelos de negocio--------------

class ProfileModelview(APIView): 
    def post (self,request,format=None):
        serializer= ProfileModelSerializer(data = request.data, context = {'request': request}) # va a importar una clase
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
#        Response = ResponseJson("Error")
        return Response('formato invalido')