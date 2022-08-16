from django.db import models


class Exhibition(models.Model):
    ex_title = models.CharField(max_length=200)
    ex_startDate = models.DateField()
    ex_endDate = models.DateField()
    ex_image = models.CharField(max_length=200)
    ex_place = models.CharField(max_length=200)
    ex_timeinfo = models.CharField(max_length=200)
    ex_age = models.CharField(max_length=200)
    ex_link = models.CharField(max_length=200)
    ex_detail_img = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return self.ex_title
