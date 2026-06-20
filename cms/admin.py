from django.contrib import admin
from .models import (
    Attendance,
    Blog,
    BlogCategory,
    CMSPage,
    Department,
    Designation,
    DynamicSection,
    Employee,
    EmployeeDocument,
    FooterContent,
    HomePageContent,
    MediaAsset,
    MenuItem,
    Report,
    Tag,
    Task,
    TaskAttachment,
    TaskComment,
    WebsiteSettings,
)


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(SingletonAdmin):
    list_display = ('site_name', 'email', 'phone')
    fieldsets = (
        ('Branding', {'fields': ('site_name', 'logo', 'favicon', 'footer_logo')}),
        ('Contact Details', {'fields': ('contact_details', 'email', 'phone', 'address')}),
        ('Social Media Links', {
            'fields': (
                'facebook_url',
                'instagram_url',
                'twitter_url',
                'linkedin_url',
                'youtube_url',
            )
        }),
        ('Copyright', {'fields': ('copyright_text',)}),
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'named_url', 'sort_order', 'is_enabled')
    list_editable = ('sort_order', 'is_enabled')
    list_filter = ('is_enabled', 'parent')
    search_fields = ('title', 'url', 'named_url')


@admin.register(HomePageContent)
class HomePageContentAdmin(SingletonAdmin):
    list_display = ('hero_title', 'primary_cta_text', 'secondary_cta_text', 'is_active')
    fieldsets = (
        ('Hero Banner', {
            'fields': (
                'hero_banner',
                'hero_title',
                'hero_subtitle',
                'primary_cta_text',
                'primary_cta_url',
                'secondary_cta_text',
                'secondary_cta_url',
                'background_image',
                'background_video',
                'is_active',
            )
        }),
        ('Home Page Content', {
            'fields': ('featured_sections', 'testimonials', 'counters', 'body_content')
        }),
    )


@admin.register(FooterContent)
class FooterContentAdmin(SingletonAdmin):
    list_display = ('__str__', 'is_active')
    fieldsets = (
        ('Footer Management', {
            'fields': (
                'about_section',
                'quick_links',
                'contact_information',
                'social_links',
                'copyright_area',
                'footer_image',
                'is_active',
            )
        }),
    )


@admin.register(DynamicSection)
class DynamicSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    list_filter = ('page', 'is_active')
    search_fields = ('title', 'subtitle', 'content')


@admin.register(CMSPage)
class CMSPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_type', 'slug', 'is_published', 'updated_at')
    list_filter = ('page_type', 'is_published')
    search_fields = ('title', 'content', 'seo_title', 'seo_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_at', 'updated_at')
    list_filter = ('status', 'category', 'tags')
    search_fields = ('title', 'excerpt', 'content', 'seo_title', 'seo_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'is_active', 'uploaded_at')
    list_filter = ('media_type', 'is_active')
    search_fields = ('title', 'alt_text', 'description')
    readonly_fields = ('uploaded_at',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'sort_order', 'is_active')
    list_filter = ('department', 'is_active')
    list_editable = ('sort_order', 'is_active')
    search_fields = ('title',)


class EmployeeDocumentInline(admin.TabularInline):
    model = EmployeeDocument
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'full_name', 'department', 'designation', 'status', 'joining_date')
    list_filter = ('department', 'designation', 'status', 'joining_date')
    search_fields = ('employee_code', 'full_name', 'email', 'phone')
    inlines = (EmployeeDocumentInline,)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('status', 'date', 'employee__department')
    search_fields = ('employee__full_name', 'employee__employee_code')
    date_hierarchy = 'date'


class TaskCommentInline(admin.TabularInline):
    model = TaskComment
    extra = 1


class TaskAttachmentInline(admin.TabularInline):
    model = TaskAttachment
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'priority', 'due_date', 'status', 'updated_at')
    list_filter = ('priority', 'status', 'due_date', 'assigned_to__department')
    search_fields = ('title', 'description', 'assigned_to__full_name')
    inlines = (TaskCommentInline, TaskAttachmentInline)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'report_type', 'start_date', 'end_date', 'created_at')
    list_filter = ('report_type', 'start_date', 'end_date')
    search_fields = ('title', 'notes')
    readonly_fields = ('created_at',)
