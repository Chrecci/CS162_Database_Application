import os
from datetime import datetime, timedelta
import pandas as pd
from statistics import mean
from real_estate_app.models import Listing, Agent, Customer, Office
import uuid
from django.forms.models import model_to_dict
from django.utils import timezone

#1. Find the top 5 offices with the most sales for that month.
from django.db.models import Count, Sum, Avg, F
#specify time frame that we want, 31 days
last_month = timezone.now() - timedelta(days=31)
#'-' in front of dcount means ascending
result_dict_1 = pd.DataFrame((list(Listing.objects
    .filter(created_at__gte=last_month)
    .values('office')
    .annotate(dcount=Count('office'))
    .order_by('-dcount')))[:5])
print(result_dict_1)
#2. Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).
result_dict_2 = pd.DataFrame((list(Listing.objects
    .filter(created_at__gte=last_month)
    .values('agent')
    .annotate(sales_total=Count('agent'))
    .order_by('-sales_total')))[:5])
print(result_dict_2)

#3. Calculate the commission that each estate agent must receive and store the results in a separate table. 
result_dict_3 = pd.DataFrame((list(Listing.objects
    .filter(created_at__gte=last_month)
    .values('agent', 'agent__name')
    .annotate(total_commission=Sum('agent_commission'))
    .order_by('-agent_commission')))[:5])
print(result_dict_3)
#For all houses that were sold that month, calculate the average number of days that the house was on the market.

# Django's F-expressions allow us to reference tables directly
result_dict_4 = pd.DataFrame((list(Listing.objects
    .filter(created_at__gte=last_month)
    .values('address', 'agent__name')
    .annotate(days_on_market=F('sold_on')-F('created_at'))
    .order_by('-days_on_market'))))
print(result_dict_4)
# Average of Timedelta objects
temp_delta = timedelta(0)
times_list = list(result_dict_4['days_on_market'])
for i in times_list:
    temp_delta += i

print(temp_delta/len(times_list))

#For all houses that were sold that month, calculate the average selling price
house_price_average = Listing.objects.filter(created_at__gte=last_month).filter(sold="Yes").aggregate(Avg('price'))

print(house_price_average)


