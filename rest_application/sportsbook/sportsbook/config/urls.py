from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from sportsbook.config.api_root import ApiRoot

urlpatterns = [
    path('sports/', include('sports.urls')),
    path('events/', include('events.urls')),
    path('selections/', include('selections.urls')),
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
