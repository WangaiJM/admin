from django.contrib import admin

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'

blog_admin_site = BlogAdminArea(name='Blog Admin Area')
