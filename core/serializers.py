from rest_framework import serializers

from core import models


class OutletRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=31,
        required=True
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class OutletResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Outlet
        exclude = ['worker', ]


class VisitRequestSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=31,
        required=True
    )

    class Meta:
        model = models.Visit
        fields = ['phone_number', 'coordinates', 'outlet']

    def create(self, validated_data):
        validated_data.pop('phone_number')
        return models.Visit.objects.create(**validated_data)


class VisitResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Visit
        fields = ['id', 'outlet', 'coordinates', 'date']
