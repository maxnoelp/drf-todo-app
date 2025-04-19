from django.urls import path
from .views import TodoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TodoView, basename="todo")
urlpatterns = router.urls
