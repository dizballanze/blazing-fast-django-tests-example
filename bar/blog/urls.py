from django.conf.urls import url

from blog.views import ArticlesListView, author_page_view


urlpatterns = [
    url(r'^$', ArticlesListView.as_view(), name='articles_list'),
    url(r'^authors/(?P<username>[\w\-_]{1,64})$', author_page_view, name='author_page'),
]
