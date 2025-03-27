from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraineeViewSet

router = DefaultRouter()
router.register(r'', TraineeViewSet)  # هنستخدم هنا عنوان أساسي، مثلاً "trainees/"

urlpatterns = [
    path('', include(router.urls)),
]
