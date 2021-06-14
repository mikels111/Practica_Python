from pages.models import Page


def get_pages(request):
    pages = Page.objects.filter(visible=True).values_list('id', 'title', 'slug')  # es como hacer un select| el 'filter' es opcional
    return{
        'pages': pages
    }
