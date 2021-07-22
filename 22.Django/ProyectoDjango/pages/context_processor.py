from pages.models import Page


def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')  # es como hacer un select| el 'filter' es opcional; el order_by('order') es para ordenar segun el orden que le he puesto en el campo 'order'
    return{
        'pages': pages
    }
