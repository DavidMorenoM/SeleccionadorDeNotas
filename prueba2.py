import Reforma
import os

#Reforma.VerificarNulos()
#os.remove("folioNulos.bin")

#Reforma.GuardarUltimoFolio("2170194")
folio=Reforma.ObtenerPrimerFolio()
folioInt=int(folio)

contadorNulos=0;
flagFinal=0;
i=1;
folioTemp=folioInt;

while flagFinal == 0:
	folioUrl=folioInt+i
	i=i+1
	url=Reforma.CrearUrl(str(folioUrl))
	nota=Reforma.DescargarNota(url)
	if nota["titulo"]=="None":
		contadorNulos=contadorNulos+1
		print(contadorNulos)
		Reforma.GuardarNulo(folioUrl)
	else:
		contadorNulos=0
		folioTemp=folioUrl

	if contadorNulos>=50:
		flagFinal=1
		folioTemp=folioUrl-1

	if nota["titulo"]=="Error de conexión":
		flagFinal=1;

	print(nota["titulo"]+" -> "+nota["fechaSubida"]+" -> "+str(folioUrl))
	print(folioTemp)
	print("-------------------------------------------------------------------------------------------------")

Reforma.GuardarUltimoFolio(str(folioTemp))

Reforma.MemoriaNulos(folioTemp)