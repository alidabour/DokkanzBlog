from django import forms

class PostForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=200)
    content = forms.CharField(widget=forms.Textarea,label='Content')
    post_id = forms.IntegerField(widget=forms.HiddenInput,required=False)

class CommentForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea,label='Add Comment')