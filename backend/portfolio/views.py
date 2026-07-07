from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Profile, SkillCategory, Experience, Project,
    Education, Leadership, Award,
)
from .serializers import (
    ProfileSerializer, SkillCategorySerializer, ExperienceSerializer,
    ProjectSerializer, EducationSerializer, LeadershipSerializer,
    AwardSerializer, ContactMessageSerializer,
)


class PortfolioDataView(APIView):
    """
    GET /api/portfolio/
    Returns all portfolio data in a single response.
    """

    def get(self, request):
        profile = Profile.objects.first()
        skill_categories = SkillCategory.objects.prefetch_related('skills').all()
        experiences = Experience.objects.prefetch_related('bullets').all()
        projects = Project.objects.prefetch_related('bullets').all()
        education = Education.objects.all()
        leadership = Leadership.objects.prefetch_related('bullets').all()
        awards = Award.objects.all()

        data = {
            'profile': ProfileSerializer(profile).data if profile else {},
            'skill_categories': SkillCategorySerializer(skill_categories, many=True).data,
            'experiences': ExperienceSerializer(experiences, many=True).data,
            'projects': ProjectSerializer(projects, many=True).data,
            'education': EducationSerializer(education, many=True).data,
            'leadership': LeadershipSerializer(leadership, many=True).data,
            'awards': AwardSerializer(awards, many=True).data,
        }

        return Response(data, status=status.HTTP_200_OK)


class ContactMessageView(APIView):
    """
    POST /api/contact/
    Accepts contact form submissions.
    """

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Thank you for reaching out. I will get back to you soon.'},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
