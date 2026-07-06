from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EscolaViewSet,
    ComentarioViewSet,
    MotdViewSet,
    ImagemViewSet,
    home,
    health,
)

router = DefaultRouter()

router.register(r"escolas", EscolaViewSet)
router.register(r"comentarios", ComentarioViewSet)
router.register(r"motds", MotdViewSet)
router.register(r"imagens", ImagemViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("health", health, name="health"),
    path("api/", include(router.urls)),
]