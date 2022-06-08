from rest_framework import serializers

from .models import keluarga

class keluargaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = keluarga
        fields = ('nama', 'jenis_kelamin', 'status')