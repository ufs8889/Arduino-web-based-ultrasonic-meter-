import json
import serial
from time import sleep
from threading import Thread
from flask import *



app = Flask(__name__,template_folder="temp")
status = None


def task():
 global status 
 try: 
  arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
 except:
  arduino.close()
  arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.01)
 while True:
   try: 
    data = arduino.readline()
    status =(data.strip()).decode() 
   except:
    sleep(0.01)
    data = arduino.readline()
    status = data.strip().decode()


@app.route('/')
def index():
  t1 = Thread(target=task)
  t1.start()
  return render_template('dynamic_page.html')
  

@app.route('/status', methods=['GET'])
def getStatus():
  statusList = {'status':status}
  return json.dumps(statusList)




if __name__ == '__main__':
  app.run(debug=True)