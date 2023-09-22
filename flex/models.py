"""Flexible page"""
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

from base.blocks import TitleAndTextBlock, RichTextBlock, CardBlock


class FlexiblePage(Page):
    """Flexible page model"""

    template = "flex/flexible_page.html"

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ("title_and_text", TitleAndTextBlock()),
        ("full_richtext", RichTextBlock()),
        ("cards", CardBlock()),
    ], null=True, blank=True,
        use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

    class Meta:  # noqa
        verbose_name = "Flex_Page"
        verbose_name_plural = "Flex Pages"
