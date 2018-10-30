__version__ = "0.0.1"

from subprocess import check_output

class Procfile(object):
  def __init__(self, file="Procfile"):  
    self.processes = {}
    with open(str(file), "r") as fp:
      for line in fp.read().split("\n"):
        try:
          name, cmd = line.split(":", 2)
          self[name] = cmd
        except:
          pass

  def __len__(self):
    return len(self.processes)

  def __getitem__(self, name):
    return self.processes[name]

  def __setitem__(self, name, cmd):
    self.processes[name] = cmd
  
  def __iter__(self):
    for name in self.processes:
      yield name


class Manager(object):
  def __init__(self):
    self.processes = []
  
  def run(self, procfile):
    output = {}
    for name in procfile:
      output[name] = check_output(procfile[name], shell=True).decode("utf-8")
    return output

  def stop(self):
    pass
