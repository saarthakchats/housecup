from django.contrib import admin
from django.urls import path, include
import points.views
import points.urls
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', points.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('update/', points.views.update, name='update'),
    path('houses/', include(points.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
