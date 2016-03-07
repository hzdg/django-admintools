import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str


class ExportAsCsv(object):
    """
    An admin action for exporting CSV files.
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    Based on http://djangosnippets.org/snippets/1697/
    """

    __name__ = 'ExportAsCsv'

    def __init__(self, description="Export selected objects as CSV file",
                 fields=None, exclude=None, header=True):
        self.description = description
        self.short_description = description
        self.fields = fields or []
        self.exclude = exclude or []
        self.header = header

    def __call__(self, modeladmin, request, queryset):
        opts = modeladmin.model._meta

        if len(self.fields) > 0:
            field_names = [field.name for field in opts.fields
                           if field.name not in self.exclude and field.name in self.fields]
        else:
            field_names = [field.name for field in opts.fields
                           if field.name not in self.exclude]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % \
                                          unicode(opts).replace('.', '_')

        writer = csv.writer(response)
        if self.header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([self._get_value(obj, field)
                            for field in opts.fields if field.name in field_names])
        return response

    def _get_value(self, obj, field):
        if field.choices:
            f = getattr(obj, 'get_{0}_display'.format(field.name))
            value = f()
        else:
            value = smart_str(getattr(obj, field.name))
        return value


# For backwards compatibility
def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    return ExportAsCsv(description, fields, exclude, header)
