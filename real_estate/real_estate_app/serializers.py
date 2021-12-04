from rest_framework import serializers
from .models import Listing, Agent, Customer, Office

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('listing_id', 
                'address', 
                'price', 
                'bedrooms', 
                'bathrooms',
                'zipcode',
                'city',
                'agent',
                'agent_commission',
                'office',
                'sold',
                'sold_on',
                'customer',
                'created_at')
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('agent_id',
                    'name',
                    'email',
                    'created_at',
                    'office')
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id',
                    'name',
                    'email',
                    'created_at',
                    'agent_representative')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('office_id',
                    'name',
                    'email',
                    'address')