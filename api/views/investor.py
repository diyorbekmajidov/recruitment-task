from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from ..serializers import InvestorSerializer,InvestorGetSerializer
from ..models import Investor

class InvistorApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body = InvestorSerializer(), 
        responses={
            200: InvestorSerializer(many=True)
        }
    )
    def post(self, request):
        data = request.data
        user = request.user
        data["user"] = user.id
        serializer = InvestorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_description='Get all Investor ',
        responses={ 
            200: 'Investor all'
        }
    )
    def get(self, request) :
        investor = Investor.objects.all()
        serializer = InvestorSerializer(investor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class InvestorUpdate(APIView):
    @swagger_auto_schema(
        request_body=InvestorSerializer,
        operation_description='Update by investor id',
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

class InvestorGet(APIView):
    
    @swagger_auto_schema(
        operation_description=
        "bu API endpoint, tanlangan investor byudjetiga mos keladigan barcha loyihalarni chiqaradi.",
        responses={
            200: InvestorGetSerializer(many=True)
        }
    )
    def get(self, request, pk):

        invistor = Investor.objects.get(id=pk)
        serializer = InvestorGetSerializer(invistor)
        return Response(serializer.data, status=status.HTTP_200_OK)
                 