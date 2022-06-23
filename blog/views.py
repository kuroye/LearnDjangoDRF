from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

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

    queryset = Article.objects.get()
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
