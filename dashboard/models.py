from django.db import models

class GalleryImage(models.Model):
    CATEGORIES = [
        ("shop", "Our shop"),
        ("phones", "Phones"),
        ("repairs", "Repairs"),
        ("accessories", "Accessories"),
        ("other", "Other"),
    ]
    title = models.CharField(max_length=100, blank=True, help_text="Short caption (optional)")
    image = models.ImageField(upload_to="gallery/")
    category = models.CharField(max_length=20, choices=CATEGORIES, default="phones")
    is_visible = models.BooleanField(default=True, help_text="Untick to hide without deleting")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title or f"Image {self.pk}"