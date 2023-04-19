from rest_framework.routers import DefaultRouter
from member_church.views import MemberChurchViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', MemberChurchViewSet, 'member-church-crud')

urlpatterns = router.urls