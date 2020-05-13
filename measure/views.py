from rest_framework import viewsets
from .models import Temphum
from .serializers import MeasureSerializer

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Temphum.objects.all()
    serializer_class = MeasureSerializer
