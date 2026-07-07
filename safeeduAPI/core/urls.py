from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EscolaViewSet,
    ComentarioViewSet,
    #MotdViewSet,
    MotdAPIView,
    ImagemViewSet,
    home,
    health,
    AuthAPIView,
    ValidateTokenAPIView,
)

router = DefaultRouter()

router.register(r"escolas", EscolaViewSet)
router.register(r"comentarios", ComentarioViewSet)
#router.register(r"motds", MotdViewSet)
router.register(r"imagens", ImagemViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("health", health, name="health"),
    path("api/", include(router.urls),  name="api"),
    path(
        "api/motd/",
        MotdAPIView.as_view(),
        name="motd"
    ),    

    path(
        "api/auth/",
        AuthAPIView.as_view(),
        name="auth"
    ),

    path(
        "api/validate_token/",
        ValidateTokenAPIView.as_view(),
        name="validate-token"
    ),    
]