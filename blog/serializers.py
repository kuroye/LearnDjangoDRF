from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    full_status = serializers.ReadOnlyField(source='get_status_display')

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')
