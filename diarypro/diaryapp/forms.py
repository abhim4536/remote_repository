from django import forms
from .models import DiaryData


# class DiaryForm(forms.Form):
#     title = forms.CharField(
#         label='Enter Title',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Title'
#             }
#         )
#     )
#     body = forms.CharField(
#         label='Enter Note',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Note'
#             }
#         )
#     )
#     img = forms.ImageField(
#         label='Select Image',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'multiple': True,
#                 'class':'form-control',
#                 'placeholder':'Image'
#             }
#         )
#     )
#     img1 = forms.ImageField(
#         label='Select Image',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'multiple': True,
#                 'class': 'form-control',
#                 'placeholder': 'Image'
#             }
#         )
#     )
#     img2 = forms.ImageField(
#         label='Select Image',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'multiple': True,
#                 'class': 'form-control',
#                 'placeholder': 'Image'
#             }
#         )
#     )
#     img3 = forms.ImageField(
#         label='Select Image',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'multiple': True,
#                 'class': 'form-control',
#                 'placeholder': 'Image'
#             }
#         )
#     )

class DiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryData
        fields = ['title', 'body', 'img', 'img1', 'img2', 'img3']
