'''import psycopg2

conn = psycopg2.connect(host="postgres_db",
                        port=5432,
                        user="postgres",
                        password="password",
                        database="app_db") # To remove slash

cursor = conn.cursor()
cursor.execute("INSERT INTO Agent(name, email) VALUES('cc', 'eyo@gmail.com');")
conn.commit() # <- We MUST commit to reflect the inserted data
cursor.close()
conn.close()'''
import os
import datetime
from real_estate_app.models import Listing, Agent, Customer, Office
import uuid

o1 = Office(name="office1", email="office1@gmail.com", address="address1")
o2 = Office(name="office2", email="office2@gmail.com", address="address2")
o1.save()
o2.save()

a1 = Agent(name="Chretien Li", email="chrecci1@gmail.com", office=o1)
a2 = Agent(name="Mattew Li", email="matthew@gmail.com", office=o1)
a3 = Agent(name="Gisele de Araujo", email="gisele@gmail.com", office=o2)
a1.save()
a2.save()
a3.save()

c1 = Customer(name="Anonymous", email="anonymous@gmail.com", agent_representative=a1)
c2 = Customer(name="cust", email="cust@gmail.com", agent_representative=a2)
c1.save()
c2.save()

l1 = Listing(address="Adalbertstraße 6, 10999 Berlin", price=400000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, agent_commission = 4000, office=o1, customer=c1)
l2 = Listing(address="Dresdener Str. 121, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a2, agent_commission = 4000, office=o1, customer=c1)
l3 = Listing(address="Adalbertstraße 7, 10999 Berlin", price=600000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a3, agent_commission = 4000, office=o2, customer=c1)
l4 = Listing(address="Adalbertstraße 8, 10999 Berlin", price=700000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, agent_commission = 4000, office=o1, customer=c2)
l5 = Listing(address="Adalbertstraße 9, 10999 Berlin", price=800000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, agent_commission = 4000, office=o1, customer=c2)

l1.save()
l2.save()
l3.save()
l4.save()
l5.save()