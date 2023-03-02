import os
import cv2

class AsciiGerador:
    def _desenhar_tela(self, imagem, largura_maxima):
        tela = ""
        lista_caracteres = [" ", ".", "~", ":", ";", "*", "#", "$", "@"]
        qtd_caracteres = len(lista_caracteres) - 1
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        altura, largura = self._gerar_dimensoes(imagem.shape, largura_maxima)
        imagem = cv2.resize(imagem, (largura, altura))
        for linha in imagem:
            for pixel in linha:
                grau_luminosidade = 255 / qtd_caracteres
                indice = round(pixel / grau_luminosidade)
                caractere = lista_caracteres[indice]
                tela += caractere + " "
            tela += "\n"
        os.system("cls")
        print(tela)

    @staticmethod
    def _gerar_dimensoes(dimensoes_originais, largura_maxima):
        altura, largura = dimensoes_originais
        if largura <= largura_maxima:
            return altura, largura
        proporcao = largura / altura
        altura = round(largura_maxima / proporcao)
        largura = largura_maxima
        return altura, largura