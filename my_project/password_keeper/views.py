from django.shortcuts import render


def index_view(request):
    index_page = 'index.html'
    return render(request, index_page)

