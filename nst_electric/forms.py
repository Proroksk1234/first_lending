from django import forms

phone_regex = r'^(\+375|80|375)(29|25|44|33)(\d{3})(\d{2})(\d{2})$'
name_regex = r'^[а-яА-ЯёЁa-zA-Z]{1,20}$'


class FormRequest(forms.Form):
    username = forms.CharField(max_length=20, label='Ваше имя', widget=forms.TextInput(
        attrs={'placeholder': 'Ваше имя', 'required pattern': name_regex,
               'oninvalid': "this.setCustomValidity('Введите корректные значения')", 'oninput':"setCustomValidity('')"}))
    email = forms.EmailField(label='Ваш e-mail', widget=forms.EmailInput(
        attrs={'placeholder': 'Ваш e-mail', 'oninvalid': "this.setCustomValidity('Введите корректный e-mail')", 'oninput':"setCustomValidity('')"}))
    number = forms.CharField(label='Ваш номер телефона', widget=forms.TextInput(
        attrs={'placeholder': 'Ваш телефон', 'required pattern': phone_regex,
               'oninvalid': "this.setCustomValidity('Введите корректный номер телефона в формате(+375)')", 'oninput':"setCustomValidity('')"}))
