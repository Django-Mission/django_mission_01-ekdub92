from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    return render(request, 'lotto.html')


def result(request):
    number = request.GET.get('number')
    result = []

    for _ in range(int(number)):
        temp = []
        for _ in range(6):
            temp.append(random.randint(1,45))
        result.append(temp)

    return render(request, 'result.html', {'number' : number, 'result' : result})
