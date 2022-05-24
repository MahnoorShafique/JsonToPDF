from django.contrib import admin
from django.urls import path, include
from Task import urls, views
from rest_framework.routers import SimpleRouter
from Task.views import Abc
# router = SimpleRouter()
# router.register("abc/", views.Abc,basename='abc')
# urlpatterns = router.urls
urlpatterns = [

    path('abc/', Abc.as_view({'get': 'list1'}), name='data'),
]
