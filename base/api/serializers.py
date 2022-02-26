from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomsSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class HostSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class RoomSerializer(ModelSerializer):
    host = HostSerializer(read_only=True)
    participants = HostSerializer(read_only=True, many=True)
    topic = SerializerMethodField()

    class Meta:
        model = Room
        exclude = ['id']

    def get_topic(self, obj):
        return obj.topic.name
