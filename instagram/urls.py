from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.images_of_the_day,name = 'imagesToday'),
    url(r'^past/(\d{4}-\d{2}-\d{2})/$',views.past_images,name = 'pastImages'),
]