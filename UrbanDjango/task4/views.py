from django.shortcuts import render


# Create your views here.

def wellcome(request):
    return render(request, 'main_page.html')


def games(request):
    games_list = ['GTA V', 'NFS', 'FIFA']
    context = {'games_list': games_list}
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
