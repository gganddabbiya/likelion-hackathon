from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exhibitions/', include("exhibition.urls")),
    path('festivals/', include("festival.urls")),
    path('accounts/', include('allauth.urls')),
    path('exhibitions', include("exhibition.urls")),
    path('post/', include("post.urls")),
]
