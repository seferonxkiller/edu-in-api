from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('post-rud/<int:pk>/', views.BodyRUDApiView.as_view()),
    path('post-comment/<int:post_id>/comment-list-create/', views.CommentListCreateApiView.as_view()),
]