from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexVews(generic.ListView):
    template_name  = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()
    
class detailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genra']