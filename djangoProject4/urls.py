from django.contrib import admin
from django.urls import path, include

import djangoProject4.notes_app_profile.urls as notes_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(notes_urls))
]
