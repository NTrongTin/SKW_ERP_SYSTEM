from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    print('View=home')
    return render(request, 'home.html', {'section': 'home'})