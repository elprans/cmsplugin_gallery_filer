=======================
cmsplugin_gallery_filer
=======================

cmsplugin_gallery_filer adds simple gallery plugin to your djangoCMS
installation

Features:

- Drag&Drop reordering of photos in the plugin admin
- Unlimited, auto-discovered custom templates - you can change template
  of given gallery at anytime, use javascript galleries etc.
- Uses django-filer for storing images.

This plugin is a fork of http://github.com/centralniak/cmsplugin_gallery to
add filer support. To get a django-filer_ free version go to the original
plugin by Piotr Kilczuk.

Contributions and comments are welcome using Github at:
http://github.com/shagi/cmsplugin_gallery_filer

Please not that cmsplugin_gallery_filer requires:

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/
- django-filer http://pypi.python.org/pypi/django-filer/

Installation
============

#. `pip install cmsplugin_gallery_filer`
#. Add `'cmsplugin_gallery'` to `INSTALLED_APPS` (if necessary)
#. Run `syncdb` or `migrate cmsplugin_gallery` if using South

Configuration
=============

#. Create directory for storing media files - files will be uploaded to
   MEDIA_ROOT + 'cmsplugin_gallery/images'. Make sure it is writable especially
   when running in embedded mode on production server.

#. Very simple template is included with the project. To make it work 100%,
   install jQueryTOOLS for overlay support using your favorite method
   http://flowplayer.org/tools/download/index.html

Usage
=====

The easiest approach is to use a nice feature of cmsplugin_gallery -
the template autodiscovery. In order to take advantage of it, add your custom
templates in the cmsplugin_gallery subdirectory of any of template dirs scanned
by Django.

If you don't want to use the autodiscovery, you can hardcode available templates
in settings.py using following setting:

::

    CMSPLUGIN_GALLERY_TEMPLATES = (
        ('app/template.html', 'Template #1', ),
        ('app/other_template.html', 'Template #2', ),
    )

Embed as a typical plugin.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/shagi/cmsplugin_gallery_filer

:date: 2012/08/01

.. _django-filer: https://github.com/stefanfoulis/django-filer/
