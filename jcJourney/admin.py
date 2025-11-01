from django.contrib import admin
from .models import LearningJourney, AboutMe, AdminScreenshots  # ADD AdminScreenshots here

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    """
    Admin interface for Learning Journey items
    """
    list_display = ('title', 'category', 'date_learned', 'difficulty_level', 'is_completed')
    list_filter = ('category', 'difficulty_level', 'is_completed')
    search_fields = ('title', 'description')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    """
    Admin interface for personal information
    """
    list_display = ('full_name', 'student_id', 'email')

# ADD THIS NEW ADMIN CLASS
@admin.register(AdminScreenshots)
class AdminScreenshotsAdmin(admin.ModelAdmin):
    """
    Admin interface for Admin Screenshots
    """
    list_display = ('title', 'display_order', 'created_at')
    list_editable = ('display_order',)
    search_fields = ('title', 'description')