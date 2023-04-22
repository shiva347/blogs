from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.views import BaseViewSet
from core.constants import Action
from articles import models, serializers


class ArticleViewSet(BaseViewSet):
    queryset = models.Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    dynamic_serializers = {
        Action.CREATE: serializers.CreateArticleSerializer,
        Action.UPDATE: serializers.UpdateArticleSerializer,
        Action.LIST: serializers.ArticleDetailsSerializer,
    }
