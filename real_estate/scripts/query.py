import os
import datetime
from real_estate_app.models import Listing, Agent, Customer, Office
import uuid

for i in Listing.objects.all():
    temp = i.price
    if temp<100000:
        i.agent_commission = temp * 0.1
    elif temp>= 100000 and temp<200000:
        i.agent_commission = temp * 0.075
    elif temp>= 200000 and temp<500000:
        i.agent_commission = temp * 0.06
    elif temp>= 500000 and temp<1000000:
        i.agent_commission = temp * 0.05
    else:
        i.agent_commission = temp * 0.04

    i.save()