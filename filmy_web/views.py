from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, AdditionalInfo, Review
from .forms import FilmForm, AdditionalInfoForm, ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def all_movies(request):
    all_films = Film.objects.all()  # read
    # all_films = Film.objects.get(id=1)
    # all_films = Film.objects.filter(id=1)
    return render(request, "films.html", {'films': all_films})


@login_required()
def new_movie(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfoForm(request.POST or None)

    if all([form_film.is_valid(), form_additional.is_valid()]):
        film = form_film.save(commit=False)
        additional = form_additional.save()
        film.additional = additional
        film.save()
        return redirect(all_movies)
    return render(request, 'movie_form.html', {'form_film': form_film, 'form_additional': form_additional,
                                                 'reviews': None, 'form_review': None, 'new': True})


@login_required()
def edit_movie(request, id):
    film = get_object_or_404(Film, pk=id)
    reviews = Review.objects.filter(movie=film)

    try:
        additional = AdditionalInfo.objects.get(film=film.id)
    except AdditionalInfo.DoesNotExist:
        additional = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_additional = AdditionalInfoForm(request.POST or None, instance=additional)
    form_review = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            review = form_review.save(commit=False)
            review.movie = film
            review.save()

    if all([form_film.is_valid(), form_additional.is_valid()]):
        film = form_film.save(commit=False)
        additional = form_additional.save()
        film.additional = additional
        film.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form_film': form_film, 'form_additional': form_additional,
                                               'reviews': reviews, 'form_review': form_review, 'new': False})


@login_required()
def delete_movie(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(all_movies)
    return render(request, 'confirm.html', {'film': film})
