import os

from conftest import create_temporary_files

from procfile_manager import Procfile, Manager

def test_running_procfile_with_one_process(tmpdir):
  name = "demo"
  cmd  = "for i in `seq 1 10`; do echo $i; done"
  create_temporary_files(tmpdir, { "Procfile" : "{0}:{1}".format(name, cmd) })

  procfile = Procfile(tmpdir.join("Procfile"))
  manager = Manager()
  output = manager.run(procfile)

  assert len(output) == 1
  assert output[name] == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"

def test_running_procfile_with_two_processes(tmpdir):
  name1 = "demo1"
  cmd1  = "for i in `seq 1 10`; do echo $i; done"
  name2 = "demo2"
  cmd2  = "for i in `seq 5 15`; do echo $i; done"
  create_temporary_files(tmpdir, {
    "Procfile" : "{0}:{1}\n{2}:{3}".format(name1, cmd1, name2, cmd2)
  })

  procfile = Procfile(tmpdir.join("Procfile"))
  manager = Manager()
  output = manager.run(procfile)

  assert len(output) == 2
  assert output[name1] == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
  assert output[name2] == "5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n"
