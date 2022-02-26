from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.api.serializers import RoomsSerializer, RoomSerializer
from base.models import Room


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/rooms/',
        'GET /api/rooms/<int:room_id>/',

    ]
    return Response(routes)


@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomsSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_room(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
