from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


# Create your views here.


# =================================================================
def track_list(request):
    context = {}
    tracks = Track.list_track()
    context["tracks"] = tracks
    return render(request, "track/list.html", context)


# =================================================================
# def track_create(request):
#     context = {}
#     form = CreateTrack()
#     context["form"] = form
#     if request.method == "POST":
#         # publich data user enter
#         form = CreateTrack(request.POST, request.FILES)
#         if form.is_valid():
#             # create object from book
#             name = form.cleaned_data["name"]
#             description = form.cleaned_data["description"]
#             image = form.cleaned_data["image"]

#             trackobj = Track.create_track(name, description, image)
#             return redirect(trackobj)
#         else:
#             context["error"] = form.errors
#     return render(request, "track/create.html", context)


def track_create(request):
    context = {}
    form = CreateTrackModel()
    context = {"form": form}
    return render(request, "track/create.html", context)


# =================================================================
def track_update(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)
        form = UpdateTrack(
            initial={
                "name": trackobj.name,
                "description": trackobj.description,
                "image": trackobj.image,
            }
        )

        if request.method == "POST":
            form = UpdateTrack(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data["name"]
                description = form.cleaned_data["description"]
                image = form.cleaned_data["image"]

                if not image:
                    image = trackobj.image

                track_url = Track.update_track(id, name, description, image)
                return redirect(track_url)
            else:
                context["error"] = form.errors

        context["form"] = form
        context["track"] = trackobj
    except Track.DoesNotExist:
        return HttpResponse("Track not found", status=404)

    return render(request, "track/update.html", context)


# =================================================================
def track_delete(request, id):
    try:
        if request.method == "POST":
            Track.delete_track(id)
            return JsonResponse({"success": True})
    except Track.DoesNotExist:
        return JsonResponse({"success": False, "error": "Track not found"}, status=404)


# =================================================================
def track_details(request, id):
    context = {}
    trackobj = Track.details_track(id)  # Fetch record from the database
    if trackobj is None:
        return HttpResponse("Track not found", status=404)
    context["track"] = trackobj
    return render(request, "track/details.html", context)
