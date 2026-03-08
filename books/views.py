from django.http import JsonResponse

BOOKS = [
    {
        'title': f'Book {index}',
        'author': f'Author {((index - 1) % 20) + 1}',
        'year': 1950 + (index % 74),
        'pages': 120 + (index * 3),
        'borrowed': index % 2 == 0,
    }
    for index in range(1, 101)
]


def list_books(request):
    if request.method != 'GET':
        return JsonResponse({'detail': 'Method not allowed'}, status=405)
    return JsonResponse(BOOKS, safe=False)
