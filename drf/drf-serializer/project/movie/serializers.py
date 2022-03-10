from django.db.models import IntegerField
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    @staticmethod
    def is_valid_rating(value):
        if value < 1:
            raise serializers.ValidationError("rating can not be lower than 1")
        elif value > 10:
            raise serializers.ValidationError("rating can not be higher than 10")

    rating = IntegerField(validators=[is_valid_rating])

    class Meta:
        model = Movie
        fields = "__all__"

    # custom validation
    # def validate_rating(self, value):
    #     if value < 1 or value > 10:
    #         raise serializers.ValidationError("rating has to be between 1 and 10.")
    #     return value

    # object-level validation
    def validate(self, data):
        if data["us_gross"] > data["worldwide_gross"]:
            raise serializers.ValidationError(
                "worldwide_gross can not be bigger than us_gross"
            )
        return data
