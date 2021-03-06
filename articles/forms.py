from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Article


class AddArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget()

    class Meta:
        model = Article
        fields = ["title", "image", "content"]
