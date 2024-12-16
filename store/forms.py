from django import forms
from django.utils.translation import gettext as _

TUTORIAL_CHOICES = (
    ("پایتون", "پایتون"),
    ("app inventor", "app inventor"),
    ("اسکرچ", "اسکرچ"),
)
TUTORIAL_TYPE_CHOICES = (
    ("آنلاین", "آنلاین"),
    ("آفلاین", "آفلاین"),
)


class Register(forms.Form):
    name = forms.CharField(label=_('نام'), max_length=100,
                           required=True, error_messages={'invalid': 'مقدار نامعتبر است', 'required':"این فیلد ضروری است"})
    family = forms.CharField(label=_('نام خانوادگی'), max_length=100,
                             required=True, error_messages={'invalid': 'مقدار نامعتبر است', 'required':"این فیلد ضروری است"})
    age = forms.IntegerField(label=_('سن'),
                             required=True, error_messages={'invalid': 'مقدار نامعتبر است', 'required':"این فیلد ضروری است"})
    email = forms.EmailField(label=_('ایمیل'),
                             required=True, error_messages={'invalid': 'مقدار نامعتبر است', 'required':"این فیلد ضروری است"})
    mobile = forms.CharField(label=_('موبایل'), max_length=100,
                             required=True, error_messages={'invalid': 'مقدار نامعتبر است', 'required':"این فیلد ضروری است"})
    # tutorial = forms.CharField(label=_('دوره آموزشی'), max_length=100,
    #                            required=True)
    tutorial = forms.ChoiceField(label=_('دوره آموزشی') ,choices=TUTORIAL_CHOICES)
    type = forms.ChoiceField(label=_('نوع دوره') ,choices=TUTORIAL_TYPE_CHOICES)
