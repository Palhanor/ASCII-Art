import cv2
import urllib.request
from Ascii import AsciiGerador


class AsciiGif(AsciiGerador):
    def __init__(self, path=None, url=None):
        self.path = path
        self.url = url
        self.gif = self.configurar_gif()

    def configurar_gif(self):
        if self.path:
            return cv2.VideoCapture(self.path)
        elif self.url:
            urllib.request.urlretrieve(self.url, "Assets/img.gif")
            return cv2.VideoCapture("Assets/img.gif")

    def exibir_gif(self):
        while True:
            resultado, imagem = self.gif.read()
            if not resultado:
                self.gif = self.configurar_gif()
                resultado, imagem = self.gif.read()
            largura_maxima = 190
            self._desenhar_tela(imagem, largura_maxima)
