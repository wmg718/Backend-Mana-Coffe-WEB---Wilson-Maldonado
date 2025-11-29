from rest_framework import routers

from .views import CategoriaViewSet, ProductoViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet, basename='productos')

urlpatterns = router.urls
