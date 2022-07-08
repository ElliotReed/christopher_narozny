from django.shortcuts import render


def appearances(request):
    return render(request, "appearances/appearances.html")
