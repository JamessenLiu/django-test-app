from rest_framework import serializers
from .models import Companies
from rest_framework.validators import UniqueValidator


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Companies.objects.all())]
    )
    email = serializers.EmailField(
    )

    class Meta:
        model = Companies
        fields = "__all__"
