from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from ..serializers import ProjectSerializer
from ..models import Project

class ProjectApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ProjectSerializer, 
        responses={
            200: ProjectSerializer(many=True)
        }
    )

    def post(self, request):
        data = request.data
        user = request.user
        data["owner"] = user.id
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    @swagger_auto_schema(
            operation_description="get all product",
            responses={
                200:ProjectSerializer(many=True)
            }
    )

    def get(self, request):
        product = Project.objects.all()
        serializer = ProjectSerializer(product, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ProjectSerializer,
        responses={
            200:ProjectSerializer(many=True)
        }
    )
    def put(self, request, pk):
        product = Project.objects.get(id=pk)
        serializer = ProjectSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




