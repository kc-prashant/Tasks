try:
    with open("\\Users\\macbook\\desktop\\Prashant\\INTERN\firstfile.txt") as F1:
        with open("\\Users\\macbook\\desktop\\Prashant\\INTERNN\thirdfile.txt") as F3:
            for i in F1:
                F3.write(i)

except:
    print("FIle is not found try again!")

else:
    F1.close
    print("FIle is closed...")