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
    template_name = 'music/registration.html'
    #display blank form for lgin
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # return user object if crendiial are correct
            user = authenticate( password=password, username=username)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music/index')

        return render(request, self.template_name, {'form': form})
        