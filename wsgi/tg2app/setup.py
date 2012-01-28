# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       True
#
#

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=['WebTest >= 1.2.3',
               'nose',
               'coverage',
               'wsgiref',
               'repoze.who-testutil >= 1.0.1',
               ]
if sys.version_info[:2] == (2,4):
    testpkgs.extend(['hashlib', 'pysqlite'])

setup(
    name='tg2app',
    version='0.1',
    description='Scrape foreclosures from Monroe County for great justice.',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    #url='',
    install_requires=[
        "Pylons==1.0.0",
        "WebOb<=1.0.8",
        "PasteDeploy",
        "tg.devtools",
        "tgscheduler",
        "TurboGears2 >= 2.1.2",
        "Mako",
        "zope.sqlalchemy >= 0.4",
        "repoze.tm2 >= 1.0a5",
        "sqlalchemy",
        "sqlalchemy-migrate",
        "repoze.what-quickstart",
        "repoze.what >= 1.0.8",
        "repoze.what-quickstart",
        "repoze.who-friendlyform >= 1.0.4",
        "repoze.what-pylons >= 1.0",
        "repoze.what.plugins.sql",
        "repoze.who==1.0.19",
        "tgext.admin >= 0.3.9",
        "mechanize",
        "BeautifulSoup",
        "docutils",
        "tw2.jqplugins.ui>=2.0b26",
        "tw2.jqplugins.jqgrid",
        "tw2.slideymenu",
        "tw2.jit",
        "tw2.polymaps>=0.1.a4",
        ],
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2', 'tg.devtools'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'tg2app': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'tg2app': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
                        ('public/**', 'ignore', None)]},

    entry_points="""
    [paste.app_factory]
    main = tg2app.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [tw2.widgets]
    # Register your widgets so they can be listed in the
    # WidgetBrowser
    tg2app.widgets = tg2app.widgets

    """,
    dependency_links=[
        "http://www.turbogears.org/2.1/downloads/current/"
        ],
    zip_safe=False
)
