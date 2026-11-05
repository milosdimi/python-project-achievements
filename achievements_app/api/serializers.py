from rest_framework import serializers
from achievements_app.models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'category', 'earned_at']
        read_only_fields = ['id', 'earned_at']