from .models import Article
from rest_framework import serializers



# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)
#     author = serializers.CharField(max_length=120)
#     email = serializers.EmailField(max_length=120)
#     date = serializers.DateTimeField()
    
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'