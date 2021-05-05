from django.db import models
import logging

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)

class DistrictManager(models.Manager):
    pass

class SuperheroManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")
        # all_dogs = self.all()
        # self == 'objects'

    def get_stale_widgets(self, cutoff):
        return # ....

    #  create complex queries and return results here

class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def my_extra_method(self):
        return 42

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    @classmethod
    def model_repr(cls):
        return 42

    @staticmethod
    def bar():
        return "wombat"

    def blah(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):

    @classmethod
    def make_field(cls):
        return "foo"

    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
#    myfield = models.CharField(max_length=10)

    objects = SuperheroManager()
    # mgr1 = ThisManager()
    # mgr2 = ThatManager()

    # Superhero.mgr1.method1()
    # Superhero.mgr1.method2()
    # Superhero.mgr2.method_foo()

    districts = DistrictManager()
    # MyModel.districts.all()
    # MyModel.districts.filter(zip_code='22222')

    # a = MyModel.districts.all()
    # b = MyModel.regions.active()
    # result = a | b
    # r = result.distinct().order_by()...

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['secret_identity']
        # app_label = 'superheroes'
        # db_table = 'superhero'
        # managed = False   # default = True
        # permissions = [
        #     ('can_update', 'User update allowed'),
        # ]
        # default_permissions = ['view']
        # indexes = [
        #
        # ]
        # unique_together = [('secret_identity', 'real_name')]
        # verbose_name = 'Story'
        # verbose_name_plural = 'Stories'

    def get_brief_enemies(self):
        # should be prefetch_related(...)
        enemies = [e.name.split()[-1][:4] for e in self.enemies.all()]
        return '/'.join(enemies)

    def save(self, *args, **kwargs):
        logging.info("Created superhero {}".format(self.name))
        super().save(*args, **kwargs)
        # do something else here as needed

# Superhero.myfield.default=Superhero.make_field

