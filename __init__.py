import cv2
import os
import urllib.request
from prettytable import PrettyTable

class AsciiGerador:
    @staticmethod
    def _desenhar_tela(imagem):
        tela = ""
        lista_caracteres = [" ", ".", "~", ":", ";", "*", "#", "$", "@"]
        qtd_caracteres = len(lista_caracteres) - 1
        for linha in imagem:
            for pixel in linha:
                indice = round(pixel / (255 / qtd_caracteres))
                caractere = lista_caracteres[indice]
                tela += caractere + " "
            tela += "\n"
        os.system("cls")
        print(tela)

    @staticmethod
    def _gerar_dimensoes(altura, largura, largura_maxima):
        if largura <= largura_maxima:
            return altura, largura
        proporcao = largura / altura
        altura = round(largura_maxima / proporcao)
        largura = largura_maxima
        return altura, largura

class AsciiImagem(AsciiGerador):
    def __init__(self, path=None, url=None):
        if path:
            self.imagem = cv2.imread(path)
        elif url:
            urllib.request.urlretrieve(url, "Assets/img.png")
            self.imagem = cv2.imread("Assets/img.png")

    def exibir_imagem(self):
        largura_maxima = 260
        imagem_cinza = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2GRAY)
        altura, largura = imagem_cinza.shape
        altura, largura = self._gerar_dimensoes(altura, largura, largura_maxima)
        imagem_cinza = cv2.resize(imagem_cinza, (largura, altura))
        self._desenhar_tela(imagem_cinza)
        # cv2.imshow("Imagem", self.imagem)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

class AsciiVideo(AsciiGerador):
    def __init__(self, path=None):
        if path:
            self.video = cv2.VideoCapture(path)
        else:
            print("Inicializando a câmera...")
            self.webcam = cv2.VideoCapture(0)

    def exibir_video(self):
        while True:
            if hasattr(self, 'webcam'):
                imagem = self.webcam.read()[1]
                imagem = cv2.flip(imagem, 1)
                cv2.imshow("Video", imagem)
                cv2.waitKey(1)
            elif hasattr(self, 'video'):
                imagem = self.video.read()[1]
            imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            altura, largura = imagem.shape
            altura, largura = self._gerar_dimensoes(altura, largura, 190)
            imagem = cv2.resize(imagem, (largura, altura))
            self._desenhar_tela(imagem)

class AsciiGif(AsciiGerador):
    def __init__(self, path=None, url=None):
        self.path = path
        self.url = url
        if url:
            urllib.request.urlretrieve(url, "Assets/img.gif")
            self.imagem = cv2.VideoCapture("Assets/img.gif")
        elif path:
            self.imagem = cv2.VideoCapture(path)

    def exibir_gif(self):
        while True:
            resultado, imagem = self.imagem.read()
            if not resultado:
                if self.url:
                    urllib.request.urlretrieve(self.url, "Assets/img.gif")
                    self.imagem = cv2.VideoCapture("Assets/img.gif")
                elif self.path:
                    self.imagem = cv2.VideoCapture(self.path)
                resultado, imagem = self.imagem.read()
            # cv2.imshow("GIF", imagem)
            # cv2.waitKey(1)
            imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            altura, largura = imagem.shape
            altura, largura = self._gerar_dimensoes(altura, largura, 190)
            imagem = cv2.resize(imagem, (largura, altura))
            self._desenhar_tela(imagem)

if __name__ == "__main__":
    tabela_opcoes = PrettyTable()
    tabela_opcoes.field_names = ["Valor", "Comando"]
    tabela_opcoes.add_rows(
        ([1, "URL de Imagem"],
         [2, "Imagem local"],
         [3, "URL de GIF"],
         [4, "GIF local"],
         [5, "Arquivo de vídeo"],
         [6, "Webcam"]))
    print(tabela_opcoes)
    modo_input = int(input("Selecione a opção desejada: "))
    if modo_input == 1:
        url_imagem = input("Insira a URL da imagem: ")
        imagem_ascii = AsciiImagem(url=url_imagem)
        imagem_ascii.exibir_imagem()
    if modo_input == 2:
        caminho_imagem = input("Insira o caminho da imagem: ")
        imagem_ascii = AsciiImagem(path=caminho_imagem)
        imagem_ascii.exibir_imagem()
    elif modo_input == 3:
        url_gif = input("Insira a URL do gif: ")
        gif_ascii = AsciiGif(url=url_gif)
        gif_ascii.exibir_gif()
    elif modo_input == 4:
        caminho_gif = input("Insira o caminho do gif: ")
        gif_ascii = AsciiGif(path=caminho_gif)
        gif_ascii.exibir_gif()
    elif modo_input == 5:
        caminho_video = input("Insira o caminho do video: ")
        video_ascii = AsciiVideo(path=caminho_video)
        video_ascii.exibir_video()
    elif modo_input == 6:
        video_ascii = AsciiVideo()
        video_ascii.exibir_video()
