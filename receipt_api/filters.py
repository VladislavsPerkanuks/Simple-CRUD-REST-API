from django_filters import rest_framework as filters

from receipt_api.models import Receipt


class ItemFilter(filters.FilterSet):
    product_name = filters.CharFilter(field_name="product_name")


class ReceiptFilter(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter(field_name="created_on", label="date")
    item = filters.CharFilter(field_name="items", lookup_expr="product_name")

    class Meta:
        model = Receipt
        fields = ("id", "created_on", "items")
