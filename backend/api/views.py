from points.models import PointOfInterest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PointOfInterestSerializer


class PointOfInterestListCreateView(ListCreateAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class PointOfInterestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
