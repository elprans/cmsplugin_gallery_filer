from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from filer.models import Image as FilerImage

import admin
import models
from forms import GalleryForm


class CMSGalleryPlugin(CMSPluginBase):

    model = models.GalleryPlugin
    inlines = [admin.ImageInline, ]
    name = _('Image gallery')
    render_template = 'cmsplugin_gallery/gallery.html'
    form = GalleryForm

    def render(self, context, instance, placeholder):
        context.update({
                        'images': instance.image_set.all(),
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context

    def save_model(self, request, obj, form, change):
        temp = super(CMSGalleryPlugin, self).save_model(request, obj, form,
                                                        change)
        if form.data['filerfolder']:
            images = FilerImage.objects.filter(folder=form.data['filerfolder'])
            for image in images:
                img = models.Image()
                img.gallery = obj
                img.src = image
                img.title = image.name
                img.alt = image.original_filename
                img.save()

        return temp



plugin_pool.register_plugin(CMSGalleryPlugin)
