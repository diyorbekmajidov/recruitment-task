from .models import User, Investor, Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ProjectGetSerializer(serializers.ModelSerializer):
    invistor = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id','name','min_investment_amount','deadline','invested','invistor']

    def get_invistor(self, obj):
        invistor = Investor.objects.filter(budget__gte=obj.min_investment_amount)
        return InvestorSerializer(invistor, many=True).data

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__" 

class InvestorGetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    loyha = serializers.SerializerMethodField()
    class Meta:
        model = Investor
        fields = ['id','budget','user','loyha']

    def get_user(self, obj):
        return UserSerializer(obj.user).data
    
    
    def get_loyha(self, obj):
        project = Project.objects.filter(min_investment_amount__lte=obj.budget)
        return ProjectSerializer(project, many=True).data