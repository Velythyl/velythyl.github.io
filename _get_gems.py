with open("./_config.yml") as f:
  line = ""
  while "plugins:" not in line:
    line = f.readline()
  
  line = f.readline()

  gems = []
  while "# Custom vars" not in line:
    gems.append(line.strip()[2:])
    line = f.readline()

print(" ".join(gems).strip())
    
