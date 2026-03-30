from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self): # Fixed typo here too
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ministry(models.Model):
    # Fixed 'on_now' to 'on_delete'
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ministries/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    
    def __str__(self):
        return self.title