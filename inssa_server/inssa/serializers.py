from rest_framework import serializers
from inssa.models import *

class pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyScore
        fields = ('score')
