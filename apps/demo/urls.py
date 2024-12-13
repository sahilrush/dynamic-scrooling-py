from django.contrib import admin
from django.urls import path, include  # Make sure to import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('apps_demo.urls')),  # Include your app's URLs with a namespace 
]

print(urlpatterns)