from django.http import JsonResponse

def home(request):
    return JsonResponse({'info': 'Django react', 'name': 'TX'})