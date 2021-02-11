
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Article


def index(request):
    return HttpResponse('ok')


def get_posts(request, qr):
    articles = Article.objects.all()

    response = []
    for article in articles:
        a = {
            'id': article.pk,
            'title': article.title,
            'url': article.url,
            'created': article.created
        }
        response.append(a)

    print(qr)
    return JsonResponse(response, safe=False)