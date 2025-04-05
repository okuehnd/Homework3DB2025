from django import forms

class MemberLoginForm(forms.Form):
    mid = forms.CharField(widget=forms.TextInput())