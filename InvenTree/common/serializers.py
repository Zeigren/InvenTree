"""
JSON serializers for common components
"""

from InvenTree.serializers import InvenTreeModelSerializer

from .models import Currency


class CurrencySerializer(InvenTreeModelSerializer):
    """ Serializer for Currency object """

    class Meta:
        model = Currency
        fields = ["pk", "symbol", "suffix", "description", "value", "base"]
