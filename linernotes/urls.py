from django.conf.urls import url
from django.contrib import admin
from inventory import views

urlpatterns = [
	# Inventory module
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),

	# Admin Module
    url(r'^admin/', admin.site.urls),
]
