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
            field_names = [field.name for field in opts.fields \
                    if field.name not in self.exclude and field.name in self.fields]
        else:
            field_names = [field.name for field in opts.fields \
                    if field.name not in self.exclude]

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % \
                                            unicode(opts).replace('.', '_')

        writer = csv.writer(response)
        if self.header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([smart_str(
                                getattr(obj, field)) for field in field_names])
        return response


# For backwards compatibility
def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    return ExportAsCsv(description, fields, exclude, header)
