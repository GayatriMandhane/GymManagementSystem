from django.views.decorators.csrf import csrf_exempt #to access other domin to access our method
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from testdb.serializer import UserSerializer, RegisterSerializer

# Register API
@csrf_exempt
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })