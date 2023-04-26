from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.views import BaseViewSet
from core.constants import Action
from articles import models, serializers


class ArticleViewSet(BaseViewSet):
    model = models.Article
    permission_classes = [IsAuthenticatedOrReadOnly]
    dynamic_serializers = {
        Action.CREATE: serializers.CreateArticleSerializer,
        Action.UPDATE: serializers.UpdateArticleSerializer,
        Action.LIST: serializers.ArticleDetailsSerializer,
    }

    def get_queryset(self):
        if self.action in [Action.LIST, Action.RETRIEVE]:
            return self.model.objects.all()
        return self.model.objects.filter(author=self.request.user)
