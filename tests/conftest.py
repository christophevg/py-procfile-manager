def create_temporary_files(tmpdir, files):
  for file in files:
    tmpdir.join(file).write(files[file])
