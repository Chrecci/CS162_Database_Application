from real_estate_app.models import Listing, Agent
from rest_framework import viewsets, permissions
from real_estate_app.serializers import ListingSerializer, AgentSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = ListingSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = AgentSerializer