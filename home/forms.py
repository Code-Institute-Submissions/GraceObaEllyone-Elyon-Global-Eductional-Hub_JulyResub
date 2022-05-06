from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={"rows": 7})
    )

    class Meta:
        fields = ['name', 'email', 'message']
