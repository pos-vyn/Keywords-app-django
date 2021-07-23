from django.urls import path, include,re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'keywords', views.KeywordsView)
router.register(r'registration', views.RegistrationView)


urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]



           