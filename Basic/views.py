from django.shortcuts import render
import random 

# Create your views here.
def lotto(request): 
    numbers = []
    for _ in range(7):
        numbers.append(random.randint(1,45))
    return render(request, 'lotto.html', {'numbers' : numbers})
