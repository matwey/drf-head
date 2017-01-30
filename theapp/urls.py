from theapp import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'models', views.ModelViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]
