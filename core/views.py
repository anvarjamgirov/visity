from django.http import HttpRequest
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, views
from rest_framework.response import Response

from core import models
from core import serializers


class OutletAPIView(views.APIView):

    @swagger_auto_schema(
        query_serializer=serializers.OutletRequestSerializer(),
        responses={
            status.HTTP_200_OK: serializers.OutletResponseSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: '{"phone_number": ["This field is required."]}',
            status.HTTP_403_FORBIDDEN: '{"error": "Forbidden, worker not found with this phone number"}'
        },
        operation_description="Use this method to get list of outlets for specific worker by phone_number.",
        operation_summary="outlet"
    )
    def get(self, request, *args, **kwargs):
        serializer = serializers.OutletRequestSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get('phone_number')
        try:
            worker = models.Worker.objects.get(phone_number=phone_number)
            serializer = serializers.OutletResponseSerializer(worker.outlets.all(), many=True)
            return Response(serializer.data)
        except models.Worker.DoesNotExist:
            return Response(
                data={"error": "Forbidden, worker not found with this phone number"},
                status=status.HTTP_403_FORBIDDEN
            )


class VisitAPIView(views.APIView):

    @swagger_auto_schema(
        query_serializer=serializers.VisitRequestSerializer(),
        responses={
            status.HTTP_200_OK: serializers.VisitResponseSerializer(),
            status.HTTP_400_BAD_REQUEST: '{"phone_number": ["This field is required."]...}',
            status.HTTP_405_METHOD_NOT_ALLOWED: '{"detail": "Method \"GET\" not allowed."}'
        },
        operation_description="Use this method to create visit to outlet by post method.",
        operation_summary='visit'
    )
    def post(self, request: HttpRequest):
        serializer = serializers.VisitRequestSerializer(data=request.POST or request)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get('phone_number')
        if serializer.validated_data.get('outlet').worker.phone_number == phone_number:
            serializer
            visit = serializer.save()
            return Response(serializers.VisitResponseSerializer(instance=visit).data)
        else:
            return Response(
                data={"error": "Forbidden, worker not found with this phone number"},
                status=status.HTTP_403_FORBIDDEN
            )
