from points.models import PointOfInterest
from rest_framework import serializers

VALID_CATEGORIES = ["restaurant", "park", "mosque", "museum"]


class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = "__all__"

    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90.")
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError("Longitude must be between -180 and 180.")
        return value

    def validate_category(self, value):
        if value not in VALID_CATEGORIES:
            raise serializers.ValidationError(
                f"Category must be one of {VALID_CATEGORIES}."
            )
        return value
