from django.urls import path
from .views import (ArticleDetailView, ArticleView)


urlpatterns = [
    
    path('', ArticleView.as_view(), name='articles'),
    path('detail/<int:id>/', ArticleDetailView.as_view(), name='article'),
]
