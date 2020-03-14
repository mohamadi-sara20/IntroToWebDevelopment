from django.contrib import admin
from videos.models import Customer, Movie
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fields = ['phone', 'first_name', 'last_name']
    search_fields = ['phone', 'first_name', 'last_name']
admin.site.register(Movie)
admin.site.register(Customer, CustomerAdmin)
