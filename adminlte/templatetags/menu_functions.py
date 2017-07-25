from django import template
from django.core.urlresolvers import reverse, resolve
from django.contrib.contenttypes.models import ContentType

from adminlte.models import *


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_menu(context, request):

    admin_site = get_admin_site(
        context.request.resolver_match.namespace).index(request)

    app_list = admin_site.context_data['app_list']

    return app_list


def get_admin_site(current_app):

    match = resolve(reverse('%s:index' % current_app))
    return match.func.admin_site


@register.filter(name='get_icon_class_from_model')
def get_icon_class_from_model(app, model):

    app_label = app['app_label']
    model_name = model['object_name']
    model_admin_url = model['admin_url']

    if app_label == 'auth':
        if model_admin_url == '/admin/auth/user/':
            return 'fa-user'
        if model_admin_url == '/admin/auth/group/':
            return 'fa-users'
        return ''

    model_type = ContentType.objects.get(
        app_label=app_label, model=model_name.lower())

    type_model = model_type.model_class()
    instance_model = type_model()

    if hasattr(instance_model, 'get_icon_menu_model_class'):
        return instance_model.get_icon_menu_model_class()

    return ''


@register.filter(name='get_icon_class_add_from_model')
def get_icon_class_add_from_model(app, model):

    app_label = app['app_label']
    model_name = model['object_name']

    model_type = ContentType.objects.get(
        app_label=app_label, model=model_name.lower())

    type_model = model_type.model_class()
    instance_model = type_model()

    if hasattr(instance_model, 'get_icon_menu_add_model_class'):
        return instance_model.get_icon_menu_add_model_class()

    return 'fa-plus'


@register.filter(name='get_icon_class_change_from_model')
def get_icon_class_change_from_model(app, model):

    app_label = app['app_label']
    model_name = model['object_name']

    model_type = ContentType.objects.get(
        app_label=app_label, model=model_name.lower())

    type_model = model_type.model_class()
    instance_model = type_model()

    if hasattr(instance_model, 'get_icon_menu_change_model_class'):
        return instance_model.get_icon_menu_change_model_class()

    return 'fa-edit'
