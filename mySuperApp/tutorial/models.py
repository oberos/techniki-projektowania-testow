from django.db import models


class Companies(models.Model):
    company_name = models.CharField(max_length=100)
    company_nip = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name
