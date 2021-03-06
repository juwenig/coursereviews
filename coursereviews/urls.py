from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from static_pages.views import http403, http404, http500

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'static_pages.views.index', name='index'),  # noqa
    url(r'^about/$', 'static_pages.views.about', name='about'),
    url(r'^contact/$', 'static_pages.views.contact', name='contact'),
    url(r'', include('registration.urls')),
    url(r'', include('reviews.urls')),
    url(r'', include('users.urls')),
    url(r'^admin/', include('cr_admin.urls')),
    url(r'^stats/', include('stats.urls')),
    # url(r'^users/', include('users.urls')),

    url(r'^google(?P<code>[0-9a-f]{16})\.html$',
        'static_pages.views.google_verify'),

    url(r'^djadmin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^djadmin/', include(admin.site.urls)),

    # api patterns
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)

handler403 = http403
handler404 = http404
handler500 = http500
