import time
x = True
while x:
    print("Choose any method:- \n1.Encode \n2.Decode\n3.Exit")
    cde = int(input("Enter code - "))
    print("----------------------------------")

    if cde == 3:
        x = False

    elif cde == 1:
        #Encode  
        text = str(input("Enter Text = "))
        print("----------------------------------")
        encrpt = text.replace("a", "&.e7")
        encrpt = encrpt.replace("i", "(.e9")
        encrpt = encrpt.replace("o", ").e0")
        encrpt = encrpt.replace("u", "@.e2")
        encrpt = encrpt.replace(" ","?.?")
        encrpt = encrpt.replace("A", "e*L")
        encrpt = encrpt.replace("B", "e*M")
        encrpt = encrpt.replace("C", "e*N")
        encrpt = encrpt.replace("D", "e*O")
        encrpt = encrpt.replace("E", "e*P")
        encrpt = encrpt.replace("F", "e*Q")
        encrpt = encrpt.replace("S", "e*R")
        encrpt = encrpt.replace("T", "e*Z")
        encrpt = encrpt.replace("U", "e*G")
        encrpt = encrpt.replace("V", "e*H")
        encrpt = encrpt.replace("W", "e*I")
        encrpt = encrpt.replace("X", "e*J")
        encrpt = encrpt.replace("Y", "e*K")
        encrpt = encrpt.replace("5", ":t")
        encrpt = encrpt.replace("4", ":r")
        encrpt = encrpt.replace("1", ":q")
        encrpt = encrpt.replace("6", ":y")
        encrpt = encrpt.replace("8", ":i")

        encptext = encrpt
        print("Your encoded Text is = ",encptext)
        print("----------------------------------")
        time.sleep(4)

    elif cde == 2:
        # Decode
        text = str(input("Enter Text = "))
        print("----------------------------------")
        decrpt = text.replace("&.e7", "a")
        decrpt = decrpt.replace("(.e9", "i")
        decrpt = decrpt.replace(").e0", "o")
        decrpt = decrpt.replace("@.e2", "u")
        decrpt = decrpt.replace("?.?"," ")
        decrpt = decrpt.replace("e*L", "A")
        decrpt = decrpt.replace("e*M", "B")
        decrpt = decrpt.replace("e*N", "C")
        decrpt = decrpt.replace("e*O", "D")
        decrpt = decrpt.replace("e*P", "E")
        decrpt = decrpt.replace("e*Q", "F")
        decrpt = decrpt.replace("e*R", "S")
        decrpt = decrpt.replace("e*Z", "T")
        decrpt = decrpt.replace("e*G", "U")
        decrpt = decrpt.replace("e*H", "V")
        decrpt = decrpt.replace("e*I", "W")
        decrpt = decrpt.replace("e*J", "X")
        decrpt = decrpt.replace(":t", "5")
        decrpt = decrpt.replace(":r", "4")
        decrpt = decrpt.replace(":q", "1")
        decrpt = decrpt.replace(":y", "6")
        decrpt = decrpt.replace(":i", "8")

        dectext = decrpt
        print("Your Decoded text is = ",dectext)
        print("----------------------------------")
        time.sleep(4)