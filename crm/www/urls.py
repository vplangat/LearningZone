from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index),
    path('products/', v.products),
    path('about/', v.about),
]