from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True,
                                              read_only=True,
                                              # view_name='article-detail',
                                              )

    class Meta:
        model = User
        fields = ('id', 'username', 'articles',)
        read_only_fields = ('id', 'username',)


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    full_status = serializers.ReadOnlyField(source='get_status_display')
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')

    def get_cn_status(self, obj):
        if obj.status == 'p':
            return '已发表'
        elif obj.status == 'd':
            return '草稿'
        else:
            return ''

    def to_representation(self, value):
        data = super().to_representation(value)

        data['total_likes'] = value.liked_by.count()

        return data
