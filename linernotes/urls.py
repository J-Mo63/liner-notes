from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
	# Inventory module
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/', views.show_post, name='show_post'),
    url(r'^archive/', views.index_posts, name='index_posts'),

	# Admin Module
    url(r'^admin/', admin.site.urls),
]
