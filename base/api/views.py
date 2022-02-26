from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/rooms/',
        'GET /api/rooms/<int:room_id>/',

    ]
    return Response(routes)
