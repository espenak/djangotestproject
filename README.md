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



## Specify/Freeze versions
Buildout prints the picked versions of new unfrozen versions after each run.
You can freeze/specify versions in the ``[versions]``-section of
``buildout.cfg``. Example:

    [versions]
    Django = 1.5.2
    mr.developer = 1.25
