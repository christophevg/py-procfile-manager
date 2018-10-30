import sys

from procfile_manager import ProcfileManager

def main():
  procfile = "Procfile"
  if len(sys.argv) > 1:
    procfile = sys.argv[1]
  manager = ProcfileManager()
  manager.load(procfile)
  manager.run()

if __name__ == "__main__":
    main()
