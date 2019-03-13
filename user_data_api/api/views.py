from rest_framework import generics
from .serializers import UserDataModelSerializer
from .models import UserDataModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = UserDataModel.objects.all()
    serializer_class = UserDataModelSerializer

    def perform_create(self, serializer):
        serializer.save()


class GetDataByNameView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, name, year):
        user_data = UserDataModel.objects.get(name=name, birth_date__contains=year)
        serializer = UserDataModelSerializer(user_data)
        return Response(serializer.data)

