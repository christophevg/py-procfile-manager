import os

from conftest import create_temporary_files

from procfile_manager import ProcfileManager

def test_loading_single_process(tmpdir):
  create_temporary_files(tmpdir, {
    "Procfile" : "demo: for i in `seq 1 10`; do echo $i; sleep 1; done"
  })

  manager = ProcfileManager()
  manager.load(tmpdir.join("Procfile"))

  assert len(manager.processes) == 1
