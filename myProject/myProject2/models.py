from django.db import models # type: ignore[reportMissingModuleSource]

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


