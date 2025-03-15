from django.contrib.auth import get_user_model
from rest_framework import generics

from humans.api.serializers import HumanSerializer
from rest_framework import viewsets


class HumanViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = HumanSerializer

