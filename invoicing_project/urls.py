from django.urls import path, include
from rest_framework.routers import DefaultRouter
from invoices.views import InvoiceViewSet,InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicesDetails', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
