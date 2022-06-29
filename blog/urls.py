from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    re_path(r'^articles/$', views.ArticleList.as_view()),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetails.as_view()),
    re_path(r'^users/$', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)$', views.UserDetails.as_view()),
    re_path(r'^user/', views.UserInfo.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)