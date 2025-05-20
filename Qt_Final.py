from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 341)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 175, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 175, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 175, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Encript = QtWidgets.QWidget()
        self.Encript.setObjectName("Encript")
        self.Input1 = QtWidgets.QLineEdit(self.Encript)
        self.Input1.setGeometry(QtCore.QRect(0, 40, 491, 26))
        self.Input1.setObjectName("Input1")
        self.Input2 = QtWidgets.QLineEdit(self.Encript)
        self.Input2.setGeometry(QtCore.QRect(0, 100, 491, 26))
        self.Input2.setObjectName("Input2")
        self.Result1 = QtWidgets.QPushButton(self.Encript)
        self.Result1.setGeometry(QtCore.QRect(0, 190, 491, 26))
        self.Result1.setObjectName("Result1")
        self.tabWidget.addTab(self.Encript, "")
        self.Dencript_pic = QtWidgets.QWidget()
        self.Dencript_pic.setObjectName("Dencript_pic")
        self.Input3 = QtWidgets.QLineEdit(self.Dencript_pic)
        self.Input3.setGeometry(QtCore.QRect(0, 60, 491, 26))
        self.Input3.setObjectName("Input3")
        self.Result2 = QtWidgets.QPushButton(self.Dencript_pic)
        self.Result2.setGeometry(QtCore.QRect(0, 140, 491, 26))
        self.Result2.setObjectName("Result2")
        self.tabWidget.addTab(self.Dencript_pic, "")
        self.Dencript_str = QtWidgets.QWidget()
        self.Dencript_str.setObjectName("Dencript_str")
        self.Input4 = QtWidgets.QLineEdit(self.Dencript_str)
        self.Input4.setGeometry(QtCore.QRect(10, 40, 341, 51))
        self.Input4.setObjectName("Input4")
        self.Input5 = QtWidgets.QLineEdit(self.Dencript_str)
        self.Input5.setGeometry(QtCore.QRect(10, 160, 341, 51))
        self.Input5.setObjectName("Input5")
        self.Result3 = QtWidgets.QPushButton(self.Dencript_str)
        self.Result3.setGeometry(QtCore.QRect(360, 10, 131, 231))
        self.Result3.setObjectName("Result3")
        self.tabWidget.addTab(self.Dencript_str, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQT_Help = QtWidgets.QAction(MainWindow)
        self.actionQT_Help.setObjectName("actionQT_Help")
        self.actionPython_Help = QtWidgets.QAction(MainWindow)
        self.actionPython_Help.setObjectName("actionPython_Help")
        self.actionAbout_CyberSecurity = QtWidgets.QAction(MainWindow)
        self.actionAbout_CyberSecurity.setObjectName("actionAbout_CyberSecurity")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Input1.setText(_translate("MainWindow", "Input First Image:"))
        self.Input2.setText(_translate("MainWindow", "Input Second Image:"))
        self.Result1.setText(_translate("MainWindow", "&Get Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Encript), _translate("MainWindow", "Encript"))
        self.Input3.setText(_translate("MainWindow", "Input Key Image:"))
        self.Result2.setText(_translate("MainWindow", "&Get Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dencript_pic), _translate("MainWindow", "Dencript_pic"))
        self.Input4.setText(_translate("MainWindow", "Input Result Image:"))
        self.Input5.setText(_translate("MainWindow", "Input Length As Key:"))
        self.Result3.setText(_translate("MainWindow", "&Get Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dencript_str), _translate("MainWindow", "Dencript_str"))
        self.actionNew.setText(_translate("MainWindow", "&New..."))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave_as.setText(_translate("MainWindow", "&Save as"))
        self.actionClose.setText(_translate("MainWindow", "&Close"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQT_Help.setText(_translate("MainWindow", "QT Help"))
        self.actionPython_Help.setText(_translate("MainWindow", "Python Help"))
        self.actionAbout_CyberSecurity.setText(_translate("MainWindow", "About CyberSecurity"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.Result1.clicked.connect(self.encoding)
        self.Result2.clicked.connect(self.decoding_pic)
        self.Result3.clicked.connect(self.decoding_str)
    def encoding(self):
        import cv2
        import numpy as np
        from PIL import Image
        # photosize0=1920
        # photosize1=1080
        global keysize
        global imgsize
        keysize = [1920, 270]
        imgsize = [1920, 1080]
        def str_to_binary(string):
            binary_list = []
            for char in string:
                binary_list.append(bin(ord(char))[2:].zfill(8))
            return ''.join(binary_list)
        def check_path(path):
            if 'png' in path:
                return True
            else:return False
        def check_size(image_path):
            photo = Image.open(image_path).convert('RGB')
            if photo.size[1]==1080 and photo.size[0]==1920:
                return True,True
            else:
                photo1=cv2.imread(image_path)
                a=cv2.resize(photo1,(int(imgsize[0]),(int(imgsize[1]))))
                return False,a
        Fist_Image_Path = self.Input1.text()
        Second_Image_Path = self.Input2.text()
        str_im1=Fist_Image_Path
        str_im2=Second_Image_Path
        if (check_size(Fist_Image_Path)[0] != True):

            cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\Catch\edited1.png', check_size(Fist_Image_Path)[1])
            str_im1 = r'C:\Users\ASUS\Desktop\Steganography\Catch\edited1.png'
        if check_path(str_im2)==True:
            if (check_size(Second_Image_Path)[0] !=True):
                cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\Catch\edited2.png', check_size(Second_Image_Path)[1])
                str_im2=r'C:\Users\ASUS\Desktop\Steganography\Catch\edited2.png'
        else:
            bin_new=str_to_binary(str_im2)
            if len(bin_new)>(imgsize[0]*imgsize[1]):
                print("not valid")
                bin_new = str_to_binary("not valid")
            else:print("your key is:",len(bin_new))
        #NOTE:PYQT would only allow len of 262136 charecters to be entered about 32767 charecters so that else is always true
        #Max key is 262136 | Max Char is: 32767
        ################################
        def pix_file(arr):
            f = open("pixeldata.txt", "x")
            f.write(str(arr))
            f.close()
        def dec_to_bin(x):
            return int(bin(x)[2:])
        def bin_to_dec(arr):
            for i in range(0, len(arr)):
                arr[i] = eval('0b' + str(arr[i]))
            return arr
        def get_pixel(image_path):
            photo = Image.open(image_path).convert('RGB')
            arr = []  # photo.size[0]=1920,photo.size[1]=1080
            for y in range(0, photo.size[1]):
                for x in range(0, photo.size[0]):
                    R, G, B = photo.getpixel((x, y))  # GrayScale equal
                    arr.append(dec_to_bin(R))
            return arr
        def removal(arr):
            for i in range(0, len(arr)):
                arr[i] = int(arr[i] / 100)
                arr[i] = arr[i] * 100
            return arr
        def oneDtotwoD(size, oneDarray):
            twoDarray = np.reshape(oneDarray, (-1, size))
            return twoDarray
        def rgb_to_image(size, image_bites):
            oneDarraybase = np.array(image_bites)
            twoDarray = oneDtotwoD(size, bin_to_dec(oneDarraybase))
            return twoDarray
        def img_reduction(arr):
            new_arr = []
            for i in range(0, len(arr)):  # len=129600=480*270
                str_numi=str(int(arr[i]+11111111))
                new_arr.append(int(int(str_numi[0:2])-11))
                new_arr.append(int(int(str_numi[2:4])-11))
                new_arr.append(int(int(str_numi[4:6])-11))
                new_arr.append(int(int(str_numi[6:])-11))
            #pix_file(new_arr)
            return new_arr
        def combine(onerecovery, tworecovery):
            resultpic = []
            for i in range(0, len(onerecovery)):
                resultpic.append(onerecovery[i] + tworecovery[i])
            return oneDtotwoD(imgsize[0], np.array(resultpic))
        def reshape_reduction(image_path):
            image = cv2.imread(image_path)
            key1= cv2.resize(image, (int(imgsize[0] / 1), int(imgsize[1] / 4)))
            cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\Catch\key1.png', key1)
            return r'C:\Users\ASUS\Desktop\Steganography\Catch\key1.png'
        def combine_str(onerecovery, tworecovery):
            resultpic=[]
            tworec = []
            j=0
            for i in range(0,int(len(tworecovery)),2):
                tworec.append(int(tworecovery[i:i+2]))
            tworecnp=np.array(tworec)
            for i in range(0,int(int(len(onerecovery))-int(len(tworecovery)/2))):
                while(j< int(len(tworecovery)/2)):
                    resultpic.append(tworecnp[j]+onerecovery[j]) # onerecovery[j]+x[j]
                    j=j+1
                resultpic.append(onerecovery[i+j])
            return oneDtotwoD(imgsize[0],rgb_to_image(imgsize[0], np.array(resultpic)))
        #pix_file(rgb_to_image(imgsize[0],get_pixel(str(str_im2))))
        if check_path(str_im2) == True:
            onerecovery = rgb_to_image(imgsize[0], removal(get_pixel(str(str_im1))))
            tworecovery = rgb_to_image(keysize[0], img_reduction(get_pixel(reshape_reduction(str(str_im2)))))
            result = combine(onerecovery, tworecovery)
        else:
            onerecovery = (removal(get_pixel(str(str_im1))))
            tworecovery=(bin_new)
            result=combine_str(onerecovery,tworecovery)
        cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\result\result.png', result)
        im=Image.open(r'C:\Users\ASUS\Desktop\Steganography\result\result.png')
        im.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()  # free all memory
    def decoding_pic(self):
        import cv2
        import numpy as np
        from PIL import Image
        # photosize0=1920
        # photosize1=1080
        global keysize
        global imgsize
        keysize = [1920, 270]
        imgsize = [1920, 1080]
        Result_Image_Path = self.Input3.text()
        ################################
        def pix_file(arr):
            f = open("pixeldata.txt", "x")
            f.write(str(arr))
            f.close()
        def dec_to_bin(x):
            return int(bin(x)[2:])
        def bin_to_dec(arr):
            for i in range(0, len(arr)):
                arr[i] = eval('0b' + str(arr[i]))
            return arr
        def get_pixel(image_path):
            photo = Image.open(image_path).convert('RGB')
            arr = []  # photo.size[0]=1920,photo.size[1]=1080
            for y in range(0, photo.size[1]):
                for x in range(0, photo.size[0]):
                    R, G, B = photo.getpixel((x, y))  # GrayScale equal
                    arr.append(dec_to_bin(R))
            return arr
        def oneDtotwoD(size, oneDarray):
            twoDarray = np.reshape(oneDarray, (-1, size))
            return twoDarray
        def twoDtooneD(size0, size1, twoDarray):
            # photo = Image.open(image_path).convert('RGB')
            arr = []
            for i in range(0, size1):
                for j in range(0, size0):
                    arr.append(twoDarray[i][j])
            return arr
        def rgb_to_image(size, image_bites):
            oneDarraybase = np.array(image_bites)
            twoDarray = oneDtotwoD(size, bin_to_dec(oneDarraybase))
            return twoDarray
        def reshape_promotion(image_path):
            img=cv2.imread(image_path)
            key2=cv2.resize(img,(int(imgsize[0]),int(imgsize[1])))
            return key2
        def encoding(image_result):
            new_arr=[]
            resultpic=rgb_to_image(imgsize[0],(get_pixel((image_result))))
            image_result1 = twoDtooneD(imgsize[0], imgsize[1],resultpic)
            for i in range(0, len(image_result1), 4):
                x = int((dec_to_bin(image_result1[i])) % 100)
                y = int((dec_to_bin(image_result1[i + 1])) % 100)
                q = int((dec_to_bin(image_result1[i + 2])) % 100)
                z = int((dec_to_bin(image_result1[i + 3])) % 100)
                t = (x * 1000000 + y *10000 + q * 100 + z * 1)
                new_arr.append(t)
            #pix_file(new_arr)
            cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\Catch\encript.png', (rgb_to_image(keysize[0], new_arr)))
            img=reshape_promotion(r'C:\Users\ASUS\Desktop\Steganography\Catch\encript.png')
            cv2.imwrite(r'C:\Users\ASUS\Desktop\Steganography\result\encript.png',img)
            return oneDtotwoD(imgsize[0], new_arr)
        encoding(Result_Image_Path)
        #pix_file(encoding(Result_Image_Path))
        im=Image.open(r'C:\Users\ASUS\Desktop\Steganography\result\encript.png')
        im.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()  # free all memory
    def decoding_str(self):
        import cv2
        import numpy as np
        from PIL import Image
        # photosize0=1920
        # photosize1=1080
        global keysize
        global imgsize
        keysize = [1920, 270]
        imgsize = [1920, 1080]
        Fist_Image_Path = self.Input4.text()
        Second_Image_Path = self.Input5.text()
        str_im1=Fist_Image_Path
        str_im2=(Second_Image_Path)
        def BinaryToDecimal(binary):
            string = int(binary, 2)
            return string
        def binary_to_str(bin_data):
            str_data = ''
            for i in range(0, len(bin_data), 8):
                temp_data = bin_data[i:i + 8]
                decimal_data = BinaryToDecimal(temp_data)
                str_data = str_data + chr(decimal_data)
            return str_data
        def dec_to_bin(x):
            return int(bin(x)[2:])
        def bin_to_dec(arr):
            for i in range(0, len(arr)):
                arr[i] = eval('0b' + str(arr[i]))
            return arr
        def get_pixel(image_path):
            photo = Image.open(image_path).convert('RGB')
            arr = []  # photo.size[0]=1920,photo.size[1]=1080
            for y in range(0, photo.size[1]):
                for x in range(0, photo.size[0]):
                    R, G, B = photo.getpixel((x, y))  # GrayScale equal
                    arr.append(dec_to_bin(R))
            return arr
        def oneDtotwoD(size, oneDarray):
            twoDarray = np.reshape(oneDarray, (-1, size))
            return twoDarray
        def twoDtooneD(size0, size1, twoDarray):
            # photo = Image.open(image_path).convert('RGB')
            arr = []
            for i in range(0, size1):
                for j in range(0, size0):
                    arr.append(twoDarray[i][j])
            return arr
        def rgb_to_image(size, image_bites):
            oneDarraybase = np.array(image_bites)
            twoDarray = oneDtotwoD(size, bin_to_dec(oneDarraybase))
            return twoDarray
        def encoding(Result,int_First):
            res_str=''
            resultpic=rgb_to_image(imgsize[0],(get_pixel((Result))))
            image_result1 = twoDtooneD(imgsize[0], imgsize[1],resultpic)
            for i in range(0,int(int(int_First)/2)):
                str_numi=(dec_to_bin(image_result1[i]))
                res=str_numi%100
                if res==1:
                    res=str('01')
                if res==0:
                    res=str('00')
                if res==11:
                    res=str('11')
                if res==10:
                    res=str('10')
                res_str=res_str+(res)
            return res_str
        res_str=(encoding(str_im1,str_im2))
        print(res_str)
        print("res:",binary_to_str(res_str))
        #pix_file(encoding(Result_Image_Path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()  # free all memory

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())