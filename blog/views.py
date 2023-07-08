from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import BlogPostForm
from .models import BlogPost


class BlogCreateView(generic.CreateView):
    model = BlogPost
    template_name = 'blog/blog_create.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(generic.UpdateView):
    model = BlogPost
    template_name = 'blog/blog_update.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blogs')


class BlogListView(generic.ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogPost.objects.filter(is_active=True)  # по положительному признаку публикации


class BlogDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        """
        Увеличиваем счетчик просмотров
        """
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


def increase_views(request, post_id):
    try:
        blog_post = BlogPost.objects.get(pk=post_id)
        blog_post.views += 1
        blog_post.save()
        return JsonResponse({'status': 'success', 'views': blog_post.views})
    except BlogPost.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Blog post not found'}, status=404)
