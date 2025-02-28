from main.models import Epos, Manaschi, Researchers


class StyleFormMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EposForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Epos
        fields = '__all__'


class ManaschiForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Manaschi
        fields = '__all__'


class ResearchersForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Researchers
        fields = '__all__'


