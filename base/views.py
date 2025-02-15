from django.shortcuts import render
from django.views import generic
from base.models import Post

class ListPostView(generic.ListView):
    model = Post
    template_name = 'base/post/list.html'
    context_object_name = 'posts'