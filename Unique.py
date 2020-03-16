file=open("sample.txt","r+")
lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques = set(line.split())

    print(f"Unique words: {len(uniques)}")
    
  
