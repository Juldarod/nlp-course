from django import forms


class InputForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15'}))
