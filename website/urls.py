# from django.contrib import admin
from django.urls import path, include
from website.views import *
 
urlpatterns = [
    # path('', http_test),
    # path('admin/', admin.site.urls),
    # path('http-test/', http_test),
    # path('json-test/', json_test),
    # path('website/', include('website.urls'))
      path('', index_view, name='index'),
      path('about', about_view, name='about'),
      path('contact', contact_view, name='contact')
]