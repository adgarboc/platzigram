from django.http import HttpResponse, JsonResponse
from django.utils import timezone


def hello_world(request):
    now = timezone.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')


def sort_numbers(request):
    # import pdb
    #  pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'data': sorted_numbers
    }
    return JsonResponse(
        data,
        safe=False
    )


def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}! Welcome to Platzigram'
    return JsonResponse(
        message,
        safe=False
    )
