from .models import User, Investor, Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'owner', 'name', 'min_investment_amount', 'deadline', 'invested', 'investor']

class InvestorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Investor
        fields = "__all__"

    def get_user(self, obj):
        return UserSerializer(obj.user).data