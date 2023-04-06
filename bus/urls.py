from rest_framework.routers import DefaultRouter
from bus.views import BusViewSet


app_name = 'bus'

router = DefaultRouter(trailing_slash=False)
router.register(r'bus', BusViewSet)

urlpatterns = router.urls