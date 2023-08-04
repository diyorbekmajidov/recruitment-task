from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers import InvestorSerializer
from ..models import Investor

class Invistor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Investor register', 
        responses={
            200: InvestorSerializer(many=True)
        }
    )
    def post(self, request):
        data = request.data
        user = request.user
        data["user"] = user.id
        print(data)
        serializer = InvestorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
    investor/: get by id
    """
    @swagger_auto_schema(
        operation_description='Get Investor all',
        responses={ 
            200: 'Investor all'
        }
    )
    def get(self, request) :
        investor = Investor.objects.all()
        serializer = InvestorSerializer(investor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    """
    investor/ update by invistor id
    """
    @swagger_auto_schema(
            responses={
            200: InvestorSerializer(many=True)
        }
    )

    def put(self, request,pk):
        investor = Investor.objects.get(id=pk)
        serializer = InvestorSerializer(instance=investor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
