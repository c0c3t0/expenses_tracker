from django import forms

from expenses.expenses_app.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].label = 'Budget:'
        self.fields['first_name'].label = 'First Name:'
        self.fields['last_name'].label = 'Last Name:'
        self.fields['image'].label = 'Profile Image:'

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        widget = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-file'
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].label = 'Budget:'
        self.fields['first_name'].label = 'First Name:'
        self.fields['last_name'].label = 'Last Name:'
        self.fields['image'].label = 'Profile Image:'

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-file',
                },
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Expense.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title:'
        self.fields['description'].label = 'Description:'
        self.fields['expense_image'].label = 'Link to Image:'
        self.fields['price'].label = 'Price:'

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class EditExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title:'
        self.fields['description'].label = 'Description:'
        self.fields['expense_image'].label = 'Link to Image:'
        self.fields['price'].label = 'Price:'

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class DisabledFieldsFormMixin:
    fields = {}

    def _init_disabled_fields(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class DeleteExpenseForm(DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()
        self.fields['title'].label = 'Title:'
        self.fields['description'].label = 'Description:'
        self.fields['expense_image'].label = 'Link to Image:'
        self.fields['price'].label = 'Price:'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
