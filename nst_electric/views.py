# import telepot
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import FormRequest
from electrical.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
import re


class Done(TemplateView):
    template_name = 'nst_electric/done.html'


def Home(request):
    context = {'form': FormRequest(),
               'legal1': LegalService.objects.all()[0:5:2],
               'legal2': LegalService.objects.all()[1:6:2],
               'clean1': CleanService.objects.all()[0:5:2],
               'clean2': CleanService.objects.all()[1:6:2],
               'draft1': DraftService.objects.all()[0:5:2],
               'draft2': DraftService.objects.all()[1:6:2],
               'reviews': Review.objects.all(),
               'advantages': Advantages.objects.all(),
               'navigates': Navigate.objects.all(),
               'stages': StageWork.objects.all(),
               }

    if request.method == 'GET':
        return render(request, 'nst_electric/home.html', {'context': context})

    if request.method == 'POST':  # If the form has been submitted...
        form = FormRequest(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            number = form.cleaned_data['number']
            result_number = re.match(r'^(\+375|80|375)(\(33\)|\(44\)|\(25\)|\(29\)|29|25|44|33)(\d{3})(\d{2})(\d{2})$', number)
            result_username = re.match(r'^[а-яА-ЯёЁa-zA-Z]{1,20}$', username)
            result_email = re.match(r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$", email)
            if bool(result_username) == False or bool(result_number) == False or bool(result_email) == False:
                return HttpResponse(status=404)
            send_mail(f'Заказ на электромонтажные услуги от клиента', f'Имя клиента: {username}\n'
                                                                      f'Номер клиента: {number}\n'
                                                                      f'Email клиента: {email}\n',
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            return render(request, 'nst_electric/done.html', {'context': context})
        else:
            return HttpResponse(status=404)

# form.save()
# first_name = form.cleaned_data['first_name']
# additional_information = form.cleaned_data['additional_information']
# number = form.cleaned_data['number']
# services = form.cleaned_data['services']
# message = "*Заявка с формы*:" + "\n" + "*ИМЯ*: " + str(first_name) + "\n" + "*ТЕЛЕФОН*: " + str(
#     number) + "\n" + "*Услуги*: " + str(services) + "\n" + "*Дополнительная информация*: " + str(additional_information)
# send_message(message)
# return super(Forms, self).form_valid(form)
