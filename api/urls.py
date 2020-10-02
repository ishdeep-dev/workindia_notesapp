from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import NoteViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('sites', NoteViewSet)


urlpatterns = [
    path('auth', obtain_auth_token),
    path('', include(router.urls)),
]
