from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin

from .models import Home, About

# Register your models here.
admin.site.register(Home)
admin.site.register(About)

#admin.site.register(Category)


#admin.site.register(Skills)


'''class ProfileInline(admin.TabularInline):  # child class
    model = Profile
    extra = 5'''

#admin.site.register(Projects)
