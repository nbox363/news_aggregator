from django.http import HttpResponse
from django.http import JsonResponse

from .models import Article


def index(request):
    return HttpResponse('ok')


def get_article(request):
    total_articles = len(Article.objects.all())
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 5))
    order = request.GET.get('order', 'created')

    try:
        assert limit < total_articles
    except AssertionError:
        return HttpResponse('Слишком большой лимит, всего записей ' + str(total_articles))

    articles = Article.objects.all().order_by(order)[offset:limit+offset]

    response = []
    for article in articles:
        a = {
            'id': article.pk,
            'title': article.title,
            'url': article.url,
            'created': article.created
        }
        response.append(a)

    return JsonResponse(response, safe=False)
