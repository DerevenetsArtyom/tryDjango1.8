from django.db import models


class SignUp(models.Model):
    email = models.EmailField('Enter your E-mail', max_length=200)
    full_name = models.CharField('Enter your Full name', max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField('Created at', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Updated at', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
