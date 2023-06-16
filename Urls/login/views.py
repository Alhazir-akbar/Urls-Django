from django.shortcuts import render

def login(request):
    context = {
        'kata':'halaman login'
    }
    return render(request, 'login/index.html', context)
