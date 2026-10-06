from django import forms

SUBJECTS = [
    ("Buying a phone", "Buying a phone"),
    ("Lipa Pole Pole", "Lipa Pole Pole"),
    ("Trade-in", "Trade-in"),
    ("Repair", "Repair"),
    ("Accessories", "Accessories"),
    ("Unlock / flashing", "Unlock / flashing"),
    ("Other", "Other"),
]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "e.g. 0712 345 678", "autocomplete": "tel", "inputmode": "tel"}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"placeholder": "Optional", "autocomplete": "email"}))
    subject = forms.ChoiceField(choices=SUBJECTS)
    message = forms.CharField(max_length=1500, widget=forms.Textarea(attrs={"rows": 5, "placeholder": "How can we help? Phone model, problem, budget..."}))
    # Hidden spam trap: real people leave this empty
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))