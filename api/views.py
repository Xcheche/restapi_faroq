from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Article
from .serializers import ArticleSerializer 
import os

class ArticleView(APIView):
    def get(self, request):  # GET
        try:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
           

            return Response({
                'data': serializer.data,
                'message': "Articles data fetched successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):  # POST
        try:
            data = request.data
            serializer = ArticleSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Invalid data provided"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Save article
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "New article created successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while creating the article"
            }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):  # PATCH
        try:
            data = request.data
            article = Article.objects.filter(id=data.get('id')).first()

            if not article:
                return Response({
                    'data': {},
                    'message': "Article not found with this ID"
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = ArticleSerializer(article, data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Invalid data provided"
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Article updated successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while updating the article"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):  # DELETE
        try:
            data = request.data
            article = Article.objects.filter(id=data.get('id')).first()

            if not article:
                return Response({
                    'data': {},
                    'message': "Article not found with this ID"
                }, status=status.HTTP_404_NOT_FOUND)

            article.delete()
            return Response({
                'data': {},
                'message': "Article deleted successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while deleting the article"
            }, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    def get(self, request, id):  # GET
        try:
            article = Article.objects.filter(id=id).first()

            if not article:
                return Response({
                    'data': {},
                    'message': "Article not found with this ID"
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = ArticleSerializer(article)

            return Response({
                'data': serializer.data,
                'message': "Article data fetched successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the article data"
            }, status=status.HTTP_400_BAD_REQUEST)
