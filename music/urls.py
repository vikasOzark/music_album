from django.urls import path, re_path
# ==> from django.conf.urls import url      | old syntax |
from . import views
app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexVews.as_view(), name='index'),

    #/music/<album_id>/       old synta ==> |   url(r'^(?P<album_id>[0-9]+)/$', views.details, name = 'details')  |
    re_path(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name = 'details'),

    # /music/album/add/
    path('album/add/',views.AlbumCreate.as_view(), name = 'album-add'),
]
