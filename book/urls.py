from django.urls import include, re_path
from django.contrib import admin
from book import urls

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/', include(urls)),
]
