from articles.models import Article
from users.models import CustomUser
from ckeditor.widgets import CKEditorWidget
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ['url','id', 'title', 'image', 'created_at', 'author']


class ArticleDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'content']


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'id',]


class CustomUserDetailSerializer(serializers.HyperlinkedModelSerializer):
    authors_articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api-article-detail')
    class Meta:
        model = CustomUser
        fields = ['username', 'id', 'profile_image', 'email', 'date_joined', 'authors_articles']
