from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Create your views here.
users = ['Vasya', 'Alex', 'Pavel', 'Elena', 'Mike']


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Вы должны быть старше 18')
        elif username in users:
            return HttpResponse('Пользователь уже существует')
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                return HttpResponse('Пользователь уже существует')
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
