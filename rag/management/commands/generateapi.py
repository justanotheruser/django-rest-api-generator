import os
from django.core.management.base import AppCommand, CommandError
from django.template import Context, loader


class Command(AppCommand):
    help = 'Generates code of serializers, views and urls for CRUD commands for each model'

    def handle_app_config(self, app_config, **options):
        models = [m for m in app_config.get_models()]
        model_names = [m.__name__ for m in models]
        context = {'app': app_config.name,
                   'models': models, 'model_names': model_names}
        print(context)

        for m in models:
            print(m.__name__)
            for field in m._meta.get_fields():
                print(f'{field.name}: {field}')

        serializers_template = loader.get_template('serializers.html')
        print(serializers_template.render(context))
        serializers = serializers_template.render(context)

        serializers_file_name = os.path.join(app_config.name, 'serializers.py')
        with open(serializers_file_name, 'w') as f:
            f.write(serializers)
            f.close()

        views_template = loader.get_template('views.html')
        print(views_template.render(context))
        views = views_template.render(context)

        views_file_name = os.path.join(app_config.name, 'views.py')
        with open(views_file_name, 'w') as f:
            f.write(views)
            f.close()
