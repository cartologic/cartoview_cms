from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from coderedcms.forms import CoderedFormField
from coderedcms.models import CoderedFormPage, CoderedEmail


class FormField(CoderedFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ['sort_order']

    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(CoderedFormPage):
    """
    A page with a html <form>.
    """
    show_in_menus_default = True
    template = 'cartoview_cms/forms/form_page.html'
    landing_page_template = 'cartoview_cms/forms/form_page_landing.html'
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    body_content_panels = CoderedFormPage.body_content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
    ]

    class Meta:
        verbose_name = "Form with Email"


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """
    page = ParentalKey('FormPage', related_name='confirmation_emails')
