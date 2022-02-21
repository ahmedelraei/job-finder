from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Job finder administration"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("user/", include("users.urls")),
]
