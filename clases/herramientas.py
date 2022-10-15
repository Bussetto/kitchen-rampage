from io import BytesIO as Convertir_a_Bytes
from urllib.request import urlopen as Leer_url
from translate import Translator

class Conversor_Imagen():
    @classmethod
    def convertir_url_a_imagen(cls, imagen_url):
        imagen_string = Leer_url(imagen_url).read()
        imagen_archivo = Convertir_a_Bytes(imagen_string)
        return imagen_archivo

class Traductor(Translator):
    def __init__(self, traducir_de, traducir_a):
        super().__init__(to_lang=traducir_a, from_lang=traducir_de)        

    def traducir(self, texto_a_traducir):
        return super().translate(texto_a_traducir)