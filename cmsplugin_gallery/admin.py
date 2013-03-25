from cms.utils import cms_static_url
from inline_ordering.admin import OrderableStackedInline, INLINE_ORDERING_JS
from cmsplugin_gallery import forms, models


class ImageInline(OrderableStackedInline):

    model = models.Image

    class Media:
        from django.conf import settings

        extend = False

        js = [cms_static_url(path) for path in (
            'js/libs/jquery.ui.core.js',
            'js/libs/jquery.ui.sortable.js'
        )] + [
            INLINE_ORDERING_JS,
            settings.ADMIN_MEDIA_PREFIX + 'js/inlines.min.js'
        ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'src':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline, self).\
            formfield_for_dbfield(db_field, **kwargs)
