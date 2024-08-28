from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from account.models import *
from track.models import *
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# @login_required()
@method_decorator(login_required, name="dispatch")

# =================================================================
# def trainee_list(request):
#     context = {}
#     # traineesobj = Trainee.objects.all()  # Fetch all records from the database
#     trainees = Trainee.list_trainee()
#     context["trainees"] = trainees
#     return render(request, "trainee/list.html", context)


class TraineeListG(ListView):
    model = Trainee
    template_name = "trainee/list.html"
    context_object_name = "trainees"


# =================================================================
# def trainee_create(request):
#     context = {}
#     form = CreateTrainee()
#     context["form"] = form
#     if request.method == "POST":
#         form = CreateTrainee(request.POST, request.FILES)
#         if form.is_valid():
#             traineeobj = Trainee.create_trainee(
#                 form.cleaned_data["first_name"],
#                 form.cleaned_data["last_name"],
#                 form.cleaned_data["date_of_birth"],
#                 form.cleaned_data["image"],
#                 form.cleaned_data["account_obj"],
#                 form.cleaned_data["track_obj"],
#             )
#             return redirect(traineeobj)
#         else:
#             context["error"] = form.errors
#     return render(request, "trainee/create.html", context)


# def trainee_create(request):
#     context = {}
#     form = CreateTraineeModel()
#     context = {"form": form}
#     if request.method == "POST":
#         form = CreateTraineeModel(request.POST, request.FILES)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect(Trainee.get_list_url)
#     return render(request, "trainee/create.html", context)


class TraineeCreate(View):
    # request method get --> call instantiate get
    context = {}
    # context["accounts"] = Account.objects.all()
    # context["tracks"] = Track.objects.all()

    def get(self, request):
        form = CreateTraineeModel()
        self.context["form"] = form
        return render(request, "trainee/create.html", TraineeCreate.context)

    def post(self, request):
        form = CreateTraineeModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(Trainee.get_list_url())
        else:
            self.context["form"] = form
            self.context["error"] = form.errors

        return render(request, "trainee/create.html", self.context)


# =================================================================
def trainee_update(request, id):
    context = {}
    try:
        traineeobj = Trainee.objects.get(id=id)
        form = UpdateTrainee(
            initial={
                "first_name": traineeobj.first_name,
                "last_name": traineeobj.last_name,
                "date_of_birth": traineeobj.date_of_birth,
                "image": traineeobj.image,
                "account_obj": traineeobj.account_obj,
                "track_obj": traineeobj.track_obj,
            }
        )

        if request.method == "POST":
            form = UpdateTrainee(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = (form.cleaned_data["last_name"],)
                date_of_birth = (form.cleaned_data["date_of_birth"],)

                image = form.cleaned_data.get("image")
                if not image:
                    image = traineeobj.image

                account_obj = Account.objects.get(id=form.cleaned_data["account_obj"])
                track_obj = Track.objects.get(id=form.cleaned_data["track_obj"])

                trainee_url = Trainee.update_trainee(
                    id,
                    first_name,
                    last_name,
                    date_of_birth,
                    image,
                    account_obj,
                    track_obj,
                )
                return redirect(trainee_url)
            else:
                context["error"] = form.errors

        context["form"] = form
        context["trainee"] = traineeobj

    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)

    return render(request, "trainee/update.html", context)


# class TraineeUpdateG


# =================================================================
def trainee_delete(request, id):
    try:
        if request.method == "POST":
            Trainee.delete_trainee(id)
            return JsonResponse({"success": True})
    except Trainee.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "Trainee not found"}, status=404
        )


class TraineeDelete(DeleteView):
    model = Trainee
    success_url = reverse_lazy("trainee_list")


# =================================================================
def trainee_details(request, id):
    context = {}
    try:
        traineeobj = Trainee.details_trainee(id)
        context["trainee"] = traineeobj
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)
    return render(request, "trainee/details.html", context)


# class TraineeDetailsG(DetailView):
#     model = Trainee
#     template_name = "trainee/details.html"
#     context_object_name = "trainee"
