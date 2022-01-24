from .import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('index/',views.index,name="index"),
    path('', views.info, name="info"),
    path('/''<int:info_id>/', views.info1, name="info1"),
    path('infoadd/', views.add_info, name="add_info"),
    path('tags/', views.get_tag, name="get_tag"),
    path('tags/''<int:tag_id>/', views.category, name="category"),
    path('tags/''<str:tag_name>/''<int:info_id>/', views.tag_info, name="get_tag"),
    path('about/',views.about_page,name='about')

]