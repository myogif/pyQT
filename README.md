#PYQT
## Requiremnet

install PySerial
`pip install pyserial`

#### install PyQt5
 `sudo apt-get install qttools5-dev-tools`

# Configuration Auto Start Program
`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`
### add the last line 
`@/usr/bin/python /home/pi/main.py`
