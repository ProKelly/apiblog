# apiblog

Django + Django REST Framework, lectures for Flutter developers seeking to utilize Django as a backend 
for their Flutter mobile apps.

```markdown

## SUPER POWERS

### Viewsets and Routers
I utilized viewsets and routers provided by Django REST Framework. This produces powerful functionalities with just a few lines of code.

#### `api/views.py`
```python
from rest_framework import viewsets
from base.models import Post
from base.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
```

#### `api/urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
```

### Why Use Viewsets and Routers?
With viewsets and routers, a single view can handle CRUD operations with just a few lines of code, making API development much more efficient.
```
