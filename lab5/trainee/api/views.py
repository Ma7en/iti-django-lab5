from ..models import Trainee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.http import Http404
from .serializers import TraineeSerializer


@api_view(["GET"])
def trainne_list_api(request):
    trainees = Trainee.objects.all()
    traineejson = TraineeSerializer(trainees, many=True)
    return Response(data=traineejson.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def trainne_details_api(request, id):
    try:
        traineeobj = Trainee.objects.get(pk=id)
    except Trainee.DoesNotExist:
        raise Http404("Trainee not found")

    traineejson = TraineeSerializer(traineeobj)
    return Response(data=traineejson.data, status=status.HTTP_200_OK)


@api_view(["POST", "GET"])
def trainne_create_api(request):
    traineejson = TraineeSerializer(data=request.data)
    if traineejson.is_valid():
        traineejson.save()
        return Response(data=traineejson.data, status=status.HTTP_201_CREATED)
    return Response(data=traineejson.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST", "GET"])
# def trainne_create_api(request):
#     if request.method == "POST":
#         serializer = TraineeSerializer(data=request.data)
#         if serializer.is_valid():
#             # Access validated data
#             validated_data = serializer.validated_data

#             # Use validated data to create a new trainee
#             Trainee.create_trainee(
#                 Trainee,
#                 validated_data.get("first_name"),
#                 validated_data.get("last_name"),
#                 validated_data.get("date_of_birth"),
#                 validated_data.get("image"),
#                 None,
#                 None,
#             )
#             return Response(
#                 {"message": "Trainee created successfully"},
#                 status=status.HTTP_201_CREATED,
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Handle GET request or other methods here if needed
#     return Response(
#         {"message": "GET request not handled"},
#         status=status.HTTP_405_METHOD_NOT_ALLOWED,
#     )


# @api_view(["POST"])
# def trainne_create_api(request):
#     traineejson = TraineeSerializer(data=request.data)
#     if traineejson.is_valid():
#         # Access validated data
#         first_name = traineejson.validated_data.get("first_name")
#         last_name = traineejson.validated_data.get("last_name")
#         date_of_birth = traineejson.validated_data.get("date_of_birth")
#         image = traineejson.validated_data.get("image")

#         # Create the Trainee object using the validated data
#         Trainee.create_trainee(
#             Trainee,
#             first_name,
#             last_name,
#             date_of_birth,
#             image,
#             None,
#             None,
#         )
#     else:
#         # Handle invalid data
#         return Response(traineejson.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response(
#         {"success": "Trainee created successfully"}, status=status.HTTP_201_CREATED
#     )


@api_view(["PUT"])
def trainne_update_api(request, id):
    try:
        traineeobj = Trainee.objects.get(pk=id)
    except Trainee.DoesNotExist:
        raise Http404("Trainee not found")

    traineejson = TraineeSerializer(traineeobj, data=request.data)
    if traineejson.is_valid():
        traineejson.save()
        return Response(data=traineejson.data, status=status.HTTP_200_OK)
    return Response(data=traineejson.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def trainne_delete_api(request, id):
    try:
        traineeobj = Trainee.objects.get(pk=id)
    except Trainee.DoesNotExist:
        raise Http404("Trainee not found")

    traineeobj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
