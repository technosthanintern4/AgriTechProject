from django.db import models
from django.conf import settings
from django.utils.text import slugify


class ActiveOrderedModel(models.Model):
    title = models.CharField(max_length=200)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title


class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=150, default='AgroSthan')
    logo = models.ImageField(upload_to='cms/site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='cms/site/', blank=True, null=True)
    footer_logo = models.ImageField(upload_to='cms/site/', blank=True, null=True)
    contact_details = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    copyright_text = models.CharField(
        max_length=255,
        default='© 2026 AgroSthan. All Rights Reserved.'
    )

    class Meta:
        verbose_name = 'Website Settings'
        verbose_name_plural = 'Website Settings'

    def __str__(self):
        return self.site_name


class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=120, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True
    )
    sort_order = models.PositiveIntegerField(default=0)
    open_in_new_tab = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order', 'title']
        verbose_name = 'Navbar Menu Item'
        verbose_name_plural = 'Navbar Menu Items'

    def __str__(self):
        return self.title


class HomePageContent(models.Model):
    hero_banner = models.ImageField(upload_to='cms/home/', blank=True, null=True)
    hero_title = models.CharField(max_length=200, default='AgroSthan')
    hero_subtitle = models.CharField(
        max_length=255,
        default='Plants • Plant Doctors • Gardeners • Home Delivery'
    )
    primary_cta_text = models.CharField(max_length=80, default='Shop Plants')
    primary_cta_url = models.CharField(max_length=255, default='/products/')
    secondary_cta_text = models.CharField(max_length=80, default='Book Plant Doctor')
    secondary_cta_url = models.CharField(max_length=255, default='/doctors/')
    background_image = models.ImageField(upload_to='cms/home/backgrounds/', blank=True, null=True)
    background_video = models.FileField(upload_to='cms/home/videos/', blank=True, null=True)
    featured_sections = models.TextField(blank=True)
    testimonials = models.TextField(blank=True)
    counters = models.TextField(blank=True)
    body_content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Home Page Content'
        verbose_name_plural = 'Home Page Content'

    def __str__(self):
        return self.hero_title


class FooterContent(models.Model):
    about_section = models.TextField(blank=True)
    quick_links = models.TextField(blank=True, help_text='One link per line: Label|URL')
    contact_information = models.TextField(blank=True)
    social_links = models.TextField(blank=True, help_text='One link per line: Platform|URL')
    copyright_area = models.CharField(
        max_length=255,
        default='© 2026 AgroSthan. All Rights Reserved.'
    )
    footer_image = models.ImageField(upload_to='cms/footer/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Footer Content'
        verbose_name_plural = 'Footer Content'

    def __str__(self):
        return 'Footer Content'


class DynamicSection(ActiveOrderedModel):
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
        ('contact', 'Contact Page'),
        ('privacy', 'Privacy Policy'),
        ('terms', 'Terms & Conditions'),
        ('faq', 'FAQ'),
    ]

    page = models.CharField(max_length=30, choices=PAGE_CHOICES)
    subtitle = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='cms/sections/', blank=True, null=True)
    video = models.FileField(upload_to='cms/sections/videos/', blank=True, null=True)


class CMSPage(models.Model):
    PAGE_TYPE_CHOICES = [
        ('about', 'About Page'),
        ('contact', 'Contact Page'),
        ('privacy', 'Privacy Policy'),
        ('terms', 'Terms & Conditions'),
        ('faq', 'FAQ'),
        ('custom', 'Custom Page'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    page_type = models.CharField(max_length=30, choices=PAGE_TYPE_CHOICES, default='custom')
    content = models.TextField(blank=True)
    banner = models.ImageField(upload_to='cms/pages/', blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogCategory(ActiveOrderedModel):
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    featured_image = models.ImageField(upload_to='cms/blog/', blank=True, null=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MediaAsset(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
        ('banner', 'Banner'),
        ('gallery', 'Gallery'),
    ]

    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='cms/media/')
    alt_text = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class Department(ActiveOrderedModel):
    description = models.TextField(blank=True)


class Designation(ActiveOrderedModel):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)


class Employee(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
        ('terminated', 'Terminated'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='employee_profile',
        blank=True,
        null=True
    )
    employee_code = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    joining_date = models.DateField(blank=True, null=True)
    salary_information = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    profile_photo = models.ImageField(upload_to='cms/employees/photos/', blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} ({self.employee_code})"


class EmployeeDocument(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=150)
    document = models.FileField(upload_to='cms/employees/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['employee', 'title']

    def __str__(self):
        return f"{self.employee} - {self.title}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('half_day', 'Half Day'),
        ('leave', 'Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date', 'employee']
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} - {self.date}"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('review', 'Review'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_tasks',
        blank=True,
        null=True
    )
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='tasks', blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment on {self.task}"


class TaskAttachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='cms/tasks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['task', 'title']

    def __str__(self):
        return f"{self.task} - {self.title}"


class Report(models.Model):
    REPORT_TYPES = [
        ('orders', 'Orders Report'),
        ('products', 'Product Report'),
        ('services', 'Service Report'),
        ('consultations', 'Consultation Report'),
        ('employees', 'Employee Report'),
        ('attendance', 'Attendance Report'),
        ('tasks', 'Task Report'),
    ]

    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=30, choices=REPORT_TYPES)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    attachment = models.FileField(upload_to='cms/reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
