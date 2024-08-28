from rest_framework import serializers


class TraineeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    # image = serializers.ImageField(allow_empty_file=True, required=False)
