from django.db import models


class TimeStampModel(models.Model):
    added_by = models.CharField(max_length=250, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    last_modified_by = models.CharField(max_length=250, null=True, blank=True)
    last_modified_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Authentication(TimeStampModel):
    source_key = models.CharField(max_length=30, null=True, blank=True, verbose_name='Authentication Source Key')

    def __str__(self):
        return f'{self.source_key} -{self.added_by}'
