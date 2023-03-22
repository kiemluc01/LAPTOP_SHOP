from django.db import models
# from django.contrib.gis.db import models as gis_models

class BaseCreateModel(models.Model):
    created_at = models.DateTimeField('Created At', auto_now_add=True, null=True)

    class Meta:
        abstract = True

class BaseCreateUpdateModel(BaseCreateModel):
    updated_at = models.DateTimeField('Updated At', auto_now=True, null=True)

    class Meta:
        abstract = True
