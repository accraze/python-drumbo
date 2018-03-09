========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-drumbo/badge/?style=flat
    :target: https://readthedocs.org/projects/python-drumbo
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-drumbo.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/python-drumbo

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/accraze/python-drumbo?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/accraze/python-drumbo

.. |requires| image:: https://requires.io/github/accraze/python-drumbo/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/accraze/python-drumbo/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/accraze/python-drumbo/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/accraze/python-drumbo

.. |version| image:: https://img.shields.io/pypi/v/drumbo.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/drumbo

.. |commits-since| image:: https://img.shields.io/github/commits-since/accraze/python-drumbo/v0.2.0.svg
    :alt: Commits since latest release
    :target: https://github.com/accraze/python-drumbo/compare/v0.2.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/drumbo.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/drumbo

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/drumbo.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/drumbo

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/drumbo.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/drumbo


.. end-badges

Simple Step Sequencer

* Free software: BSD 2-Clause License

Installation
============

::

    pip install drumbo

Documentation
=============

https://python-drumbo.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
