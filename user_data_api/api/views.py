from rest_framework import generics
from .serializers import UserDataModelSerializer
from .models import UserDataModel
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset = UserDataModel.objects.all()
    serializer_class = UserDataModelSerializer

    def perform_create(self, serializer):
        serializer.save()


class GetDataByNameView(APIView):
    def get(self, request, name):
        user_data = UserDataModel.objects.get(name=name)
        serializer = UserDataModelSerializer(user_data)
<<<<<<< HEAD
        return Response(serializer.data)

=======
        return Response(serializer.data)
>>>>>>> ef4618ab7d04d43453adf3201c5e14a69a3c7862
