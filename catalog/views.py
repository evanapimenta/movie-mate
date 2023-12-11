from django.shortcuts import render

from .forms import MovieForm
from .models import Movie, Genre

# Create your views here.
def index(request):
    return render(request, "movies/index.html")


def register_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['movie_title']
            year = form.cleaned_data['movie_year']
            genre = form.cleaned_data['movie_genres']
            synopsis = form.cleaned_data['movie_synopsis']
            poster = form.cleaned_data['movie_poster']

            movie = Movie.objects.create(
                title=title,
                year=year,
                synopsis=synopsis,
                poster=poster
                )
            movie.genre.set(genre)
            movie.save()

        return render(request, 'index.html')

    else:
        form = MovieForm()

    return render(request, "movies/register.html", {"form": form})