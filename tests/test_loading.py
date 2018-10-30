import os

from conftest import create_temporary_files

from procfile_manager import Procfile

def test_loading_procfile_with_one_process(tmpdir):
  name = "demo"
  cmd  = "for i in `seq 1 10`; do echo $i; sleep 1; done"
  create_temporary_files(tmpdir, { "Procfile" : "{0}:{1}".format(name, cmd) })

  procfile = Procfile(tmpdir.join("Procfile"))
  
  assert len(procfile) == 1
  assert procfile[name] == cmd
