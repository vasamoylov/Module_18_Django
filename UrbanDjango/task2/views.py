from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def wellcome(request):
    return render(request, 'func_template.html')


class Wellcome(TemplateView):
    template_name = 'class_template.html'
