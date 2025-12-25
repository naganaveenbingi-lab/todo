from django import forms

class TodolistForm(forms.Form):
    text = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a new todo item', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))