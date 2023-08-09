from rest_framework import ser
from .models import Regist

class RegistSerial(serializer.ModelSerializer):
    class Meta:
        model=Regist
        fields = ('__all__')