from rest_framework import serializers
from .models import Status, Road, Occurrence


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ["name", "color_hex"]


class RoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Road
        fields = ["name", "uf_code", "length"]


class OccurrenceSerializer(serializers.HyperlinkedModelSerializer):
    road_name = serializers.ReadOnlyField(source='road.name')
    status_name = serializers.ReadOnlyField(source='status.name')

    class Meta:
        model = Occurrence
        fields = ["description", "road", "road_name", "km", "status",
                  "status_name", "created_at", "updated_at"]
