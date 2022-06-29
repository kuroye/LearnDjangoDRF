from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


from .models import Article
from .serializers import ArticleSerializer, UserSerializer

User = get_user_model()

class UserInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})

class UserList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users.html'

    queryset = User.objects.all()
    # serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,

                          )

class ArticleList(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get(self, request):
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = ArticleSerializer(request.data)
    #     if serializer.is_valid():
    #         serializer.save(author=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve，update or delete an article instance。"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def get_object(self, pk):
    #     try:
    #         return Article.objects.get(pk=pk)
    #     except Article.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk):
    #     article = self.get_object(pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk):
    #     article = self.get_object(pk=pk)
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk):
    #     article = self.get_object(pk=pk)
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
