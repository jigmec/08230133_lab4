from django.db import models

class LearningJourney(models.Model):
    """
    Model to track Jigme Choden's learning progress in web development
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_learned = models.DateField()
    category = models.CharField(max_length=100, choices=[
        ('django', 'Django Framework'),
        ('python', 'Python Programming'),
        ('html', 'HTML & CSS'),
        ('javascript', 'JavaScript'),
        ('database', 'Database'),
        ('deployment', 'Deployment'),
    ])
    difficulty_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"

    class Meta:
        verbose_name_plural = "Learning Journey Items"
        ordering = ['-date_learned']

class AboutMe(models.Model):
    """
    Model to store Jigme Choden's personal information
    """
    full_name = models.CharField(max_length=100, default="Jigme Choden")
    student_id = models.CharField(max_length=20, default="02230283")
    email = models.EmailField(default="jigme@example.com")
    bio = models.TextField(default="Computer Science student passionate about web development and Django framework.")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    interests = models.TextField(default="Web Development, Programming, Technology, Reading")
    skills = models.TextField(default="Python, Django, HTML, CSS, JavaScript, SQL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.student_id}"

    class Meta:
        verbose_name_plural = "About Me Information"

# ADD THIS NEW MODEL RIGHT HERE
class AdminScreenshots(models.Model):
    """
    Model to store admin interface screenshots information
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='admin_screenshots/', blank=True, null=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Admin Screenshots"
        ordering = ['display_order']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Admin Screenshots"
        ordering = ['display_order']