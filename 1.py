try: 
    with open(r"C:\Users\jaswa\OneDrive\Documents\sample.txt","r") as f1:
        r1=f1.readline()
        r2=f1.readline()
        print(f"Line 1: {r1}\nLine 2: {r2}")
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")
