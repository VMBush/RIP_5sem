from kittalog.models import Kit
from rest_framework import serializers

class KitSerializer (serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ["pk", "name", "type", "description", "picture", "shelter"]