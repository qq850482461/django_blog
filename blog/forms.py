from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Post, About


class PostForm(forms.ModelForm):
    """
    admin post后台表单
    """
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = "__all__"


class AboutForm(forms.ModelForm):
    """
    admin about后台表单
    """
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = About
        fields = "__all__"
