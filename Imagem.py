import cv2
import urllib.request
from Ascii import AsciiGerador

class AsciiImagem(AsciiGerador):
    def __init__(self, path=None, url=None):
        if path:
            self.imagem = cv2.imread(path)
        elif url:
            urllib.request.urlretrieve(url, "Assets/img.png")
            self.imagem = cv2.imread("Assets/img.png")

    def exibir_imagem(self):
        largura_maxima = 260
        self._desenhar_tela(self.imagem, largura_maxima)
