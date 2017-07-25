from django import forms

from django.forms import TextInput, SplitDateTimeWidget


class NumberInput(TextInput):
    """
    HTML5 Number input
    Left for backwards compatibility
    """
    input_type = 'number'


class AdminDateWidget(forms.DateInput):

    @property
    def media(self):
        js = ["calendar.js", "admin/DateTimeShortcuts.js"]
        return forms.Media(js=["admin/js/%s" % path for path in js])

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'form-control datepicker',
                       'size': '10', 'type': 'date'}

        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminDateWidget, self).__init__(attrs=final_attrs, format=format)


class AdminTimeWidget(forms.TimeInput):

    @property
    def media(self):
        js = ["calendar.js", "admin/DateTimeShortcuts.js"]
        return forms.Media(js=["admin/js/%s" % path for path in js])

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'form-control timepicker',
                       'size': '8', 'type': 'time'}

        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminTimeWidget, self).__init__(attrs=final_attrs, format=format)


class LteAdminSplitDateTime (forms.SplitDateTimeWidget):

    #template_name = 'admin/widgets/split_datetime.html'

    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimeWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

