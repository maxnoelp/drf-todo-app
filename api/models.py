from django.db import models
from filer.fields.image import FilerImageField
from filer.models import Image
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(_("Skill"), max_length=100)
    bs_icon = models.CharField(
        _("Bootstrap Icon"),
        max_length=100,
        help_text="Bootstrap icon name",
        blank=True,
    )
    image = FilerImageField(
        related_name=_("Image"), on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")


class Projects(models.Model):
    title = models.CharField(max_length=100)
    teaser = RichTextField(blank=True)
    coding_language = models.CharField(max_length=100)
    coding_lang_icon = models.CharField(max_length=100, blank=True)
    description = RichTextField()
    images = models.ManyToManyField(Image, blank=True, related_name=_("Projektbilder"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Projekt")
        verbose_name_plural = _("Projekte")
