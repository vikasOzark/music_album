from re import template
from django.shortcuts import render,get_object_or_404
from .models import Album, song


# Create your views here.
def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album' : all_album,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):
    album = get_object_or_404(Album,pk = album_id)
        
    return render(request, 'music/details.html', {'album' : album})

def fevorite(request,album_id):
    album = get_object_or_404(Album, pf = album_id)


    try:
        selected_song = album.song_get.get(pd = request.POST['song'])
    except (KeyError,song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album' : album,
            'erre_messenge' : 'You din not selected right song'
            })
