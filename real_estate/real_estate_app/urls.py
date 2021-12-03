from django.urls import path
from rest_framework import routers
from real_estate_app.api import ListingViewSet, AgentViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/Listing', ListingViewSet, 'Listing')
router.register('api/Agent', AgentViewSet, 'Agent')
urlpatterns = router.urls