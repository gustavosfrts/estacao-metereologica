# estacao-metereologica
Estação meteorológica feito com sensores conectados ao Raspbarry, e um web service em Django.

##Comandos necessários para rodar o projeto

pip install apscheduler django requests

###dht11
sudo apt-get install git build-essential python-dev
\
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
\
cd Adafruit_Python_DHT
\
sudo python setup.py install

###bmp280
sudo pip install bmp280
\
git clone https://github.com/pimoroni/bmp280-python
\
cd bmp280-python
\
sudo ./install.sh


##Links de referência:
https://blog.fazedores.com/temperatura-com-dht11-e-raspberry-pi/
\
https://www.iotstarters.com/configuring-bmp280-sensor-with-raspberry-pi/#:~:text=The%20BMP280%20module%20is%20one,between%20300%20to%201100%20hPa
\
https://openweathermap.org