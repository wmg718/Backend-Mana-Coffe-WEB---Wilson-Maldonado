from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from .pagination import CustomPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    pagination_class = CustomPagination

class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminOrReadOnly]


    def get_queryset(self):
        queryset = Producto.objects.all().order_by('id')

        # Filtro por categoría
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)

        # Filtro por nombre (búsqueda parcial)
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        # Filtro por precio mínimo
        precio_min = self.request.query_params.get('precio_min')
        if precio_min:
            queryset = queryset.filter(precio__gte=precio_min)

        # Filtro por precio máximo
        precio_max = self.request.query_params.get('precio_max')
        if precio_max:
            queryset = queryset.filter(precio__lte=precio_max)

        # Filtro por disponibilidad
        disponible = self.request.query_params.get('disponible')
        if disponible is not None:
            disponible_bool = disponible.lower() == 'true'
            queryset = queryset.filter(disponible=disponible_bool)

        # Ordenamiento
        ordenar = self.request.query_params.get('ordenar')

        if ordenar == 'precio_asc':
            queryset = queryset.order_by('precio')
        elif ordenar == 'precio_desc':
            queryset = queryset.order_by('-precio')
        elif ordenar == 'nombre_asc':
            queryset = queryset.order_by('nombre')
        elif ordenar == 'nombre_desc':
            queryset = queryset.order_by('-nombre')
        elif ordenar == 'creado_asc':
            queryset = queryset.order_by('creado')
        elif ordenar == 'creado_desc':
            queryset = queryset.order_by('-creado')

        return queryset

