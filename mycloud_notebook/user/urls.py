from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login',views.mylogin),
    url(r'^reg',views.myreg),
    url(r'^logout',views.mylogout),
]