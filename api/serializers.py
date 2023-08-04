from .models import User, Investor, Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class InvestorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Investor
        fields = ['id', 'user', 'budget', 'project_deadline']

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    investor = InvestorSerializer()
    class Meta:
        model = Project
        fields = ['id', 'owner', 'name', 'min_investment_amount', 'deadline', 'invested', 'investor']