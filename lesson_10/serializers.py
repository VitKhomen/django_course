from rest_framework import serializers
from django.contrib.auth.models import User

import pytz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TimezoneSerializer(serializers.Serializer):
    timezone = serializers.ChoiceField(
        choices=pytz.all_timezones, required=True)
