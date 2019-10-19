from django.apps import AppConfig

# add this configuration class to the apps list in the main settings.py whenever you create a new app
# this config class is referencing the "blog" subdirectory under "templates", loading in the templates
# you have created through the AppConfig function

class BlogConfig(AppConfig):
    name = 'blog'
