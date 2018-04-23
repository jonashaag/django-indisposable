# encoding: utf-8
from setuptools import setup

setup(
    name='django_indisposable',
    version='1.0.0',
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    packages=['django_indisposable'],
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/jonashaag/django-indisposable',
    description='Disallow disposable email addresses in Django EmailField',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Version Control",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=['mailchecker'],
    package_data={'django_indisposable': ['locale/*/LC_MESSAGES/django.*']},
)

