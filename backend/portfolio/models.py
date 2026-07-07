from django.db import models


class Profile(models.Model):
    """Personal information and summary."""
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.full_name


class SkillCategory(models.Model):
    """Skill category grouping (Languages, Frameworks, etc.)."""
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'
        ordering = ['order']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skill belonging to a category."""
    category = models.ForeignKey(
        SkillCategory, on_delete=models.CASCADE, related_name='skills'
    )
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        default=75,
        help_text='Proficiency percentage (0-100)'
    )

    class Meta:
        ordering = ['-proficiency', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Experience(models.Model):
    """Work experience entries."""
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default='Current')
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"


class ExperienceBullet(models.Model):
    """Bullet points for an experience entry."""
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name='bullets'
    )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    skills_used = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title or self.content[:50]}"


class Project(models.Model):
    """Portfolio projects."""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=500)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectBullet(models.Model):
    """Bullet points for a project."""
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='bullets'
    )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title or self.content[:50]}"


class Education(models.Model):
    """Education entries."""
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    field_of_study = models.CharField(max_length=300, blank=True)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Leadership(models.Model):
    """Leadership & volunteering entries."""
    organization = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.organization}"


class LeadershipBullet(models.Model):
    """Bullet points for leadership."""
    leadership = models.ForeignKey(
        Leadership, on_delete=models.CASCADE, related_name='bullets'
    )
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title or self.content[:50]}"


class Award(models.Model):
    """Honors and awards."""
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Contact form submissions."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
