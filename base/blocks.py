from django.db import models
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text block"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True)
    image = ImageChooserBlock()

    class Meta:
        template = "base/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text Block"


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all features"""

    class Meta:
        template = "base/rich_text_block.html"
        icon = "edit"
        label = "Full Rich Text"


class CardBlock(blocks.StructBlock):
    """Card with image, title, text and CTA"""

    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True, max_length=80)),
            ("text", blocks.TextBlock(required=True)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False, help_text="If button above is selected, it will be used "
                                                                     "first")),
        ])
    )

    class Meta:
        template = "base/card_block.html"
        icon = "edit"
        label = "Cards List"