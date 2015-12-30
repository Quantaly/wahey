git = raw_input("Wahey? (y/n)\n")
while not (git.startswith("y") or git.startswith("n")):
    print "Invalid response."
    git = raw_input("Wahey? (y/n)\n")
if git.startswith("y"):
    print "Wahey!"
else:
    print "Wahey..."
    
