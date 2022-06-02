import pytesseract
import os


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    directory = input('Enter directory: ')
    for filename in os.listdir(directory):
        if filename.endswith('.png'):

            ocr_text = pytesseract.image_to_string(os.path.join(directory, filename))
            rsrp = ocr_text[ocr_text.find('RSRP')+5:ocr_text.find('RSRP')+14]
            rsrp = rsrp.replace(' ', '').replace('dBm', '').strip()
            rsrp = ''.join(i for i in rsrp if i.isdigit() or i == '-' or i == '.')

            rsrq = ocr_text[ocr_text.find('RSRQ')+5:ocr_text.find('RSRQ')+12]
            rsrq = rsrq.replace(' ', '').replace('dB', '').strip()
            rsrq = ''.join(i for i in rsrq if i.isdigit() or i == '-' or i == '.')

            rssnr = ocr_text[ocr_text.find('RSSNR')+6:ocr_text.find('RSSNR')+14]
            rssnr = rssnr.replace(' ', '').replace('dB', '').strip()
            rssnr = ''.join(i for i in rssnr if i.isdigit() or i == '-' or i == '.')

            if ocr_text.find('MTSMTS')!= -1:
                operator = 'MTS'
            elif ocr_text.find('Tele2') != -1:
                operator = 'Tele2'
            elif ocr_text.find('MegaFon') != -1:
                operator = 'MegaFon'
            elif ocr_text.find('Beeline') != -1:
                operator = 'Beeline'

            print(f'Mobile network,{operator},RSRP,{rsrp},RSRQ,{rsrq},RSSNR,{rssnr}')