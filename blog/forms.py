from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if not body:
            raise forms.ValidationError("Body is required.")
        return body
