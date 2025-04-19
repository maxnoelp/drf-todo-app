from django.urls import path, include
from .views import TodoView, SkillView, ProjectsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("todos", TodoView, basename="todo")
router.register("skills", SkillView, basename="skill")
router.register("projects", ProjectsView, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]
