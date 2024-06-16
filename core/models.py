from django.db import models




# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="about")
    resume = models.FileField(upload_to="resumes", null=True, blank=True)

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")
    icon = models.ImageField(upload_to="about",null=True)

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Work link")


    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name