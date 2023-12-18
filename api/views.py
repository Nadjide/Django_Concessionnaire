from rest_framework import viewsets
from .serializers import ConcessionnaireSerializer, VoitureSerializer
from .models import Concessionnaire, Voiture

# Create your views here.
class ConcessionnaireViewSet(viewsets.ModelViewSet):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer