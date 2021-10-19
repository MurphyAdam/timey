from django.contrib import admin
from django.urls import path, include, re_path
from fallback.views import FallbackView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tracker/', include('tracker.urls')),
]

# catch any other URL and forward it to front-end (client, react-router-dom)
urlpatterns += [
    re_path("", FallbackView.as_view()),
]
