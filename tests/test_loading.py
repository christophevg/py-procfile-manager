import os

from conftest import create_temporary_files

from procfile_manager import Procfile, Manager

def test_loading_procfile_with_one_process(tmpdir):
  name = "demo"
  cmd  = "for i in `seq 1 10`; do echo $i; done"
  create_temporary_files(tmpdir, { "Procfile" : "{0}:{1}".format(name, cmd) })

  procfile = Procfile(tmpdir.join("Procfile"))
  
  assert len(procfile) == 1
  assert procfile[name] == cmd

def test_running_procfile_with_one_process(tmpdir):
  name = "demo"
  cmd  = "for i in `seq 1 10`; do echo $i; done"
  create_temporary_files(tmpdir, { "Procfile" : "{0}:{1}".format(name, cmd) })

  procfile = Procfile(tmpdir.join("Procfile"))
  manager = Manager()
  output = manager.run(procfile)

  assert len(output) == 1
  assert output[name] == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
