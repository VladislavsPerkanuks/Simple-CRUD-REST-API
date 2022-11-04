from rest_framework import serializers

from receipt_api.models import Item, Receipt


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("product_name",)


class ReceiptSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = ("id", "created_on", "items")

    def create(self, validated_data):
        # We remove all items from data, and assign to items
        items = validated_data.pop("items")
        # We create receipt object with id and created_on attributes
        receipt = Receipt.objects.create(**validated_data)

        # For each item we create Item object and assign it to receipt object
        for item in items:
            item, _ = Item.objects.get_or_create(**item)
            receipt.items.add(item)

        return receipt
