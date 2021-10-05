import django
from django.views import generic
from .models import Album
from  django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForms


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

class UserFromview(View):
    form_class = UserForms
    templates_name = 'music/registration.html'
    
    def get(self, request):
        pass

    def post(self,request):
        pass