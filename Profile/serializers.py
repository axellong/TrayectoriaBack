from rest_framework import serializers
# ----------modelos------------
from Profile.models import Profile
from Profile.models import ProfileWeb

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__') 
        
class ProfileWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileWeb
        fields = ('__all__') 