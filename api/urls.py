from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('task',views.taskviewset,basename="task")

urlpatterns = [
    path('register/',views.signupview.as_view(),name="reg"),
    path('token',ObtainAuthToken.as_view())
]+router.urls