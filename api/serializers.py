from rest_framework import serializers
from base.models import Post,PostImage

class PostImageSerializer(serializers.ModelSerializer):
    get_image_url = serializers.SerializerMethodField()
    get_video_url = serializers.SerializerMethodField()
    class Meta:
        model = PostImage
        fields = ['id','image', 'video', 'get_image_url', 'get_video_url']
    
    def get_image_url(self,obj):
        return obj.get_image_url()
    
    def get_video_url(self,obj):
        return obj.get_video_url()


class PostSerializer(serializers.ModelSerializer):
    extra = PostImageSerializer(required=False)
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'extra']