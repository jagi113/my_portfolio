from django import forms

class ContactForm(forms.Form):
    error_css_class = "text-red-700"
    required_css_class = "text-red-700"
    
    name = forms.CharField(max_length=100, )
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': 'Enter Name', 
            'required': True})

        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Your@Email.com',
            'required': True})

        self.fields['message'].widget = forms.Textarea(attrs={
            'placeholder': 'Enter Your Message',
            'required': True})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full rounded-md p-4'

        
class Meta:
    model = ContactForm
    error_messages = {
        "name": {
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter name!",
        },
        "email": {
            "required": "Your email address must not be empty!",
            'invalid': 'Wrong email address format. Enter email address as: your@email.com',
        },
        "message": {
            "required": "Your message must not be empty!",
        }
    }