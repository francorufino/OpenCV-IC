import cv2 as cv

img = cv.imread("photos/cat2.jpeg")

if img is None:
    print("Erro: imagem não encontrada ou formato não suportado.")
else:
    cv.imshow("Gato", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
