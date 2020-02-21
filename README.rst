Vox
===

.. image:: https://travis-ci.com/Peilonrayz/vox.svg?branch=master
   :target: https://travis-ci.com/Peilonrayz/vox
   :alt: Build Status

About
-----

A wrapper around `nox`_ to easily run linters.

.. _nox: https://nox.thea.codes/en/stable/

Installation
------------

.. code:: shell

   $ python -m pip install vox

Documentation
-------------

Documentation is available `via GitHub <https://peilonrayz.github.io/vox/>`_.

Testing
-------

To run all tests run ``nox``. No venv is needed; nox makes all of them for us.

.. code:: shell

   $ python -m pip install --user nox
   $ git clone https://peilonrayz.github.io/vox/
   $ cd vox
   vox $ nox

License
-------

Vox is available under the MIT license.