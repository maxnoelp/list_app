from django.shortcuts import render


def myList(request):
    return render(request, "shopping_list.html")
