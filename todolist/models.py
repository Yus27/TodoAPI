from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    # date = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.isCompleted:
            return self.title + " (выполнено)"
        else:
            return self.title