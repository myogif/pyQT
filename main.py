import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication
from config import *
from Port import  customSerial
import netcore as nc

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Serial 
        self.serial = customSerial()
        self.ui.cb_BaudRate.addItems(self.serial.baudrateDIC.keys())
        self.ui.cb_BaudRate.setCurrentText('115200')
        self.update_ports()
        
        #Events
        self.ui.pb_Send.clicked.connect(self.send_data)
        self.ui.pb_Connect.clicked.connect(self.connect_serial)
        self.ui.pb_Refresh.clicked.connect(self.update_ports)
        self.ui.pb_Clear.clicked.connect(self.clear_window)
        self.serial.data_available.connect(self.update_terminal)
        
    def update_terminal(self, data):
        ID = self.ui.lineEdit_ID.text()
        IP = self.ui.lineEdit_IP.text()
        PORT = self.ui.lineEdit_Port.text()
        nc.sendUDP(data,ID, IP, PORT)
        data = data
        self.ui.txt_Result.append(data)
        #print(data);
    
    
    def connect_serial(self):
        if(self.ui.pb_Connect.isChecked()):
            port = self.ui.cb_Port.currentText()
            baud = self.ui.cb_BaudRate.currentText()
            self.serial.serialPort.port = port 
            self.serial.serialPort.baudrate = baud
            self.serial.connect_serial()
            
            if(self.serial.serialPort.is_open):
                self.ui.pb_Connect.setText("Disconnected")
            else:
                self.ui.pb_Connect.setChecked(False)
        else:
            self.serial.disconnect_serial()
            self.ui.pb_Connect.setText('Connected')
    
    def send_data(self):
        data = self.ui.lineEdit_ID.text()
        print(data);
        #self.serial.send_data(data)
        
    def update_ports(self):
        self.serial.update_ports()
        self.ui.cb_Port.clear()
        self.ui.cb_Port.addItems(self.serial.portList)
    
    def clear_window(self):
        self.ui.txt_Result.clear()
        
    def closeEvent(self, e):
        self.serial.disconnect_serial()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())