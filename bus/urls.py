from rest_framework.routers import DefaultRouter
from bus.views import BusViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', BusViewSet, 'bus-crud')

urlpatterns = router.urls