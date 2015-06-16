from django.dispatch import receiver
from django.template import Context, Template

from openslides.config.api import ConfigCollection, ConfigVariable, config
from openslides.config.signals import config_signal
from openslides.utils.test import TestCase


class ConfigTagAndFilter(TestCase):
    def test_config_tag(self):
        config['taiNg3reQuooGha4'] = 'iWoor0caThieK7yi'
        template = Template("{% load tags %} The config var is {% get_config 'taiNg3reQuooGha4' %}.")
        self.assertTrue('The config var is iWoor0caThieK7yi.' in template.render(Context({})))

    def test_config_filter(self):
        config['fkjTze56ncuejWqs'] = 'REG56Hnmfk9TdfsD'
        template = Template("{% load tags %} The config var is {{ 'fkjTze56ncuejWqs'|get_config }}.")
        self.assertTrue('The config var is REG56Hnmfk9TdfsD.' in template.render(Context({})))

    def test_both_in_one(self):
        config['jfhsnezfh452w6Fg'] = True
        config['sdmvldkfgj4534gk'] = 'FdgfkR04jtg9f8bq'
        template_code = """{% load tags %}
            {% if 'jfhsnezfh452w6Fg'|get_config %}
                {% get_config 'sdmvldkfgj4534gk' %}
            {% else %}
                bad_e0fvkfHFD
            {% endif %}"""
        template = Template(template_code)
        self.assertTrue('FdgfkR04jtg9f8bq' in template.render(Context({})))
        self.assertFalse('bad_e0fvkfHFD' in template.render(Context({})))


@receiver(config_signal, dispatch_uid='set_simple_config_view_template_tag_test')
def set_simple_config_view_template_tag_test(sender, **kwargs):
    """
    Sets a simple config view with some config variables but without
    grouping.
    """
    return ConfigCollection(
        title='Config vars for testing with template tag',
        url='testsimplepagetemplatetag',
        variables=(ConfigVariable(name='taiNg3reQuooGha4', default_value=None),
                   ConfigVariable(name='fkjTze56ncuejWqs', default_value=None),
                   ConfigVariable(name='jfhsnezfh452w6Fg', default_value=None),
                   ConfigVariable(name='sdmvldkfgj4534gk', default_value=None)))
