from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from main.apps import MainConfig
from main.views import IndexView
from main.views import IndexView, EposDetailView, ManaschiDetailView, ResearchersDetailView, MuxtarView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("epos/<int:pk>/", EposDetailView.as_view(), name="epos_detail"),
    path("manaschi/<int:pk>/", ManaschiDetailView.as_view(), name="manaschi_detail"),
    path("muxtar/", MuxtarView.as_view(), name="muxtar"),
    path("researchers/<int:pk>/", ResearchersDetailView.as_view(), name="researchers_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)