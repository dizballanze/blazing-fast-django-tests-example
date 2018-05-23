from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.db.models import Count

from blog.models import Article, Author


class ArticlesListView(ListView):

    template_name = 'blog/articles_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 20
    queryset = Article.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors_count'] = Author.objects.count()
        context['top_authors'] = Author.objects.order_by('-articles_count')[:20]
        return context


def author_page_view(request, username):
    author = get_object_or_404(Author, username=username)
    show_articles_link = author.articles.exists()
    return render(
        request, 'blog/author.html',
        context=dict(author=author, show_articles_link=show_articles_link))
