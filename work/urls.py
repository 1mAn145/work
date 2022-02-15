
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from apps.course.views import index 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('accounts/', include('apps.accounts.urls')),
    path('course/', include('apps.course.urls')),
    ]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

