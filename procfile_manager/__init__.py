__version__ = "0.0.2"

import os
import time
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
    self.file = str(file)
    self.processes = {}
    with open(self.file, "r") as fp:
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
  def __init__(self, name, cmd):
    self.name = name
    self.process = subprocess.Popen(
      cmd,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      shell=True
    )

  @property
  def running(self):
    return self.process.poll() == None

  @property
  def output(self):
    return self.process.communicate()[0]
  
  def stop(self):
    if not self.running: return
    try:
      self.process.kill()
    except OSError as e:
      logging.error("couldn't kill {0}: {1}".format(self.name, self.process.pid))

class Manager(object):
  def __init__(self, procfile):
    self.procfile = procfile
    self.processes = {}
  
  def run(self, blocking=True):
    for name in self.procfile:
      self.processes[name] = Process(name, self.procfile[name])
    logging.info("started all processes from {0}".format(self.procfile.file))

    if blocking:
      self.wait()
      output = {}
      for name in self.processes:
        output[name] = self.processes[name].output
      return output

  def running(self):
    still_running = False
    for name in self.processes:
      still_running |= self.processes[name].running
    return still_running

  def wait(self):
    while self.running():
      time.sleep(0.1)

  def stop(self):
    for name in self.processes:
      self.processes[name].stop()
    logging.info("stopped all processes from {0}".format(self.procfile.file))
