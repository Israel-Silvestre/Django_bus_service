from rest_framework.routers import DefaultRouter
from member_bus.views import MemberBusViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', MemberBusViewSet, 'member-bus-crud')

urlpatterns = router.urls