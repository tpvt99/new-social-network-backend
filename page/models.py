from django.db import models

# Create your models here.

CITY_CODE = (
    ('vn-hochiminh', 'Ho Chi Minh'),
    ('vn-vungtau', 'Vung Tau'),
    ('vn-hanoi', 'Ha Noi'),
    ('vn-hue','Hue'),
    ('vn-danang', 'Da Nang'),
    ('vn-cantho', 'Can Tho'),
    ('vn-haiphong','Hai Phong'),
    )

COUNTRY_CODE = (
    ('vn','vietnam'),
    ('us','United States of America'),
    ('uk','United Kingdom'),
    )

class Country(models.Model):
    name_ascii = models.CharField(max_length = 100)
    name_unicode = models.CharField(max_length = 100, null = True)
    country_code = models.CharField(max_length = 2,
            choices = COUNTRY_CODE)

class City(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    name_ascii = models.CharField(max_length = 100)
    name_unicode = models.CharField(max_length = 100 , null = True)
    city_code = models.CharField(max_length = 100,
            choices = CITY_CODE)

