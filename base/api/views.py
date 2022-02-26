from django.http import JsonResponse

def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/rooms/',
        'GET /api/rooms/<int:room_id>/',

    ]
    return JsonResponse(routes, safe=False)
