from django.db import models

# Create your models here.


TICKET_TYPE = (
    ('VIP', 'VIP'),
    ('Luxury', 'Luxury'),
    ('Basic', 'Basic'),
    ('Normal', 'Normal'),
)


class Tictet(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number_of_person = models.IntegerField()
    date = models.DateField()
    ticket_type = models.CharField(max_length=100, choices=TICKET_TYPE)

    def __str__(self):
        return self.fullname
