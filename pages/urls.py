from django.urls import path,include
from .views import index,bos,sponsorview,projectpageview,projectdetailview,pageview,iletisimpageview

urlpatterns = [
    path("iletisim",iletisimpageview),
    path("",bos,name="index"),
    path("takimimiz",index),
    path("sponsorlar/",sponsorview),
    path("projeler/",projectpageview),
    path("projeler/<slug:slug>",projectdetailview),
    path("<slug:slug>",pageview),
    path("ckeditör",include("ckeditor_uploader.urls")),

]



