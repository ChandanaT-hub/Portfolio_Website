from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from.import views
urlpatterns = [
    path('',views.index,name='index'),]
