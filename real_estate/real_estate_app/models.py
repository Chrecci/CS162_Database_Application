from django.db import models
import uuid
import datetime
from django.utils import timezone
# Create your models here.

class Office(models.Model):
    office_id = models.UUIDField(default=uuid.uuid4, unique=True, help_text='Unique ID for this office',)
    name = models.CharField(max_length=200)
    email = models.CharField(primary_key=True, unique=True, max_length=200)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True)
    def save(self, *args, **kwargs):
        if self.created_at is None:
            #throughout project, I will use Django timezone.now(). datetime is a naive time object, want to avoid
            self.created_at = timezone.now()
        super().save(*args, **kwargs)

class Agent(models.Model):
    agent_id = models.UUIDField(default=uuid.uuid4, unique=True, help_text='Unique ID for this agent')
    name = models.CharField(max_length=200)
    email = models.CharField(primary_key=True, unique=True, max_length=100)
    created_at = models.DateTimeField(null=True)
    #if we delete an office, the agents are no longer here either
    #but should protect the listings still
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)


class Customer(models.Model):
    customer_id = models.UUIDField(default=uuid.uuid4, unique=True, help_text='Unique ID for this customer')
    name = models.CharField(max_length=200)
    email = models.CharField(primary_key=True, unique=True, max_length=100)
    created_at = models.DateTimeField(null=True)
    
    # if we delete the agent, we still want to know who represented customer
    agent_representative = models.ForeignKey(Agent, on_delete=models.PROTECT)
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)


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
    office = models.ForeignKey(Office, on_delete=models.PROTECT)
    sold = models.CharField(max_length=50, default="No")
    # This should be an automated field, but I will insert values manually for testing sake
    sold_on = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_at = models.DateTimeField(null=True)
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.sold_on is None:
            self.sold_on = timezone.now()
        super().save(*args, **kwargs)


