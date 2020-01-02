from django.db import models

class Category(models.Model):
    catTitle = models.CharField(max_length=200)

    def __str__(self):
        return self.catTitle


class Todo(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        if self.isCompleted:
            return self.title + " (выполнено)"
        else:
            return self.title