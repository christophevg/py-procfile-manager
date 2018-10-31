# Procfile Manager

> A Python module to manage Procfiles, running them in the first place, with as little restrictions as possible.

[![Latest Version on PyPI](https://img.shields.io/pypi/v/procfile-manager.svg)](https://pypi.python.org/pypi/procfile-manager/)
[![Build Status](https://secure.travis-ci.org/christophevg/py-procfile-manager.svg?branch=master)](http://travis-ci.org/christophevg/py-procfile-manager)
[![Coverage Status](https://coveralls.io/repos/github/christophevg/py-procfile-manager/badge.svg?branch=master)](https://coveralls.io/github/christophevg/py-procfile-manager?branch=master)
[![Build with PyPi Tempalte](https://img.shields.io/badge/PyPi_Template-v0.0.1-blue.svg)](https://github.com/christophevg/pypi-template)

## Rationale

Once upon a time, not so long ago, at a desk pretty nearby, I needed a way to read and execute Procfiles. So I embarked on a quest to find a Python module that did just that, since I didn't _want_ to roll my own:

[https://pypi.org/search/?q=procfile](https://pypi.org/search/?q=procfile) returned the following top-5:
 
* procfile 0.1.0
* bureaucrat 0.3.6
* honcho 1.0.1
* heywood 0.3
* strawboss 0.2.0

and I tried each one of them. I even proposed to one of the projects to create a rather large PR to expose the functionality in an open way. None were useable in my case, requiring a Python module to access its functionality (not just a command line interfaced script), requiring also Python 2.7 support (not only 3.5) and allowing the ProcessManager to be started in a thread (so not using any form of `signal`).

So there are my three good reasons for writing yet another Procfile module ;-)

And although I couldn't use the mentioned projects as-is, I give most credit for the code in this repository to each one of them, teaching me again a lot about how to go about constructing a Python well-formed module, including testing,...

## Getting Started

```bash
$ virtualenv venv

$ . venv/bin/activate

(venv) $ pip install procfile-manager

$ echo > Procfile <<EOT
demo: for i in `seq 1 10`; do echo $i; sleep 1; done
EOT

(venv) $ python
Python 2.7.13 (default, May 24 2017, 12:12:01) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from procfile_manager import Procfile, Manager
>>> procfile = Procfile("Procfile")
>>> manager = Manager()
>>> manager.run(procfile)
{'demo': u'1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'}
>>> 
```

The module is also runnable. Given the same Procfile...

```bash
$ python -m procfile_manager
demo
--------------------------------------------------------------------------------
1
2
3
4
5
6
7
8
9
10
```
