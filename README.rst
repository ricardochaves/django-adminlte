###############################
Django-AdminLTE
###############################
Change the default Django templates to the `LTE <https://almsaeedstudio.com/themes/AdminLTE/index2.html>`_

This is my first open source project done in Django, I hope it will be useful for you and look forward to suggestions, bugs and collaborations.

### How do I get set up? ###

Instale usando PyPI:



    pip install django-lteadmin


Add the app ``adminlte`` to ``settings.py``



    INSTALLED_APPS = (
        'adminlte',
        ...
    )

Execute migrate:

    python manage.py migrate

###############################
What will you see in your admin?
###############################


Avatar
###############################
The ``User`` object will gain a relationship that will store a picture of the avatar.
You can see this in the user-inclusion form.

Menu Icons
###############################

Menu icons are set in the Model:




    class MyModel(models.Model):
        Name = models.CharField(
        ...

        def get_icon_menu_model_class(self):
            return 'fa-user'

        def get_icon_menu_add_model_class(self):
            return 'fa-plus'

        def get_icon_menu_change_model_class(self):
            return 'fa-edit'

###############################
To Do
###############################

* Create tests
* Maintain menu status after selecting an item
* Organize the code according to the `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_

