from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserSerializer

from api.models import User

class Register(APIView):
    @swagger_auto_schema(request_body=UserSerializer)

    def post(self, request: Request):
        data = request.data
        data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.create(user=serializer.instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors)
        
class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='User Logout',
        responses={
            200: 'User logged out'
        }
    )
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'success': 'User logged out'})
    
class UserLoginView(APIView):
    permission_classes = [IsAuthenticated]
    header_param = openapi.Parameter('Authorization',openapi.IN_HEADER,description="username", type=openapi.IN_HEADER)

    @swagger_auto_schema(operation_description='User Login', 
         manual_parameters=[header_param],
      )
    
    def post(self, request):
        user = request.user
        token = Token.objects.get_or_create(user=user)
        if token:
            token[0].delete()
        token= Token.objects.create(user=user)
        return Response({"token":token.key})

    
    
