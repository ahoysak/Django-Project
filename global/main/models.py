from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_article = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='Актори')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
