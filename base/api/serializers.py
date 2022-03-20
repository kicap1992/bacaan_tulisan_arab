from rest_framework.serializers import ModelSerializer
from base.models import tb_bacaan


class tb_bacaanSerializer(ModelSerializer):
    class Meta:
        model = tb_bacaan
        fields = '__all__'