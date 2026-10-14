from rest_framework import serializers

from customer.models import Customer
from customer.choice import GENDER_CHOICE


class GenderChoiceFieldSerializer(serializers.ChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(choices=GENDER_CHOICE, *args, **kwargs)


class CustomerSerializer(serializers.ModelSerializer):
    gender = GenderChoiceFieldSerializer()
    created = serializers.DateField(read_only=True)

    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "gender",
            "age",
            "favorite_number",
            "created",
        )
