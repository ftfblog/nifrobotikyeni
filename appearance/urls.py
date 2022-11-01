from django.urls import path
from .views import index,thanks


urlpatterns = [
    path("thanks/",thanks,name="thanks"),
    path("",index,name="index"),
]


        