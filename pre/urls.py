from django.urls import path,include
from pre import views
urlpatterns = [
    path('articles/',views.ArticleList.as_view()),
    path('detail/<int:pk>/',views.ArticleDetail.as_view()),
]