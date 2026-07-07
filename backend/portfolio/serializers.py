from rest_framework import serializers
from .models import (
    Profile, SkillCategory, Skill, Experience, ExperienceBullet,
    Project, ProjectBullet, Education, Leadership, LeadershipBullet,
    Award, ContactMessage,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']


class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = ['id', 'name', 'order', 'skills']


class ExperienceBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceBullet
        fields = ['id', 'title', 'content', 'skills_used', 'order']


class ExperienceSerializer(serializers.ModelSerializer):
    bullets = ExperienceBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id', 'company', 'role', 'location',
            'start_date', 'end_date', 'description', 'order', 'bullets',
        ]


class ProjectBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBullet
        fields = ['id', 'title', 'content', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    bullets = ProjectBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'subtitle', 'description',
            'tech_stack', 'github_url', 'live_url', 'order', 'bullets',
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class LeadershipBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipBullet
        fields = ['id', 'title', 'content', 'order']


class LeadershipSerializer(serializers.ModelSerializer):
    bullets = LeadershipBulletSerializer(many=True, read_only=True)

    class Meta:
        model = Leadership
        fields = [
            'id', 'organization', 'role', 'location',
            'start_date', 'end_date', 'order', 'bullets',
        ]


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
