from django import forms
from events.models import Event, Participant, Category

def add_custom_classes(widget, placeholder=""):
    widget.attrs.update({
        'class': 'custom-input',
        'placeholder': placeholder
    })
    return widget

class CustomFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            placeholder = field.label or ""
            add_custom_classes(field.widget, placeholder)

class EventForm(CustomFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'category': forms.Select(),
        }

class CategoryForm(CustomFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}

class ParticipantForm(CustomFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = {'events': forms.SelectMultiple(attrs={'size': 5})}


class ParticipantSelectionForm(forms.Form):
    """Form to select existing participants or create new ones for an event"""
    existing_participants = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Select Existing Participants'
    )
    
    add_new = forms.BooleanField(
        required=False,
        label='Add a New Participant?',
        widget=forms.CheckboxInput(attrs={'class': 'form-checkbox'})
    )
    
    new_participant_name = forms.CharField(
        max_length=150,
        required=False,
        label='Participant Name',
        widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Enter participant name'
        })
    )
    
    new_participant_email = forms.EmailField(
        required=False,
        label='Participant Email',
        widget=forms.EmailInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Enter participant email'
        })
    )

    def __init__(self, *args, event=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event
        
        if event:
            already_added = event.participants.all()
            self.fields['existing_participants'].initial = already_added

    def clean(self):
        cleaned_data = super().clean()
        add_new = cleaned_data.get('add_new')
        name = cleaned_data.get('new_participant_name')
        email = cleaned_data.get('new_participant_email')
        
        if add_new:
            if not name or not email:
                raise forms.ValidationError(
                    'Please provide both name and email for the new participant.'
                )
        
        return cleaned_data

