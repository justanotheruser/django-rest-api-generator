import os
from django.core.management.base import AppCommand, CommandError
from django.template import Context, loader


class Command(AppCommand):
    help = 'Generates code of serializers, views and urls for CRUD commands for each model'

    def handle_app_config(self, app_config, **options):
        generators = [SerializersGenerator(app_config), ViewsGenerator(
            app_config), UrlsGenerator(app_config)]

        for gen in generators:
            with open(gen.file_name(), 'w') as f:
                f.write(gen.content())
                f.close()


class GeneratorBase:

    def __init__(self, app_config):
        self.app_name = app_config.name
        self.models = [m for m in app_config.get_models()]
        self.model_names = [m.__name__ for m in self.models]

    def content(self):
        template = loader.get_template(self.template)
        return template.render(self.get_context())

    def file_name(self):
        return os.path.join(self.app_name, self.default_file_name)


class SerializersGenerator(GeneratorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'serializers.txt'
        self.default_file_name = 'serializers.py'

    def get_context(self):
        return {'app': self.app_name, 'models': self.models, 'model_names': self.model_names}


class ViewsGenerator(GeneratorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'views.txt'
        self.default_file_name = 'views.py'

    def get_context(self):
        return {'app': self.app_name, 'models': self.model_names}


class UrlsGenerator(GeneratorBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'urls.txt'
        self.default_file_name = 'urls.py'

    def get_context(self):
        return {'app': self.app_name, 'models': self.model_names}
