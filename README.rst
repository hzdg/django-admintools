Installation
==============

1. `pip install -e git+git@github.com:hzdg/django-admintools.git#egg=django-admintools`


Included Tools
==============

ExportAsCsv
-----------

In admin.py::

    from admintools.actions import ExportAsCsv

    class MyAdmin(models.ModelAdmin):
        actions = [ExportAsCsv("Export selected emails as CSV file",
                               exclude=['id'])]

