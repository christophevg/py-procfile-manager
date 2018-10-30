import sys

from procfile_manager import Procfile, Manager

def main():
  file = "Procfile"
  if len(sys.argv) > 1:
    file = sys.argv[1]
  procfile = Procfile(file)
  manager = Manager()
  output = manager.run(procfile)
  for name in output:
    print(name)
    print("-" * 80)
    print(output[name])

if __name__ == "__main__":
  main()
