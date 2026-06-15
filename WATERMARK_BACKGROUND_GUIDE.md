# AgriTech - Watermark & Background Video Features

## Overview
This feature replaces the basic watermark system with a comprehensive admin-controlled upload system for:
- **Watermark Images/Videos**: Configurable watermarks with positioning and opacity
- **Background Video**: Full-screen background video support
- **Background Image**: Enhanced background image support with fallback

---

## Features

### 1. **Watermark Management**
- Upload watermark as image (PNG recommended for transparency)
- Upload watermark as video (MP4 or WebM)
- Choose watermark position (9 positions available):
  - Top Left, Top Center, Top Right
  - Middle Left, Center, Middle Right
  - Bottom Left, Bottom Center, Bottom Right
- Adjust watermark opacity (0.0 to 1.0)
- Enable/disable watermark display

### 2. **Background Settings**
- Upload background image (recommended: 1920x1080px)
- Upload background video (MP4 or WebM)
- Enable/disable background video
- Video takes priority over image when both exist

### 3. **Responsive Design**
- Watermark automatically adapts on mobile devices
- Watermark repositioned to bottom-left on mobile
- Reduced watermark size and opacity on smaller screens

---

## Setup Instructions

### Step 1: Run Database Migration
```bash
# Activate virtual environment
(venv) $ python manage.py migrate core
```

### Step 2: Initialize Site Settings
```bash
# Activate virtual environment
(venv) $ python manage.py init_site_settings
```

### Step 3: Access Django Admin
1. Go to: `https://yourdomain.com/admin/`
2. Login with superuser credentials
3. Navigate to **Core** → **Site Settings**

---

## How to Use the Admin Interface

### Adding/Editing Settings

1. **Background Image**
   - Click "Choose File" and upload an image
   - Recommended size: 1920x1080px
   - Formats: JPG, PNG, WebP

2. **Background Video**
   - Click "Choose File" and upload a video
   - Supported formats: MP4, WebM
   - Check "Enable background video" to display
   - The video will be played on loop with no sound

3. **Watermark Image**
   - Upload a watermark image (PNG recommended for transparency)
   - Recommended size: 200x200px or smaller
   - Supports: PNG, JPG, GIF, WebP

4. **Watermark Video**
   - Upload a short video clip (MP4 or WebM)
   - Will play on loop with no sound
   - Takes priority if both image and video are uploaded

5. **Watermark Position**
   - Select from 9 positions using the dropdown
   - Default: Bottom Right

6. **Watermark Opacity**
   - Set transparency level (0.0 = invisible, 1.0 = fully opaque)
   - Default: 0.8 (80% visible)

7. **Enable Watermark**
   - Check this box to display the watermark on all pages

8. **Enable Background Video**
   - Check this box to display the background video
   - Video will show instead of static image

---

## Template Integration

The features are automatically integrated into the website through:

### Files Modified:
- `templates/base.html` - Main template with background video and watermark includes
- `static/css/site-settings.css` - CSS for positioning and styling
- `templates/includes/watermark.html` - Watermark display component
- `templates/includes/background-video.html` - Background video component

### Automatic Display:
- Settings are automatically fetched and displayed on all pages
- No code modifications needed in other templates
- Uses the context processor at `core/context_processors.py`

---

## CSS Classes Reference

### Position Classes
```css
.watermark.top-left
.watermark.top-center
.watermark.top-right
.watermark.middle-left
.watermark.center
.watermark.middle-right
.watermark.bottom-left
.watermark.bottom-center
.watermark.bottom-right
```

### Background Video Classes
```css
.bg-video-container        /* Video wrapper */
.bg-video-overlay          /* Semi-transparent overlay */
```

---

## Media Upload Paths

All uploaded files are stored in the media directory:

```
media/
├── backgrounds/
│   ├── background-image.jpg
│   └── background-video.mp4
└── watermarks/
    ├── watermark-image.png
    └── watermark-video.webm
```

---

## File Specifications

### Watermark Image
- **Format**: PNG (recommended), JPG, GIF, WebP
- **Size**: 200x200px or smaller
- **Transparency**: Supported (PNG)
- **Max File Size**: 5MB

### Watermark Video
- **Format**: MP4, WebM
- **Resolution**: 1280x720 or smaller recommended
- **Duration**: Short loops (5-10 seconds)
- **Max File Size**: 10MB

### Background Image
- **Format**: JPG, PNG, WebP
- **Size**: 1920x1080px (Full HD recommended)
- **Aspect Ratio**: 16:9
- **Max File Size**: 5MB

### Background Video
- **Format**: MP4 (recommended), WebM
- **Resolution**: 1920x1080 (Full HD)
- **Duration**: Continuous loop (10-30 seconds)
- **Max File Size**: 50MB
- **Codec**: H.264 (MP4), VP8/VP9 (WebM)

---

## Browser Compatibility

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| Background Image | ✅ | ✅ | ✅ | ✅ |
| Background Video | ✅ | ✅ | ✅ | ✅ |
| Watermark Image | ✅ | ✅ | ✅ | ✅ |
| Watermark Video | ✅ | ✅ | ✅ | ✅ |

---

## Troubleshooting

### Watermark Not Showing
- [ ] Check if "Enable watermark" is checked in admin
- [ ] Verify watermark file is uploaded
- [ ] Check browser console for errors
- [ ] Clear browser cache (Ctrl+Shift+Delete)

### Background Video Not Playing
- [ ] Check if "Enable background video" is checked
- [ ] Verify video file format is MP4 or WebM
- [ ] Check video file size (should be under 50MB)
- [ ] Try a different browser to test

### Settings Not Visible on Frontend
- [ ] Run `python manage.py init_site_settings` to create initial settings
- [ ] Check if SiteSettings object exists in database
- [ ] Verify context processor is in TEMPLATES settings
- [ ] Clear Django cache: `python manage.py clear_cache`

### Admin Page Slow When Uploading
- [ ] Compress video/images before uploading
- [ ] Use appropriate file sizes (see File Specifications)
- [ ] Upload in stages if file size is large

---

## API Reference

### Model: SiteSettings

```python
class SiteSettings(models.Model):
    # Background Fields
    background_image: ImageField
    background_video: FileField
    enable_background_video: BooleanField
    
    # Watermark Fields
    watermark_image: ImageField
    watermark_video: FileField
    watermark_position: CharField (choices: 9 positions)
    watermark_opacity: DecimalField (0.0 - 1.0)
    enable_watermark: BooleanField
```

### Template Context
```python
# In templates, access via:
{{ site_settings.background_image.url }}
{{ site_settings.background_video.url }}
{{ site_settings.watermark_image.url }}
{{ site_settings.watermark_video.url }}
{{ site_settings.watermark_position }}
{{ site_settings.watermark_opacity }}
{{ site_settings.enable_watermark }}
{{ site_settings.enable_background_video }}
```

### Management Command
```bash
# Initialize SiteSettings
python manage.py init_site_settings
```

---

## Advanced Customization

### Changing Default Watermark Position
Edit `core/admin.py` and modify the `SiteSettingsAdmin` class:

```python
# In fieldsets, change default position
watermark_position = models.CharField(
    default='bottom-left',  # Change this value
    ...
)
```

### Customizing CSS
Edit `static/css/site-settings.css` to modify:
- Watermark sizes
- Position offsets
- Opacity transitions
- Video overlay color

### Custom Watermark Animation
Add CSS animations in `static/css/site-settings.css`:

```css
@keyframes watermark-fade {
    0% { opacity: 0.5; }
    100% { opacity: 0.8; }
}

.watermark {
    animation: watermark-fade 2s infinite;
}
```

---

## Performance Considerations

1. **Image Optimization**
   - Compress watermark images to < 100KB
   - Use PNG for transparency, JPG for photos
   - Consider WebP format for smaller file sizes

2. **Video Optimization**
   - Keep video resolution at 1280x720 or lower
   - Use hardware-accelerated codec (H.264)
   - Compress to reasonable bitrate (2-5 Mbps)

3. **Caching**
   - Static files are cached by browser
   - Settings are cached in Django
   - Consider using CDN for media files

---

## Security Considerations

1. **File Upload Validation**
   - Only image and video formats are accepted
   - File size limits are enforced
   - Malicious files are prevented

2. **Admin Access**
   - Only superusers can modify settings
   - Django permission system applies
   - Use strong admin passwords

3. **Media Security**
   - Media files served through Django
   - Configure proper access controls
   - Consider serving from CDN in production

---

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Django documentation
3. Check browser console for errors
4. Contact support with:
   - Error messages
   - File sizes and formats
   - Browser information
   - Django version

---

## Version History

- **v1.0** (2026-06-15) - Initial release
  - Watermark image/video support
  - Background video support
  - Admin interface
  - Management command for initialization
