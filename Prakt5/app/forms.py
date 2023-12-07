"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Blog
from django.db import models
from .models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше ФИО', min_length = 2, max_length = 100)
    city = forms.CharField(label = 'Ваш адрес', min_length = 2, max_length = 100)
    gender = forms.ChoiceField(label = 'Ваше пол', 
                             choices = [('1', 'Мужской'), ('2', 'Женский')],
                             widget = forms.RadioSelect, initial = 1)
    email = forms.EmailField(label = 'Ваша почта', min_length = 7)
    message = forms.CharField(label = 'Дополнительная информация (О заказе и т.д.)',
                              widget = forms.Textarea(attrs = {'rows':12, 'cols':20}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': 'Заголовок', 'description': 'Краткое содержание', 'content': 'Полное содержание', 'image': "Картинка"}

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
