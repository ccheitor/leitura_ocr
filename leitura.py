try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd =r'C:\pacotes\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open(r'c:\Users\806627771\Desktop\Desenvolvimento\prop_ocr\imagem.png'), lang='por'))
