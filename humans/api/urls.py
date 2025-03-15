from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import HumanViewSet

router = SimpleRouter()

router.register('', HumanViewSet)
urlpatterns = router.urls