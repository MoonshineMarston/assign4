x=input("Enter text to write to the file :")
y=input("Enter additonal text to append :")
with open (r"C:\Users\jaswa\OneDrive\Documents\output.txt","w") as f1:
    w=f1.write(x+"\n")
with open (r"C:\Users\jaswa\OneDrive\Documents\output.txt","a") as f1:
    a=f1.write(y+"\n")
with open (r"C:\Users\jaswa\OneDrive\Documents\output.txt","r") as f1:
    r=f1.read()
    print(f"Final content of output.txt:\n{r}")