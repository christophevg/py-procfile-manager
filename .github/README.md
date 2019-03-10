# Procfile Manager

> A Python module to manage Procfiles, running them in the first place, with as little restrictions as possible

[![Latest Version on PyPI](https://img.shields.io/pypi/v/procfile-manager.svg)](https://pypi.python.org/pypi/procfile-manager/)
[![Supported Implementations](https://img.shields.io/pypi/pyversions/procfile-manager.svg)](https://pypi.python.org/pypi/procfile-manager/)
[![Build Status](https://secure.travis-ci.org/christophevg/py-procfile-manager.svg?branch=master)](http://travis-ci.org/christophevg/py-procfile-manager)
[![Documentation Status](https://readthedocs.org/projects/procfile-manager/badge/?version=latest)](https://procfile-manager.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/christophevg/py-procfile-manager/badge.svg?branch=master)](https://coveralls.io/github/christophevg/py-procfile-manager?branch=master)
[![Built with PyPi Template](https://img.shields.io/badge/PyPi_Template-v0.0.6-blue.svg)](https://github.com/christophevg/pypi-template)

## Rationale

Once upon a time, not so long ago, at a desk pretty nearby, I needed a way to read and execute Procfiles. So I embarked on a quest to find a Python module that did just that, since I didn't _want_ to roll my own:

[https://pypi.org/search/?q=procfile](https://pypi.org/search/?q=procfile) returned the following top-5:
 
* procfile 0.1.0
* bureaucrat 0.3.6
* honcho 1.0.1
* heywood 0.3
* strawboss 0.2.0

and I tried each one of them. I even proposed to one of the projects to create a rather large PR to expose the functionality in an open way. None were useable in my case, requiring a Python module to access its functionality (not just a command line interfaced script) and allowing the ProcessManager to be started in a thread (so not using any form of `signal`).

So there are my _good_ reasons for writing yet another Procfile module ;-)

And although I couldn't use the mentioned projects as-is, I give most credit for the code in this repository to each one of them, teaching me again a lot about how to go about constructing a Python well-formed module, including testing,...

## Documentation

Visit [Read the Docs](https://procfie-manager.readthedocs.org) for the full documentation, including overviews and walkthroughs.
