from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^register/user/$', registration),
   url(r'^loginview/$',loginview),
   url(r'^home/page/',home_page),
   url(r'^login/view/$',login_view),
   url(r'^registration/page/$', registration_page),
   url(r'^show/user/$',show_user),
   url(r'^logout/$',logout),

   
 

]