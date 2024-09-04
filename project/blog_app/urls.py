
from django.urls import path
from. views import ListBLog,DetailBlog
urlpatterns = [
    
    path('',ListBLog,name="List"),
    path('blog_app/<id>',DetailBlog,name='Detail')
]
