from django import forms
from .models import Submission

class NewIdeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        # exclude = ('idea',)
        fields = ['url_to']

    def __init__(self, *args, **kwargs):
        self.idea = kwargs.pop('idea', None)
        self.author = kwargs.pop('author', None)
        super(NewIdeaSubmissionForm, self).__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        submissions = self.idea.submissions.filter(
            author=self.author
        )
        if submissions:
            raise forms.ValidationError("You've done that bro.")





