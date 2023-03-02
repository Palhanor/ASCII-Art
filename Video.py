import cv2
from Ascii import AsciiGerador

class AsciiVideo(AsciiGerador):
    def __init__(self, path=None):
        if path:
            self.video = cv2.VideoCapture(path)
        else:
            print("Inicializando a câmera...")
            self.webcam = cv2.VideoCapture(0)

    def exibir_video(self):
        exibir_original = False
        while True:
            imagem = ""
            if hasattr(self, 'webcam'):
                imagem = self.webcam.read()[1]
                imagem = cv2.flip(imagem, 1)
                cv2.imshow("Video", imagem)
                cv2.waitKey(1)
            elif hasattr(self, 'video'):
                imagem = self.video.read()[1]
                if exibir_original:
                    cv2.imshow("Video", imagem)
                    cv2.waitKey(1)
            largura_maxima = 190
            self._desenhar_tela(imagem, largura_maxima)