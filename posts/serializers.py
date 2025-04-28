from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    cover = serializers.ImageField()
    views_count = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    cover = serializers.ImageField(required=False)