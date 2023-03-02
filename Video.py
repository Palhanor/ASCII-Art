import cv2
from Ascii import AsciiGerador


class AsciiVideo(AsciiGerador):
    def __init__(self, path=0):
        self.path = path
        self.video = cv2.VideoCapture(path)
        if not self.video.isOpened():
            print("O vídeo não pôde ser aberto...")

    def exibir_video(self):
        while self.video.isOpened():
            if self.path == 0:
                _, imagem = self.video.read()
                imagem = cv2.flip(imagem, 1)
                cv2.imshow("Video", imagem)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
            else:
                _, imagem = self.video.read()
            largura_maxima = 190
            self._desenhar_tela(imagem, largura_maxima)
