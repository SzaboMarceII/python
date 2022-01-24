def tizedesSzamBeolvasasa(a:str) -> float:
    szam: float = None
    while(szam == None):
        beolvasottSzam: str = input(a)
        if(beolvasottSzam.replace("-", "").replace(".", "").isdigit()):
            szam = float(beolvasottSzam)
            return szam
        else:
            print("Nem számot adott meg")
