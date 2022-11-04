from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from receipt_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"receipts", views.ReceiptViewSet, basename="receipts")

urlpatterns = [
    path("", include(router.urls), name="receipts"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
