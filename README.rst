=================
cookiecutter-kivy
=================

Basic `Cookiecutter`_ template for NUI applications built upon the `Kivy`_ python-framework.

For a feature-rich `Kivy`_ app template please check out `Cookiedozer`_.


Features
--------

* `MIT license`_ file
* Customized README
* Python gitignore


Usage
-----

Create a new app via::

    cookiecutter https://github.com/hackebrot/cookiecutter-kivy.git


Get started easily
~~~~~~~~~~~~~~~~~~

Launch the newly created app via::

    cd project_directory
    python main.py


Testsuite included
~~~~~~~~~~~~~~~~~~

Run its tests either with Python 3::

    cd project_directory
    python -m unittest discover

Or with `nose`_::

    cd project_directory
    nosetests

Or with `py.test`_::

    cd project_directory
    py.test


Deployment-ready
~~~~~~~~~~~~~~~~

The app is ready for deployment to `Kivy Launcher`_ on Android.



License
-------

Distributed under the terms of the `MIT license`_, cookiecutter-kivy is free and open source software


Issues
------

Report bugs at https://github.com/hackebrot/cookiecutter-kivy/issues.


.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Cookiedozer`: https://github.com/hackebrot/cookiedozer
.. _`Kivy Launcher`: http://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher
.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`nose`: https://github.com/nose-devs/nose/
.. _`py.test`: http://pytest.org/latest/
