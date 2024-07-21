from django import forms


class CommentForm(forms.Form):
    inputt = forms.CharField(max_length=50)
