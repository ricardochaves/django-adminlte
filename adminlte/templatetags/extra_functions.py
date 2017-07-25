from django import template
from django.utils.safestring import mark_safe
from adminlte.config import get_config

from adminlte.widgets import LteAdminSplitDateTime


register = template.Library()


@register.filter(name='lte_conf')
def lte_conf(name):
    value = get_config(name)
    return mark_safe(value) if isinstance(value, str) else value


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__


@register.filter(is_safe=True)
def add_class(value, arg):

    if field_type(value) == "AdminSplitDateTime":
        value.field.widget = LteAdminSplitDateTime()
        return value

    if field_type(value) == "AdminDateWidget":
        return value.as_widget(attrs={"class": arg, "type": "date"})

    return value.as_widget(attrs={"class": arg})


@register.filter(name='chagenthfortd')
def chagenthfortd(item):
    val_st = item.replace('<th', '<td')
    val_st = val_st.replace('th>', 'td>')
    return mark_safe(val_st)


@register.filter(name='selectaction')
def selectaction(item):
    if field_type(item) == "Select":
        return item.as_widget(attrs={"class": "form-control"})
    return item


@register.filter(name='userimage')
def userimage(user):
#    if hasattr(user, "lteprofile"):
#        html = '<img src="{}" class="user-image" alt="User Image">'
#        return mark_safe(html.format(user.lteprofile.avatar.url))
#    else:
#        return mark_safe(
#            '<img src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" alt="">')
    return mark_safe( \
        '<img src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" alt="">')


@register.filter(name='get_erro_field')
def get_erro_field(value):
    if value.errors:
        html = '<p class="help-block">{}</p>'
        return mark_safe(html.format(str(value.errors[0])))
    else:
        return ''


@register.filter(name='userpost')
def userpost(user):
    if hasattr(user, "lteprofile"):
        return user.lteprofile.post
    else:
        return ''


@register.filter(name='convert_to_class_tag_message')
def convert_to_class_tag_message(tags):

    classes_convertidas = tags \
        .replace('success', 'text-green') \
        .replace('debug', 'text-light-blue') \
        .replace('info', 'text-aqua') \
        .replace('error', 'text-red') \
        .replace('warning', 'text-yellow')

    return classes_convertidas

@register.filter(name='change_erro_html')
def change_erro_html(value):
    if len(value.field.errors) > 0:
        return True

    return False
