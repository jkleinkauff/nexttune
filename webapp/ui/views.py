from django.shortcuts import render


def ui_index(request):
    return render(request, 'index.html', {})
