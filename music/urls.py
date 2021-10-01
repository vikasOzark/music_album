from django.urls import path, re_path
# ==> from django.conf.urls import url      | old syntax |
from . import views
app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    #/music/<album_id>/       old synta ==> |   url(r'^(?P<album_id>[0-9]+)/$', views.details, name = 'details')  |
    re_path(r'^(?P<album_id>[0-9]+)/$', views.details, name = 'details'),

    #/music/<album_id>/fevorite/
    re_path(r'^(?P<album_id>[0-9]+)/fevorite/$', views.fevorite, name = 'fevorite')
]
