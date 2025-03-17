from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import Movie
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required



# Create your views here.
# class Home(LoginView):
#     template_name = 'home.html'

def signup(request):
    # view functions can handle multiple http requests
    error_message = ''
    # handle the post request (submission of the form)
    if request.method == "POST":
        # create a user form object that includes the data from the submitted form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the form and create the user 
            # adds a row to the user table
            user = form.save()
            # login in the user 
            login(request, user)
            # this creates the request.user ^ in all our view functions

            return redirect('movies-index') # cats-index is the name of a path in urls.py
        else: 
            error_message = "Invalid sign up - try again"
    # handling the get request 
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


class MovieList(ListView):
    model = Movie


class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'

class Home(LoginView):
    template_name = 'home.html'

    

def home(request):
    return HttpResponse('<h1>Welcome to the Movie app!</h1>')

def about(request):
    return render(request, 'about.html')


@login_required
def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    comment_form = CommentForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'comment_form': comment_form})