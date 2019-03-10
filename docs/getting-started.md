# Getting Started

Create a virtual environment and install `procfile-manager` using `pip`:

```bash
$ virtualenv venv
$ . venv/bin/activate
(venv) $ pip install procfile-manager
```

Create a simple Procfile that counts to 10, printing it to stdout:

```bash
$ echo > Procfile <<EOT
demo: for i in `seq 1 10`; do echo $i; sleep 1; done
EOT
```

Now use `procfile-manager` to execute it:

```bash
(venv) $ python
Python 2.7.13 (default, May 24 2017, 12:12:01)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from procfile_manager import Procfile, Manager
>>> procfile = Procfile("Procfile")
>>> manager = Manager()
>>> manager.run(procfile)
2018-11-04 18:55:14,981 - root - DEBUG - starting process monitor
2018-11-04 18:55:25,086 - root - DEBUG - process demo has stopped running
2018-11-04 18:55:25,087 - root - DEBUG - all processes have finished
{'demo': '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'}
>>> 
```

The module is also runnable. Given the same Procfile, simple call it like this from the repository:

```bash
(venv) $ python -m procfile_manager
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

Or, when installed, simple call the installed shell command:

```bash
$ procfile-manager
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

## Non-Blocking

You can also instruct the manager to _not_ block when calling `run` on it:

```bash
(venv) $ python
Python 2.7.13 (default, May 24 2017, 12:12:01)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from procfile_manager import Procfile, Manager
>>> procfile = Procfile("Procfile")
>>> manager = Manager()
>>> manager.run(procfile, blocking=False)
2018-11-04 18:56:53,316 - root - DEBUG - starting process monitor
>>> manager.running()
True
>>> manager.running()
True
2018-11-04 18:57:03,434 - root - DEBUG - process demo has stopped running
2018-11-04 18:57:03,435 - root - DEBUG - all processes have finished
>>> manager.running()
False
>>> for name in manager.processes:
...     print(manager.processes[name]["output"])
...
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
>>>
```
