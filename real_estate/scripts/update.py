import os
from datetime import datetime, timedelta
import random
from real_estate_app.models import Listing, Agent, Customer, Office
import uuid
#need at least one full line of blank space at end of document
for i in Listing.objects.all():
    random_int = random.randrange(1,10)
    random_delta = timedelta(days=random_int)
    temp = i.price
    if (temp<100000):
        i.agent_commission = temp * 0.1
    elif (temp>= 100000) and (temp<200000):
        i.agent_commission = temp * 0.075
    elif temp>= 200000 and temp<500000:
        i.agent_commission = temp * 0.06
    elif temp>= 500000 and temp<1000000:
        i.agent_commission = temp * 0.05
    else:
        i.agent_commission = temp * 0.04
    i.sold="Yes"
    created = i.created_at
    print(str(created + random_delta))
    i.sold_on = created + random_delta
    i.save()


