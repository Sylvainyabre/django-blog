from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from my_site.sitemaps import ArticleSitemap

sitemaps = {'articles': ArticleSitemap, }
urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', include('my_site.urls')),
                  path('registration/', include('registration.urls')),
                  path('', include('django.contrib.auth.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('api/', include('my_site.api.urls', namespace='api')),
                  path('api/auth/', include('registration.api.urls',namespace='api')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views.sitemap')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
