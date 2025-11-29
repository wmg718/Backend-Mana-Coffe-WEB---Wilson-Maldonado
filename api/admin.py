from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')   # columnas que verás en el admin
    search_fields = ('nombre',)

# Filtro por rango de precio personalizado
class PrecioRangeFilter(admin.SimpleListFilter):
    title = 'Rango de precio'
    parameter_name = 'precio_rango'

    def lookups(self, request, model_admin):
        return [
            ('1', 'Menos de $10.000'),
            ('2', '$10.000 - $30.000'),
            ('3', '$30.000 - $60.000'),
            ('4', 'Más de $60.000'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == '1':
            return queryset.filter(precio__lt=10000)
        elif value == '2':
            return queryset.filter(precio__gte=10000, precio__lte=30000)
        elif value == '3':
            return queryset.filter(precio__gte=30000, precio__lte=60000)
        elif value == '4':
            return queryset.filter(precio__gt=60000)
        return queryset
# Para mostrar los productos en el admin

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'disponible')
    list_filter = ('categoria','disponible', PrecioRangeFilter)      # filtro lateral
    search_fields = ('nombre',)       # barra de búsqueda
    list_editable = ('precio','disponible')
    # Paginación personalizada
    list_per_page = 20  # cuántos productos por página
    list_max_show_all = 200  # máximo si usa "Show all"
