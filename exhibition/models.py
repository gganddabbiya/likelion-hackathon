from django.db import models

class exhibition(models.Model):
    ex_title = models.CharField(max_length=200)
    ex_startDate = models.CharField(max_length=200)
    ex_endDate = models.CharField(max_length=200)
    ex_image = models.CharField(max_length=200)
    ex_place = models.CharField(max_length=200)
    ex_timeinfo = models.CharField(max_length=200)
    ex_age = models.CharField(max_length=200)
    ex_link = models.CharField(max_length=200)
    ex_detail_img = models.JSONField(default=dict)

    def __str__(self):
        return self.ex_title
