from django.shortcuts import render

def home(request):
    context = {
        'kata':'ini halaman home'
    }
    return render(request, 'index.html', context)