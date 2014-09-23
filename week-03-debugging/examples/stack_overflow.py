
i = 0

def recurse():
    global i
    i += 1
    print i
    recurse()

recurse()
    
