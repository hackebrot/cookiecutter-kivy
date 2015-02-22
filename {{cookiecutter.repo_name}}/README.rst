===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Features
--------

* TODO

Usage
-----

Launching the app
~~~~~~~~~~~~~~~~~

`Kivy`_ is compatible with Python2 as well as Python3::

    cd {{ cookiecutter.repo_name }} 
    python main.py

Running the testsuite
~~~~~~~~~~~~~~~~~~~~~

Run its testsuite either with Python3::

    cd {{ cookiecutter.repo_name }} 
    python -m unittest discover

Or with nose::

    cd {{ cookiecutter.repo_name }} 
    nosetests

Or with py.test::

    cd {{ cookiecutter.repo_name }}
    py.test

Deploying to Android
~~~~~~~~~~~~~~~~~~~~

You can easily run the app on Android by using the kivy launcher. See:

http://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher


License
-------

Distributed under the terms of the `MIT license`_, {{cookiecutter.repo_name}} free and open source software


Issues
------

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues.


.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
