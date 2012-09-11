Installation
==============

1. `pip install -e git+git://github.com/hzdg/django-admintools.git#egg=django-admintools`


Included Tools
==============

export_as_csv_action
--------------------

In admin.py::

    from admintools import export_as_csv_action

    class MyAdmin(models.ModelAdmin):
        actions = [export_as_csv_action("Export selected emails as CSV file",
        exclude=['id'])]

