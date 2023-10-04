from django.urls import path, include
from smashapp import views  # 修改这里以导入正确的视图
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('picture/<int:picture_id>/', views.show_picture, name='show_picture'),
    path('process/<int:picture_id>/', views.process_and_show_picture, name='process_and_show_picture'),
    path('like/<int:picture_id>/', views.like_picture, name='like_picture'),
    path('dislike/<int:picture_id>/', views.dislike_picture, name='dislike_picture'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
