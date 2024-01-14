from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from tuneTracker.models import Song, Artist, Contact


def home(request):
    try:
        objects = Song.objects.all()
        context = {'objects': objects}
        return render(request, 'home.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")


def artists(request):
    try:
        artists_with_song_count = Artist.objects.annotate(
            song_count=Count('song'))
        context = {'artists_with_song_count': artists_with_song_count}
        return render(request, 'artist.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")


def add_artist(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            if not name:
                raise ValueError("Name cannot be empty.")
            new_artist = Artist(name=name)
            new_artist.save()
            return redirect('/')
        return render(request, 'addartist.html')
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")


def add_song(request):
    try:
        artists = Artist.objects.all()
        context = {'artists': artists}
        if request.method == 'POST':
            artist_id = request.POST.get('artist_id')
            singer = Artist.objects.get(id=artist_id)
            song = request.POST.get('name')

            if not artist_id or not singer or not song:
                raise ValueError(
                    "Please provide valid artist, singer, and song information.")

            new_song = Song(singer=singer, song=song)
            new_song.save()
            return redirect('/')
        return render(request, 'addsong.html', context)
    except Artist.DoesNotExist:
        return HttpResponseServerError("Selected artist does not exist.")
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {str(e)}")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("written to database")
    return render(request, 'contact.html')
