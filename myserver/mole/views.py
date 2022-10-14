from rest_framework import generics, viewsets

from .models import Women
from .serializers import WomenSerializer

# Create your views here.

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

