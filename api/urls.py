from rest_framework import routers

from .views import ConcessionnaireViewSet

api_router = routers.DefaultRouter()
api_router.register('concessionnaire', ConcessionnaireViewSet)