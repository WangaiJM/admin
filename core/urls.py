from django.contrib import admin
from django.urls import path
from blog.admin import blog_admin_site

urlpatterns = [
    path('blog_admin/', blog_admin_site.urls),
    path('admin/', admin.site.urls),
]

admin.site.index_title = 'The Bookstore'
admin.site.site_header = 'Bookstore Admin'
admin.site.site_title = 'Bookstore'