from rest_framework import serializers
from django.utils import timezone

from core.constants import DateTimeFormat
from users.models import User
from articles import models


class CreateArticleSerializer(serializers.ModelSerializer):
    """ This serializer create article and blog"""
    blog_name = serializers.CharField(write_only=True, required=True, max_length=100, allow_null=False,
                                      allow_blank=False)
    blog_description = serializers.CharField(write_only=True, required=True, max_length=250, allow_null=False,
                                             allow_blank=False)
    author = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    blog = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = models.Article
        fields = ('id', 'title', 'content', 'author', 'blog', 'image', 'blog_name', 'blog_description')

    def create(self, validated_data):
        user = self.context['request'].user
        username = user.username if user else None
        blog_name = validated_data.pop('blog_name')
        blog_description = validated_data.pop('blog_description')

        blog, created = models.Blog.objects.get_or_create(
            name=blog_name, defaults={'description': blog_description, 'added_by': username}
        )

        validated_data['blog'] = blog
        validated_data['author'] = user
        validated_data["added_by"] = username
        return super().create(validated_data)


class UpdateArticleSerializer(CreateArticleSerializer):
    """ This serializer update article and blog"""
    class Meta:
        model = models.Article
        fields = ('id', 'title', 'content', 'author', 'blog', 'image', 'blog_name', 'blog_description')

    def update(self, instance, validated_data):
        user = self.context['request'].user
        username = user.username if user else None
        blog_name = validated_data.pop('blog_name')
        blog_description = validated_data.pop('blog_description')

        blog, created = models.Blog.objects.update_or_create(
            name=blog_name, defaults={'description': blog_description, 'added_by': username}
        )

        validated_data['blog'] = blog
        validated_data['author'] = user
        validated_data["last_modified_by"] = username
        validated_data["last_modified_on"] = timezone.now()

        return super().update(instance, validated_data)


class ArticleDetailsSerializer(serializers.ModelSerializer):
    """ This serializer get details of articles and blog."""
    blog_name = serializers.CharField(source='blog.name', default=None)
    blog_description = serializers.CharField(source='blog.description', default=None)
    author_name = serializers.CharField(source='author.full_name', default=None)
    posted_on = serializers.DateTimeField(source='added_on', format=DateTimeFormat.DATE_TIME)

    class Meta:
        model = models.Article
        fields = ('id', 'blog_name', 'author_name', 'blog_description', 'title', 'content', 'image', 'posted_on')
