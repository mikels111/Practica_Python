from blog.models import Category, Article


def get_categories(request):
    ids = Article.objects.filter(
        public=True).values_list('categories', flat=True)
    # es como hacer un select| el 'filter' es opcional; el order_by('order') es para ordenar segun el orden que le he puesto en el campo 'order'
    categories = Category.objects.filter(id__in=ids).values_list('id', 'name')# Con el filter solo van a aparecer las categorias que tengan articulos asociados(subconsulta)
    return{
        'categories': categories,
        'ids': ids
    }
