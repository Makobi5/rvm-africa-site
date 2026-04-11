from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ministry(models.Model):
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
    
class HeroSlide(models.Model):
    title = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        help_text="Heading for news/events. Leave blank for pure branding images."
    )
    subtitle = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        help_text="Small text above the main title."
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text="Detailed text for news or events."
    )
    image = models.ImageField(upload_to='hero_slides/')
    button_text = models.CharField(max_length=50, default="Learn More")
    button_url = models.CharField(max_length=500, default="#")
    is_news_event = models.BooleanField(
        default=False, 
        help_text="Check this to show the specific title/desc typed above. Uncheck to show general branding text."
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(
        default=0, 
        help_text="Order of appearance (0, 1, 2...)"
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else f"Slide {self.id} (No Title)"