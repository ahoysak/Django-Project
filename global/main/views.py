from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import *
from .forms import PostForm


class HomeView(ListView):
    model = Post
    ordering = ['-post_date']
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


def CategoryView(request, select):
    category_posts = Post.objects.filter(category=select)
    return render(request, 'main/category.html', {'select': select, 'category_posts': category_posts})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        #like
        likes_count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_count.total_likes()
        #dislike
        liked = False
        if likes_count.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'main/add_post.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'main/update_post.html'
    fields = ['title', 'text_article']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('home')


# class MyPostsView(DetailView):
#     model = Post
#     template_name = 'main/my_post.html'
#
# def CategoryView(request, select):
#     category_posts = Post.objects.filter(category=select)
#     return render(request, 'main/category.html', {'select': select, 'category_posts': category_posts})

