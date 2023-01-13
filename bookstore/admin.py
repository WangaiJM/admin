from django.contrib import admin

class BookstoreAdminArea(admin.AdminSite):
    site_header = 'Bookstore Admin Area'

bookstore_admin_site = BookstoreAdminArea(name='Bookstore Admin')