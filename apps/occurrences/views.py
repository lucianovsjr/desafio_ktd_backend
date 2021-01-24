from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RoadSerializer, StatusSerializer, OccurrenceSerializer
from .models import Road, Status, Occurrence


class RoadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roads to be viewed or edited.
    """

    queryset = Road.objects.all().order_by("name")
    serializer_class = RoadSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows status to be viewed or edited.
    """

    queryset = Status.objects.all().order_by("name")
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class OccurenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows occurence to be viewed or edited.
    """

    queryset = Occurrence.objects.all().order_by("created_at")
    serializer_class = OccurrenceSerializer
    permission_classes = [permissions.IsAuthenticated]
