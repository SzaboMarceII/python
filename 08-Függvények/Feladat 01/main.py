#Írjunk programot amely összead, kivon, szoroz és eloszt két számot. A matematikai műveleteket fügvényekkel oldjuk meg.

from matematika import *
from ioa import *

osszeg: float = None
kulonbseg: float = None
szorzat: float = None
hanyados: float = None
szam1: float = None
szam2: float = None
beolvasottSzam: str = ""



szam1 = tizedesSzamBeolvasasa("Kérem az 1. számot: ")
szam2 = tizedesSzamBeolvasasa("Kérem az 2. számot: ")

osszeg = osszeadas(szam1, szam2)
kulonbseg = kivonas(szam1, szam2)
szorzat = szorzas(szam1, szam2)
hanyados = osztas(szam1, szam2)

print(f"A számok összege: {osszeg}, a különbségük: {kulonbseg}, a szorzatuk: {szorzat} és a hányadosuk: {hanyados}")