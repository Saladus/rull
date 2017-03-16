#!/bin/python

##-----------------------------------------------------------------##
## !! MUUTKE FAILIDE ASUKOHAD ENDA KASUTAJAKESKONNALE VASTAVAKS !! ##
##-----------------------------------------------------------------##

#Impordime vajalikud moodulid
from time import localtime, strftime
import sys

#Pisike graafiline element kuupäeva eraldamiseks tekstist
gui = "--------------------"
#Defineerime kuupäeva ja kellaaja formaadi
kuupäev_kellaaeg = strftime("%Y-%m-%d %H:%M:%S", localtime())
#Loome tühja järjendi mida kasutame sisestatud teksti hoiustamiseks.
#Vajalik mitmerealise kasutajasisendi töötlemiseks.
puhver = []

#Kontrollime kas skript käivitatakse argumentidega
if not len(sys.argv) > 1:
	#Standartne asukoht päevikufailile
	#juhul kui skript käivitada ilma argumentideta.
	fail = open("/home/vaikus/Dokumendid/Privaatne/päevik.txt", "a")
else:
	#Argumendina antava faili asukoht.
	fail = open("/home/vaikus/Dokumendid/Privaatne/" + str(sys.argv[1]), "a")

#Võtame vastu kasutajapoolset sisendit 
#kuni sisestatakse eraldi real "."
while True:
	print("> ", end="")
	rida = input()
	if rida == ".":
		break
	puhver.append(rida)
tekst = "\n".join(puhver)

#Kirjutame puhvri sisu koos kuupäevaga faili.
fail.write(gui + "\n" + str(kuupäev_kellaaeg) + "\n" + gui)
fail.write("\n" + tekst + "\n")
fail.close()


