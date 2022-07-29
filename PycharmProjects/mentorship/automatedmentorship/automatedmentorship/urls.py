from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, student_views, mentors_views, dean_academics

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
