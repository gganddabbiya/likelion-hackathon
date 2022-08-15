from django.db import models

class festival(models.Model):
    fe_title = models.CharField(max_length=200)
    fe_startDate = models.CharField(max_length=200)
    fe_endDate = models.CharField(max_length=200)
    fe_image = models.CharField(max_length=200)
    fe_place = models.CharField(max_length=200)
    fe_timeinfo = models.CharField(max_length=200)
    fe_age = models.CharField(max_length=200)
    fe_link = models.CharField(max_length=200)
    fe_detail_img = models.JSONField(default=dict)

    def __str__(self):
        return self.fe_title