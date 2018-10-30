__version__ = "0.0.1"

class Procfile(object):
  def __init__(self, file="Procfile"):  
    self.processes = {}
    with open(str(file), "r") as fp:
      for line in fp.read().split("\n"):
        name, cmd = line.split(":", 2)
        self[name] = cmd

  def __len__(self):
    return len(self.processes)

  def __getitem__(self, name):
    return self.processes[name]

  def __setitem__(self, name, cmd):
    self.processes[name] = cmd


class Manager(object):
  def __init__(self):
    self.processes = []
  
  def load(self, procfile):
    pass
  
  def run(self, blocking=True):
    pass

  def stop(self):
    pass
