# ignore this file
create customer table
add it to serializers, api, views, urls

figure out inserting batch data into django models

revisit On_cascade in models

django startproject <name> .
django startapp <name>
pip install djangorestframework
pip install psycopg2
docker-compose.yml for postgres
models are for database
serialize to expose to rest framework 
api or views to create viewset
add to urls
to run file: python manage.py shell /< file_name.py
to reference foreign key (agent eg.): "agent__email"
create model object: 

o1 = Office(name="office1", email="office1@gmail.com", address="address1")
o1.save()

queryset (list-like) of all objects in model: Office.objects.all()

turn query in dataframe: 
df = pd.DataFrame((list(Office.objects
    .filter(_____)
    .values(____)))

complex query:
result_dict_4 = pd.DataFrame((list(Listing.objects
    #created_at greater than or equal to last month
    .filter(created_at__gte=last_month)
    .values('address', 'agent__name')
    #GROUP BY
    .annotate(total_commission=Sum('agent_commission'))
    #ORDER BY. '-' is ascending. [:5] indicates first five rows
    .order_by('-agent_commission')))[:5])