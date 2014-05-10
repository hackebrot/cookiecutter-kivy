=================
cookiecutter-kivy
=================

Cookiecutter template for NUI applications built upon the kivy python-framework.

Related
-------

* cookiecutter - https://github.com/audreyr/cookiecutter
* kivy - https://github.com/kivy/kivy
* nose - https://github.com/nose-devs/nose/

Usage
-----

Create a new app via::

    cookiecutter https://github.com/hackebrot/cookiecutter-kivy.git


Features
--------

* GPL v2 license
* Customized README
* Python gitignore

Get started easily
~~~~~~~~~~~~~~~~~~

Launch the newly created app via::

    cd project_directory
    python main.py

Testsuite included
~~~~~~~~~~~~~~~~~~

Run its tests either with Python3::

    cd project_directory
    python -m unittest discover

Or with nose::

    cd project_directory
    nosetests

Or with py.test::

    cd project_directory
    py.test

Deployment-ready
~~~~~~~~~~~~~~~~

The app is ready for deployment to kivy launcher on Android.

http://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher

TODO
----

* Buildozer spec
* Sphinx docs
* CI testing
