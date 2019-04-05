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


class UpdateView(generics.UpdateAPIView):
    queryset = UserDataModel.objects.all()
    serializer_class = UserDataModelSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = UserDataModel.objects.filter(name=request.data['name'])
        instance.pref_width = request.data.get("pref_width")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer.data)

