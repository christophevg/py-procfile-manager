__version__ = "0.0.1"

import os
import sys
import subprocess
import threading

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

import time

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
    self.processes = {}
    self.children = {}
    self.monitor = None
  
  def run(self, procfile, blocking=True):
    for name in procfile:
      self.processes[name] = {
        "process": subprocess.Popen(procfile[name],
                                    stdout=subprocess.PIPE,
                                    shell=True),
        "output": "",
        "running": True
      }
    self.monitor = threading.Thread(target=self.monitor_processes)
    self.monitor.deamon = True
    self.monitor.start()

    if blocking:
      self.wait()
      output = {}
      for name in self.processes:
        output[name] = self.processes[name]["output"]
      return output

  def monitor_processes(self):
    logging.debug("starting process monitor")
    while self.running():
      for name in self.processes:
        if self.processes[name]["running"]:
          # TODO read all available output?
          b = self.processes[name]["process"].stdout.read(1)
          if b == '' and self.processes[name]["process"].poll() != None:
            self.processes[name]["running"] = False
            logging.debug("process {0} has stopped running".format(name))
          if b != '': self.processes[name]["output"] += b
    logging.debug("all processes have finished")

  def running(self):
    still_running = False
    for name in self.processes:
      still_running |= self.processes[name]["running"]
    return still_running

  def wait(self):
    while self.running():
      time.sleep(.1)

  def stop(self):
    pass
