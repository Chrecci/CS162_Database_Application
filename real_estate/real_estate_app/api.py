from real_estate_app.models import Listing, Agent, Customer, Office
from rest_framework import viewsets, permissions
from real_estate_app.serializers import ListingSerializer, AgentSerializer, CustomerSerializer, OfficeSerializer

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

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class = OfficeSerializer