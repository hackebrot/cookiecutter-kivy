=================
cookiecutter-kivy
=================

Cookiecutter template for applications built upon the kivy-framework.

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

Launch the newly created app via::

    cd project_directory
    python main.py

Tests
~~~~~

Run its testsuite either with Python3::

    cd project_directory
    python -m unittest discover

Or with nose::

    cd project_directory
    nosetests

Deployment-ready
~~~~~~~~~~~~~~~~

The app is ready for deployment to kivy launcher on Android.

http://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher


TODO
----

* Sphinx docs
* CI testing
