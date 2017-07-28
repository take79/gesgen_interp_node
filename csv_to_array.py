with  open("input_vec.csv", "r") as f:
  raw = f.readlines();
    for line in raw:
      line = line.split(",")
    print(len(raw))
