from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.ListPostView.as_view(), name='list_post'),
]
