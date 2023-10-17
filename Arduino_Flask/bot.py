import cv2
import time
import telebot
import pytesseract
from telebot import types
from datetime import datetime
from selenium import webdriver

now = datetime.now() 
bot = telebot.TeleBot('6201292411:AAER7Y4UlCHVFKx1Fuh6KMasWjYUtM8wYhg')


def taken_picture():
  browser = webdriver.Chrome()
  browser.get('http://127.0.0.1:5000')
  path = r'C:\Users\Siroca\Desktop\icon\img\screenie.png'
  browser.save_screenshot(path)
  browser.quit()
  return path
 

def img_text():
  img = cv2.imread(r'C:\Users\Siroca\Desktop\icon\img\screenie.png')
  config = ('-l eng --oem 1 --psm 3')
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  text  = pytesseract.image_to_string(img, config=config)
  return text.strip()  


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.chat.id
    bot.send_message(message.chat.id, 'Hello World')
    time.sleep(10)
    path = taken_picture()
    img = open(path, 'rb')
    bot.delete_message(message.chat.id, message.message_id + 1)
    bot.send_message(user_id,img_text())
    bot.send_photo(user_id,img,caption=now.strftime("%d/%m/%Y %H:%M:%S"))
   

bot.infinity_polling()    