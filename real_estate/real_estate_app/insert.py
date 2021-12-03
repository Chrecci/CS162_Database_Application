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
from models import Listing, Agent, Customer
import uuid
a1 = Agent(name="Chretien Li", email="chrecci@gmail.com")
a2 = Agent(name="Mattew Li", email="matthew@gmail.com")
a1.save()
a2.save()

c1 = Customer(name="Anonymous", email="anonymous@gmail.com")
c1.save()
l1 = Listing(address="Adalbertstraße 6, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, customer=c1)
l2 = Listing(address="Dresdener Str. 121, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a2, customer=c1)
l3 = Listing(address="Adalbertstraße 6, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, customer=c1)
l4 = Listing(address="Adalbertstraße 6, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, customer=c1)
l5 = Listing(address="Adalbertstraße 6, 10999 Berlin", price=500000, bedrooms=3, bathrooms=2, zipcode="10999", city="Berlin", agent=a1, customer=c1)

l1.save()
l2.save()
l3.save()
l4.save()
l5.save()