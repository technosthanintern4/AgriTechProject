# ⚡ Quick Reference Card - Watermark Feature

## 🚀 Access Admin Panel
```
URL: https://yourdomain.com/admin/
Navigate: Core → Site Settings
```

---

## 📸 Watermark Fields

### Watermark Image
- **Type**: File Upload
- **Format**: PNG (recommended), JPG, GIF, WebP
- **Size**: 200x200px or smaller
- **Tip**: Use PNG for transparency

### Watermark Position
- **Type**: Dropdown (9 options)
- **Default**: Bottom Right
- **Options**: Top Left/Center/Right, Middle Left/Center/Right, Bottom Left/Center/Right

### Watermark Opacity
- **Type**: Decimal (0.0-1.0)
- **Default**: 0.8 (80% visible)
- **Tip**: 0.8 is recommended
- **Range**: 0.0 (invisible) to 1.0 (fully opaque)

### Enable Watermark
- **Type**: Checkbox
- **Check**: ✓ to display watermark
- **Uncheck**: ☐ to hide watermark

---

## 🎬 Background Video Fields

### Background Video
- **Type**: File Upload
- **Format**: MP4 (H.264), WebM
- **Size**: ≤ 50MB recommended
- **Duration**: 10-30 seconds (loops)

### Enable Background Video
- **Type**: Checkbox
- **Check**: ✓ to show video
- **Uncheck**: ☐ to show image instead

---

## 🎯 Watermark Positions (9 Options)

```
┌─────────────────────────┐
│ TL    TC        TR      │
│                         │
│ ML    C         MR      │
│                         │
│ BL    BC        BR ✓    │
└─────────────────────────┘

TL = Top Left
TC = Top Center
TR = Top Right
ML = Middle Left
C  = Center
MR = Middle Right
BL = Bottom Left
BC = Bottom Center
BR = Bottom Right (default)
```

---

## 📊 Opacity Settings

```
0.0 = Invisible (don't use)
0.3 = Very faint
0.5 = 50% visible
0.8 = 80% visible ← RECOMMENDED
1.0 = Fully visible
```

---

## ✅ Quick Setup Steps

1. Go to `/admin/`
2. Click "Site Settings"
3. Upload watermark image
4. Select position (Bottom Right recommended)
5. Set opacity to 0.8
6. Check "Enable watermark"
7. Click SAVE
8. View website - Done! ✅

---

## 🎬 File Requirements

### Watermark Image
```
Format:   PNG, JPG, GIF, WebP
Size:     200x200px or smaller
Max Size: 5MB
Best:     PNG with transparency
```

### Watermark Video
```
Format:   MP4, WebM
Size:     1280x720 or smaller
Duration: 5-10 seconds
Max Size: 10MB
```

### Background Image
```
Format:   JPG, PNG, WebP
Size:     1920x1080px
Aspect:   16:9
Max Size: 5MB
```

### Background Video
```
Format:   MP4, WebM
Size:     1920x1080px
Duration: 10-30 seconds
Max Size: 50MB
```

---

## 🔧 Admin Panel Layout

```
BACKGROUND SETTINGS
├─ Background Image: [Upload]
├─ Background Video: [Upload]
└─ ☐ Enable background video

WATERMARK IMAGE SETTINGS
├─ Watermark Image: [Upload]
├─ Position: [Bottom Right ▼]
├─ Opacity: [0.8]
└─ ☐ Enable watermark

WATERMARK VIDEO SETTINGS
└─ Watermark Video: [Upload]
```

---

## 🐛 Quick Troubleshooting

### Watermark Not Showing?
- [ ] Check "Enable watermark" is ✓ checked
- [ ] Verify watermark image is uploaded
- [ ] Clear browser cache (Ctrl+Shift+Delete)
- [ ] Reload page (Ctrl+R)

### Video Not Playing?
- [ ] Check "Enable background video" is ✓ checked
- [ ] Verify video format is MP4 or WebM
- [ ] Check file size (< 50MB)
- [ ] Try different browser

### Settings Not Saving?
- [ ] Check file size limits
- [ ] Check file formats
- [ ] Verify opacity is 0.0-1.0
- [ ] Try again with smaller files

---

## 🎨 CSS Classes

```
.watermark                  ← Main watermark container
.watermark.bottom-right     ← Position class
.bg-video-container         ← Background video wrapper
.bg-video-overlay           ← Semi-transparent overlay
```

---

## 📱 Responsive Breakpoints

```
Desktop (≥768px)
├─ 200px watermark
├─ Full opacity
└─ All 9 positions

Mobile (<768px)
├─ 80px watermark
├─ 60% opacity
└─ Bottom-left position
```

---

## 🔐 Admin Restrictions

```
✓ Only superusers can access
✓ Cannot delete settings
✓ Cannot create duplicates
✓ Files are validated
✓ File sizes are limited
```

---

## 📞 Commands

```bash
# Initialize settings (if needed)
python manage.py init_site_settings

# Collect static files (production)
python manage.py collectstatic --noinput

# View migrations
python manage.py showmigrations core

# Check migrations applied
python manage.py migrate --plan
```

---

## 📚 Documentation Files

| Need | File |
|------|------|
| Quick start | `SETUP_SUMMARY.md` |
| Admin help | `ADMIN_PANEL_GUIDE.md` |
| Full guide | `WATERMARK_BACKGROUND_GUIDE.md` |
| Tech details | `IMPLEMENTATION_SUMMARY.md` |
| Overview | `FINAL_SUMMARY.md` |

---

## ✨ Features Implemented

```
✅ Watermark images & videos
✅ 9 positioning options
✅ Opacity control
✅ Background videos
✅ Admin upload interface
✅ Enable/disable toggles
✅ Mobile responsive
✅ Browser compatible
✅ Production ready
✅ Fully documented
```

---

## 🎯 Common Tasks

### Change Watermark Position
1. Go to Site Settings
2. Select new position from dropdown
3. Click SAVE

### Adjust Watermark Transparency
1. Go to Site Settings
2. Change opacity value (e.g., 0.5)
3. Click SAVE

### Hide Watermark Temporarily
1. Go to Site Settings
2. Uncheck "Enable watermark"
3. Click SAVE

### Replace Watermark Image
1. Go to Site Settings
2. Click "Clear" on current image
3. Upload new image
4. Click SAVE

---

## 🌐 Browser Support

```
✅ Chrome 60+
✅ Firefox 60+
✅ Safari 12+
✅ Edge 79+
✅ Mobile browsers
```

---

## 💾 Database Info

```
Table: core_sitesettings
Fields: 8 (6 new, 2 existing)
Status: ✅ Applied
Migration: 0003_alter_sitesettings_options_and_more.py
```

---

## 📈 File Size Recommendations

```
Watermark:       < 100KB (PNG recommended)
Background Img:  100-500KB (JPG recommended)
Watermark Video: < 10MB (MP4 recommended)
Background Video: 5-20MB (MP4 recommended)
```

---

## 🎓 Tips & Tricks

💡 Use PNG for transparency
💡 Compress images before upload
💡 Use H.264 codec for videos
💡 Keep watermark size small
💡 Test on multiple devices
💡 Clear cache after changes
💡 0.8 opacity is the sweet spot
💡 Bottom-right is most professional

---

## ⚡ Performance Tips

- Compress files before uploading
- Use PNG for watermarks (smaller than JPG)
- Use MP4 over WebM (better compatibility)
- Keep video resolution at 1080p or lower
- Use CDN for media in production
- Enable browser caching

---

## 🔄 Update Workflow

```
1. Go to /admin/core/sitesettings/
2. Make changes
3. Upload files if needed
4. Click SAVE
5. Reload website to see changes
6. Done! ✅
```

---

## 🎊 Status

✅ **PRODUCTION READY**

All features implemented
All files created
All migrations applied
Documentation complete

---

## 📞 Support

For questions, refer to:
- `README_WATERMARK_FEATURE.md` (overview)
- `ADMIN_PANEL_GUIDE.md` (instructions)
- `WATERMARK_BACKGROUND_GUIDE.md` (complete guide)

---

**Last Updated**: June 15, 2026
**Version**: 1.0
**Status**: ✅ Ready to Use
