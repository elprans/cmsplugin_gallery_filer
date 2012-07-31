from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django import forms
from django.forms.models import ModelForm
from cmsplugin_gallery.models import GalleryPlugin, Image
from filer.models import Folder
from filer.models import Image as FilerImage


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" style="height: 100px;" /></a><br /> %s ' % \
                (unicode(image_url), unicode(image_url), unicode(file_name), _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class GalleryForm(ModelForm):
    filerfolder = forms.ModelChoiceField(queryset=Folder.objects.all(),
                                         required=False,
                                         help_text=_("If you choose a "
                                                     "filer folder, all "
                                                     "contained images "
                                                     "will be "
                                                     "automatically added"
                                                     "to the gallery"))

    class Meta:
        model = GalleryPlugin
        exclude = ('page', 'position', 'placeholder', 'language',
                   'plugin_type')

    def clean_filerfolder(self):
        if self.data['filerfolder']:
            images = FilerImage.objects.filter(folder=self.data['filerfolder'])
            for image in images:
                img = Image()
                img.gallery = self.instance
                img.src = image
                img.title = image.name
                img.alt = image.original_filename
                img.save()
