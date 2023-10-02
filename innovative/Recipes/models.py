from django.db import models

# Create your models here.
class Recipie(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250,unique=True)
    prep_time=models.IntegerField()
    Image=models.ImageField(upload_to='product',blank=True)
    difficulty=models.CharField(max_length=500)
    vegetarian=models.BooleanField(default=True)

    def get_url(self):
        return reverse('Recipies:detail',args=[self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='recipie'
        verbose_name_plural='recipies'
    def __str__(self):
        return self.name