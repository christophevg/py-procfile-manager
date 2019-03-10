__version__ = "0.0.1"

import os
from dotenv import load_dotenv
import logging

import sys
import subprocess
import threading
import time

# read environment from .env file

load_dotenv()

# setup logging: formatting and console logger

logger = logging.getLogger()

formatter = logging.Formatter(
  "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s",
  "%Y-%m-%d %H:%M:%S %z"
)

if len(logger.handlers) > 0:
  logger.handlers[0].setFormatter(formatter)
else:
  consoleHandler = logging.StreamHandler()
  consoleHandler.setFormatter(formatter)
  logger.addHandler(consoleHandler)

LOG_LEVEL = os.environ.get("LOG_LEVEL") or "WARN"
logger.setLevel(logging.getLevelName(LOG_LEVEL))


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

class Process(object):
  def __init__(self, cmd):
    self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    self.output  = b""
    self.running = True

class Manager(object):
  def __init__(self):
    self.processes = {}
    self.children = {}
    self.monitor = None
  
  def run(self, procfile, blocking=True):
    for name in procfile:
      self.processes[name] = Process(procfile[name])
      self.processes[name] = {
        "process": subprocess.Popen(procfile[name],
                                    stdout=subprocess.PIPE,
                                    shell=True),
        "output": b"",
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
          b = self.processes[name]["process"].stdout.read(1)
          if len(b) < 1:
            if self.processes[name]["process"].poll() != None:
              self.processes[name]["running"] = False
              logging.info("process {0} has stopped running".format(name))
          else:
            self.processes[name]["output"] += b
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
    for name in self.processes:
      self.processes[name]["process"].kill()
