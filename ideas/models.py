from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_at = models.DateField(auto_now = True)
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE, )


    def __str__(self):
        return f"{self.pk} - {self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('idea-detail', args=[self.pk])


class Submission(models.Model):
    unique_together = ('idea', 'author')
    idea    = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='submissions')
    url_to  = models.CharField(max_length=250)
    author  = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idea}"
