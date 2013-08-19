Minimalistic Django testproject with bootstrap. Perfect template for testing
simple stuff.

## Initialize bootstrap

    $ virualenv venv
    $ venv/bin/python bootstrap.py
    $ bin/buildout

If you get version problems with setuptools, run:

    $ venv/bin/pip install --upgrade setuptools

and re-run from ``venv/bin/python bootstrap.py``.


## Usage
By default, we have a single Django app in ``src/my_example/``. Edit that app,
or add more apps if you need to try out some multi-app features. When you add
an app to ``src/``, you need to add it to:

- the ``[sources]``-section of ``buildout.cfg``, and re-run ``bin/buildout``.
- ``INSTALLED_APPS`` in ``djangosettings.py``.
- ``djangourls.py`` if you add any views.


## Specify/Freeze versions
Buildout prints the picked versions of new unfrozen versions after each run.
You can freeze/specify versions in the ``[versions]``-section of
``buildout.cfg``. Example:

    [versions]
    Django = 1.5.2
    mr.developer = 1.25
