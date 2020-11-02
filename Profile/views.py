from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


# ----------modelos------------
from Profile.models import Profile

# ---------------SERIALIZERS--------------------------

from Profile.serializers import ProfileModelSerializer


# ------------vista modelos de negocio--------------

class ProfileModelview(APIView):
    def post(self, request, format=None):
        serializer = ProfileModelSerializer(data=request.data, context={
                                            'request': request})  # va a importar una clase
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
#        Response = ResponseJson("Error")
        return Response('formato invalido')

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileModelSerializer(profile, many=True)
        return Response(serializer.data)

    # def delete(self, request):
    #     id = request.data.get("id")
    #     profile = Profile.objects.get(id=id)
    #     if(profile != None )
    #         profile.delete()
    #         return Response("exito")
    #     return Response("fallo")

    # def update(self, request):
    #     profile = Profile.objects.model.get(id=request.data.get("id"))
    #     profile.addresss = request.data.get("address")
    #     profile.save()

    def delete(self,request):
        id=request.data.get("id")
        print(id)
        profile = Profile.objects.get(id = id)
        if(profile != None):
            profile.delete()
            return Response("Exito")
        return Response("Fallo")

    def put(self, request):
        profile = Profile.objects.get(id=request.data.get("id"))
        profile.address = request.data.get("address")
        print("HOLA")
        profile.save()
        
        return Response("bien")

