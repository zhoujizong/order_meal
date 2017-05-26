from __future__ import unicode_literals

from django.db import models

# Create your models here.

class staff_base_info(models.Model):
    staff_id = models.IntegerField(null = False)
    staff_name = models.CharField(null = False , max_length = 50)
    group_name = models.CharField(null = False , max_length = 50)

    def __unicode__(self) :
        return self.staff_name

    class Meta:
        ordering = ['staff_id']

class ordered_list(models.Model):
    staff_name = models.CharField(null = False , max_length = 50 , primary_key = True)

    def __unicode__(self) :
        return self.staff_name


class staff_action_log(models.Model):
    staff_id = models.IntegerField(null = False)
    staff_name = models.CharField(null = False , max_length = 50)
    group_name = models.CharField(null = False , max_length = 50)
    create_time = models.IntegerField(null = False)
    type = models.IntegerField(null = False)

    def __unicode__(self) :
        return self.staff_name
