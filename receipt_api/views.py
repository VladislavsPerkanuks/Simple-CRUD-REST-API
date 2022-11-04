import json

from django.http import HttpResponseNotFound, HttpResponseServerError
from django_filters import rest_framework as filters
from rest_framework import viewsets

from receipt_api.filters import ReceiptFilter
from receipt_api.models import Receipt
from receipt_api.serializers import ReceiptSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReceiptFilter


def error404(request, *args, **kwargs):
    response_data = {"detail": "Not found", "code": 404}

    return HttpResponseNotFound(json.dumps(response_data), content_type="application/json")


def error500(request, *args, **kwargs):
    response_data = {"detail": "Internal server error", "code": 500}

    return HttpResponseServerError(json.dumps(response_data), content_type="application/json")
