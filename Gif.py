import cv2
import urllib.request
from Ascii import AsciiGerador

class AsciiGif(AsciiGerador):
    def __init__(self, path=None, url=None):
        self.path = path
        self.url = url
        if path:
            self.gif = cv2.VideoCapture(path)
        elif url:
            urllib.request.urlretrieve(url, "Assets/img.gif")
            self.gif = cv2.VideoCapture("Assets/img.gif")

    def exibir_gif(self):
        exibir_original = False
        while True:
            resultado, imagem = self.gif.read()
            if not resultado:
                if self.url:
                    urllib.request.urlretrieve(self.url, "Assets/img.gif")
                    self.gif = cv2.VideoCapture("Assets/img.gif")
                elif self.path:
                    self.gif = cv2.VideoCapture(self.path)
                resultado, imagem = self.gif.read()
            largura_maxima = 190
            self._desenhar_tela(imagem, largura_maxima)
            if exibir_original:
                cv2.imshow("GIF", imagem)
                cv2.waitKey(1)