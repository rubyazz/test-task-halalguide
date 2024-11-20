from django.urls import path

from .views import PointOfInterestDetailView, PointOfInterestListCreateView

urlpatterns = [
    path("api/point/", PointOfInterestListCreateView.as_view(), name="poi-list-create"),
    path("api/point/<int:pk>/", PointOfInterestDetailView.as_view(), name="poi-detail"),
]
