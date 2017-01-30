from django.db import models, transaction

class Model(models.Model):
	name = models.CharField(max_length=256, blank=False, unique=True, db_index=True)
