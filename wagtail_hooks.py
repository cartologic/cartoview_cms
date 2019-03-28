from wagtail.wagtailcore import hooks
from django.shortcuts import redirect


@hooks.register('before_serve_document')
def serve_document(document, request):
    # eg. use document.file_extension, document.url, document.filename
    if document.file_extension == 'pdf':
        return redirect(document.file.url)
    # no return means the normal page serve will operate
