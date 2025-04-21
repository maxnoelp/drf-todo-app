from rest_framework import viewsets
from .serializers import TodoSerializer, SkillSerializer, ProjectsSerializer
from .models import Todo, Projects, Skill
from rest_framework.permissions import IsAuthenticated
from .permission import ReadOnly


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]


class SkillView(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    permission_classes = [ReadOnly]


class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    permission_classes = [ReadOnly]
