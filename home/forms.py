from django import forms


class ContactForm(forms.Form):
    SUBJECT_CHOICES = (
        ('Corporate & Group Course Inquiry',
         'Corporate & Group Course Inquiry'),
        ('Course Recommendation Inquiry', 'Course Recommendation Inquiry'),
        ('Other', 'Other'),
    )

    name = forms.CharField(
        label="Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.Select(choices=SUBJECT_CHOICES),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 7,
        })
    )

    class Meta:
        fields = ['name', 'email', 'subject', 'message']
