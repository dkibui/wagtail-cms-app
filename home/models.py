from django.db import models
from django.db.models import SET_NULL
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import BaseStreamBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from base.blocks2 import BaseStreamBlock


class HomePage(Page):
    """Home page model """

    templates = "home/home_page.html"
    # max_count = 1

    banner_title = models.CharField(max_length=255, blank=True, null=True)
    banner_subtitle = RichTextField()
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel('banner_image'),
    ]

    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     FieldPanel('banner_image'),
    # ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
