from rest_framework import serializers
from .models import UserDataModel


class UserDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDataModel
        fields = '__all__'
