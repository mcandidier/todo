from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    """ Todo models
    """
    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    checklist = models.ManyToManyField("todo.Checklist", blank=True, null=True)

    def __str__(self):
        return "{}".format(self.content)

    @property
    def checklist_count(self):
        return self.checklist.all().count()


class Checklist(models.Model):
    """ Checklist for todo
    """
    title = models.CharField(max_length=220)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.done)


class Attachments(models.Model):
    """ Todo attachments
    """

    file = models.FileField(upload_to='uploads/')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="attachments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Attachments"