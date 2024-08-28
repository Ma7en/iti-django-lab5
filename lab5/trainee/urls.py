from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from .api.views import *

urlpatterns = [
    # views
    # path("", trainee_list, name="trainee_list"),
    # path("Add/", trainee_create, name="trainee_create"),
    # class views
    path("", TraineeListG.as_view(), name="trainee_list"),
    path("Add/", TraineeCreate.as_view(), name="trainee_create"),
    path("Update/<int:id>", trainee_update, name="trainee_update"),
    path("Delete/<int:id>", trainee_delete, name="trainee_delete"),
    path("Details/<int:id>", trainee_details, name="trainee_details"),
    # path("Details/<int:id>", TraineeDetailsG.as_view(), name="trainee_details"),
    # API
    # path("API/", include("api.urls")),
    path("API/", trainne_list_api),
    path("API/Add/", trainne_create_api),
    path("API/Update/<int:id>", trainne_update_api),
    path("API/Delete/<int:id>", trainne_delete_api),
    path("API/Details/<int:id>", trainne_details_api),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
