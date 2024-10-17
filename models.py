from django.db import models


# Create your models here.
class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField(max_length=50)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=40)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    address = models.TextField()
    password = models.CharField(max_length=70)
    status = models.CharField(max_length=40, default='pending')
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)


class Notification(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=70)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now=True)


class Category(models.Model):
    title = models.CharField(max_length=80)


class Movie(models.Model):
    title = models.CharField(max_length=60)
    category = models.TextField()
    cast = models.CharField(max_length=40)
    description = models.TextField()
    director = models.CharField(max_length=60)
    duration = models.DurationField()
    release_date = models.DateField()
    language = models.CharField(max_length=60)
    thumbnail = models.ImageField()
    movie_video = models.FileField()


class Webseries(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    cast = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    language = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    webseries_video = models.FileField()

    def __str__(self):
        return self.title


class Episode(models.Model):
    webseries = models.ForeignKey(Webseries, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    episode_number = models.PositiveIntegerField()
    release_date = models.DateField()
    thumbnail = models.FileField()
    video = models.FileField()


class Serials(models.Model):
    title = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    duration = models.DurationField()
    description = models.TextField()
    director = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    episode = models.FileField()


class Serials_Episodes(models.Model):
    serial = models.ForeignKey(Serials, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='episodes/')
    description = models.TextField()
    thumbnail = models.FileField()
    episode_number = models.IntegerField()


class Movie_Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    customer_email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    review = models.CharField(max_length=150)
    rating = models.CharField(max_length=200)


class Webseries_Review(models.Model):
    web_series = models.ForeignKey(Webseries, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    customer_email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    review = models.CharField(max_length=150)
    rating = models.CharField(max_length=200)


class Serial_Review(models.Model):
    serial = models.ForeignKey(Serials, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    customer_email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    review = models.CharField(max_length=150)
    rating = models.CharField(max_length=200)


class AdminLogin(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)


class Subscription(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    months = models.IntegerField()
    cost = models.BigIntegerField()
    discount = models.BigIntegerField()
    date_time = models.DateTimeField(auto_now=True)


class Subscribers(models.Model):
    customer_email = models.EmailField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    holder_name = models.CharField(max_length=100)
    card_number = models.BigIntegerField()
    cvv_number = models.BigIntegerField()
    bank_name = models.CharField(max_length=100)
