def nevBekeres() -> str:
    nev:str = None

    while(nev == None):
        data:str=input("Kérem a nevét: ")

        if(len(data)<3):
            print("Túl rövid a név, minimum 3 karakter")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data
            
    return nev