# Admin Panel Guide - Watermark & Background Video

## 🎯 Accessing the Settings

### URL
```
https://your-domain.com/admin/core/sitesettings/
```

### Navigation
1. Login to Django Admin (`/admin/`)
2. Look for **CORE** section (left sidebar)
3. Click on **Site Settings**
4. You'll see the single settings entry

---

## 📋 Admin Form Fields

### Section 1: Background Settings

#### Background Image
```
Label: Background Image
Type: File Upload
Required: Yes
Formats: JPG, PNG, WebP, GIF
Recommended Size: 1920x1080px (Full HD)
Max Size: 5MB
Description: Upload a background image. Recommended size: 1920x1080px
Help Text: ✓ Provided
```

**Steps to upload:**
1. Click "Choose File" button
2. Select your image (1920x1080px recommended)
3. Image automatically displays behind website content

#### Background Video
```
Label: Background Video
Type: File Upload
Required: No (Optional)
Formats: MP4, WebM
Recommended Size: 1920x1080 @ 24fps
Max Size: 50MB
Description: Upload a background video (mp4, webm)
Help Text: ✓ Provided
```

**Tips:**
- Compress video to reduce file size
- Keep resolution at 1080p or lower
- Use H.264 codec for MP4
- Video will play on loop, muted

#### Enable background video ⚠️ IMPORTANT
```
Label: Enable background video
Type: Checkbox (✓ or ☐)
Default: ☐ (unchecked)
Description: Enable background video display (if video is uploaded)
```

**What it does:**
- ✓ CHECKED: Background video displays instead of image
- ☐ UNCHECKED: Background image displays instead

---

### Section 2: Watermark Image Settings

#### Watermark Image
```
Label: Watermark Image
Type: File Upload
Required: No (Optional)
Formats: PNG (recommended), JPG, GIF, WebP
Recommended Size: 200x200px
Max Size: 5MB
Description: Upload an image as watermark
Help Text: ✓ Provided - PNG recommended for transparency
```

**Best Practices:**
- Use PNG for transparency
- Size: 200x200px or smaller
- Keep file size under 100KB
- Use company logo or branding

**Transparency:**
- PNG with transparent background recommended
- Shows through to website behind it
- Can be any shape (not just square)

#### Watermark Position
```
Label: Watermark Position
Type: Dropdown (Select one)
Default: bottom-right
Options:
  ├─ Top Left (top-left)
  ├─ Top Center (top-center)
  ├─ Top Right (top-right)
  ├─ Middle Left (middle-left)
  ├─ Center (center)
  ├─ Middle Right (middle-right)
  ├─ Bottom Left (bottom-left)
  ├─ Bottom Center (bottom-center)
  └─ Bottom Right (bottom-right) ← Default
Description: Position of the watermark on the page
```

**Visual Reference:**
```
┌──────────────────────────────┐
│ TL    TC           TR        │
│                              │
│ ML    C            MR        │
│                              │
│ BL    BC           BR ✓      │
└──────────────────────────────┘
```

#### Watermark Opacity
```
Label: Watermark Opacity
Type: Decimal Input
Range: 0.0 to 1.0
Default: 0.8 (80% visible)
Description: Opacity of watermark (0.0 to 1.0)
```

**Understanding Opacity:**
- **0.0** = Invisible (don't use)
- **0.3** = Very faint/subtle
- **0.5** = 50% transparent, 50% visible
- **0.8** = 80% visible (DEFAULT - recommended)
- **1.0** = Fully opaque, no transparency

**Recommended Values:**
- Logo watermark: 0.8-0.9
- Large watermark: 0.5-0.7
- Subtle branding: 0.3-0.5

#### Enable Watermark
```
Label: Enable watermark
Type: Checkbox (✓ or ☐)
Default: ☐ (unchecked)
Description: Enable watermark display on the website
```

**What it does:**
- ✓ CHECKED: Watermark displays on all pages
- ☐ UNCHECKED: Watermark is hidden

---

### Section 3: Watermark Video Settings

#### Watermark Video
```
Label: Watermark Video
Type: File Upload
Required: No (Optional)
Formats: MP4, WebM
Recommended Size: 1280x720px
Max Size: 10MB
Duration: 5-10 seconds (loops)
Description: Upload a video as watermark
Help Text: ✓ Provided
```

**Important:**
- If both image and video are uploaded, **VIDEO takes priority**
- Video will play on loop, muted
- Keep video short (5-10 seconds)
- Compress video files before uploading

---

## ⚙️ Complete Admin Workflow

### Step 1: Navigate to Site Settings
```
1. Go to: https://yourdomain.com/admin/
2. Login with admin credentials
3. Find "CORE" section on left sidebar
4. Click "Site Settings"
```

### Step 2: Upload Background Image
```
1. Scroll to "Background Settings" section
2. Click "Choose File" next to "Background Image"
3. Select a 1920x1080px image
4. Image preview appears
5. (Optional) Upload background video
6. (Optional) Check "Enable background video" if you want video
```

### Step 3: Configure Watermark
```
1. Scroll to "Watermark Image Settings"
2. Click "Choose File" next to "Watermark Image"
3. Select PNG with transparent background (200x200px)
4. Image preview appears
```

### Step 4: Set Watermark Position
```
1. Click dropdown next to "Watermark Position"
2. Choose from 9 positions (e.g., "Bottom Right")
3. Selected position shows in dropdown
```

### Step 5: Adjust Watermark Opacity
```
1. Click field next to "Watermark Opacity"
2. Clear current value
3. Type new value (e.g., 0.85)
4. Value must be between 0.0 and 1.0
```

### Step 6: Enable Watermark Display
```
1. Scroll down in "Watermark Image Settings"
2. Check checkbox "Enable watermark"
3. Checkbox shows ✓
```

### Step 7: Save Changes
```
1. Click green "SAVE" button at bottom
2. Page reloads with success message
3. "Site Settings changed successfully"
```

### Step 8: Verify on Website
```
1. Open website in new tab
2. Reload page (Ctrl+R)
3. Watermark should appear in chosen position
4. Background should display
5. Check different pages to confirm
```

---

## 🎬 Field Interaction Matrix

### When Watermark Video is Uploaded
```
Watermark Image + Watermark Video
      ↓
VIDEO TAKES PRIORITY
      ↓
Watermark Video displays, Image is ignored
```

### When Background Video is Enabled
```
Enable Background Video = ✓
           ↓
Background Video displays
           ↓
Background Image is ignored
           ↓
Video plays on loop, muted
```

### Watermark Visibility Matrix
```
Enable Watermark = ☐ (unchecked)
        ↓
Watermark hidden (not visible)

Enable Watermark = ✓ (checked)
        ↓
Watermark visible using:
├─ Video (if uploaded, priority)
├─ Image (if no video)
├─ Position (9 options)
└─ Opacity (0.0-1.0 control)
```

---

## 📊 Quick Reference Table

| Setting | Type | Default | Required | Notes |
|---------|------|---------|----------|-------|
| Background Image | Image Upload | - | Yes | 1920x1080px recommended |
| Background Video | Video Upload | - | No | MP4/WebM, ≤50MB |
| Enable BG Video | Checkbox | ☐ | No | Video takes priority if ✓ |
| Watermark Image | Image Upload | - | No | PNG recommended, 200x200px |
| Watermark Video | Video Upload | - | No | MP4/WebM, ≤10MB |
| Watermark Position | Dropdown | Bottom Right | No | 9 position options |
| Watermark Opacity | Decimal | 0.8 | No | Range: 0.0-1.0 |
| Enable Watermark | Checkbox | ☐ | No | Check to display watermark |

---

## 🔄 Common Admin Tasks

### Task 1: Change Watermark Position
```
1. Navigate to Site Settings
2. Find "Watermark Position" dropdown
3. Click dropdown and select new position
4. Click SAVE
```

### Task 2: Make Watermark Less Visible
```
1. Navigate to Site Settings
2. Find "Watermark Opacity" field
3. Change value from 0.8 to 0.5 (more transparent)
4. Click SAVE
```

### Task 3: Switch to Video Background
```
1. Navigate to Site Settings
2. Upload video to "Background Video" field
3. Check "Enable background video" ✓
4. Click SAVE
```

### Task 4: Disable Watermark Temporarily
```
1. Navigate to Site Settings
2. Uncheck "Enable watermark" ☐
3. Click SAVE
4. Watermark disappears from website
```

### Task 5: Replace Watermark Image
```
1. Navigate to Site Settings
2. Click on "Watermark Image" field
3. Click "Clear" or "Change" button
4. Upload new image
5. Click SAVE
```

---

## ⚠️ Important Notes

### File Sizes
- **Image uploads**: 5MB max
- **Video uploads**: 50MB max (background), 10MB max (watermark)
- Compress files before uploading to avoid timeout

### Supported Formats
```
Images:  JPG, PNG, GIF, WebP
Videos:  MP4 (H.264), WebM (VP8/VP9)
```

### Browser Support
```
All modern browsers supported:
├─ Chrome 60+
├─ Firefox 60+
├─ Safari 12+
├─ Edge 79+
└─ Mobile browsers (iOS, Android)
```

### Performance Tips
1. Compress watermark to <100KB
2. Use 1080p or lower video resolution
3. Keep video duration short (5-10 seconds)
4. Use WebM for smaller video files
5. Consider CDN for large files

---

## 🐛 Troubleshooting

### Watermark Not Showing
```
Check 1: ✓ "Enable watermark" is checked?
Check 2: ✓ Watermark image/video is uploaded?
Check 3: ✓ Opacity is not 0?
Action: Clear cache (Ctrl+Shift+Delete) and reload
```

### Video Not Playing
```
Check 1: ✓ "Enable background video" is checked?
Check 2: ✓ Video file is MP4 or WebM?
Check 3: ✓ Video file size < 50MB?
Action: Try different browser or video format
```

### Settings Not Saving
```
Check 1: ✓ File sizes within limits?
Check 2: ✓ File formats correct?
Check 3: ✓ Opacity between 0.0-1.0?
Action: Reduce file size and try again
```

---

## 📱 Mobile Admin Access

Django admin is responsive and works on mobile:

```
Mobile Admin Access:
1. Open: https://yourdomain.com/admin/
2. Login with admin credentials
3. Settings form adjusts to mobile screen
4. Upload buttons work on mobile
5. All fields accessible on mobile
```

---

## 🔐 Admin Restrictions

```
Only Superusers Can:
├─ Access Site Settings
├─ Upload files
├─ Change settings
└─ Save changes

Users Cannot:
├─ Delete Site Settings
├─ Create duplicate settings
└─ Access without superuser permission
```

---

## 📞 Support Information

### If Settings Don't Appear:
1. Verify SiteSettings table has one record
2. Run: `python manage.py init_site_settings`
3. Check Django admin access permissions

### If Files Won't Upload:
1. Check file format (JPG, PNG, MP4, WebM)
2. Check file size (images <5MB, videos <50MB)
3. Check server storage space
4. Verify media folder has write permissions

### If Watermark Looks Strange:
1. Check opacity value (should be 0.0-1.0)
2. Verify image format (PNG for transparency)
3. Check image size (200x200px recommended)
4. Clear browser cache and reload

---

**Version**: 1.0
**Last Updated**: June 15, 2026
**Status**: Ready for Admin Use ✅
