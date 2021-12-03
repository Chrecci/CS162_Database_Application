from django.urls import path
from rest_framework import routers
from real_estate_app.api import ListingViewSet, AgentViewSet, CustomerViewSet, OfficeViewSet
router = routers.DefaultRouter()
router.register('api/Listing', ListingViewSet, 'Listing')
router.register('api/Agent', AgentViewSet, 'Agent')
router.register('api/Customer', CustomerViewSet, 'Customer')
router.register('api/Office', OfficeViewSet, 'Office')
urlpatterns = router.urls