from django.db import models
import uuid
# Create your models here.

class Office(models.Model):
    office_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, help_text='Unique ID for this office')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Agent(models.Model):
    agent_id = models.UUIDField(default=uuid.uuid4, unique=True, help_text='Unique ID for this agent')
    name = models.CharField(max_length=200)
    email = models.CharField(primary_key=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)


class Customer(models.Model):
    customer_id = models.UUIDField(default=uuid.uuid4, unique=True, help_text='Unique ID for this agent')
    name = models.CharField(max_length=200)
    email = models.CharField(primary_key=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    agent_representative = models.ForeignKey(Agent, on_delete=models.CASCADE)



class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, help_text='Unique ID for this listing')
    address = models.CharField(max_length=200)
    price = models.FloatField(blank=True)
    bedrooms = models.FloatField(blank=True)
    bathrooms = models.FloatField(blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    agent_commission = models.FloatField(blank=True)
    sold = models.CharField(max_length=50, default="No")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

