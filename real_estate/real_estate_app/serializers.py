from rest_framework import serializers
from .models import Listing, Agent

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('listing_id', 
                'address', 
                'price', 
                'rooms', 
                'bathrooms', 
                'zipcode',
                'city',
                'agent')
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('agent_id',
                    'name',
                    'email')