from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def home(request):
    return render(request,'index.html')   



def health(request):
    return JsonResponse({
        "api": "SafeEdu API",
        "version": "1.0",
        "status": "online"
    })

from rest_framework import viewsets

from .models import (
    Escola,
    Comentario,
    Motd,
    Imagem,
)

from .serializers import (
    EscolaSerializer,
    ComentarioSerializer,
    MotdSerializer,
    ImagemSerializer,
)


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    http_method_names = ["get"]


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]

class MotdViewSet(viewsets.ModelViewSet):
    queryset = Motd.objects.all()
    serializer_class = MotdSerializer
    http_method_names = ["get"]


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]    