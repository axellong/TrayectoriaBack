from rest_framework import serializers
# ----------modelos------------
from Profile.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = ('_all_') 