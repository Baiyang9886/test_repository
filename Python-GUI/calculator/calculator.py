import sys
import os
from PyQt5.QtGui import QIcon
from QCandyUi import CandyWindow
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (QWidget,QApplication)
from app import Ui_Form
import math
#主界面窗口
class Calculator(QWidget,Ui_Form,QObject):
    # warning_signal = pyqtSignal(str,str)

    def __init__(self) -> object:           #-> object      #_xxx__：系统定义的特殊成员
        super(Calculator, self).__init__()       #分别调用了父类的初始化函数
        self.setupUi(self)     #UI界面控件的初始化
        self.show()
        self.last_result = 0          #该数据成员属于对象，用于存放上次的计算结果
        self.setWindowTitle("计算器")   #标题的设置
        # 图标文件的文件夹
        # current work directory
        print(os.getcwd())
        path = os.path.join(os.path.join(os.getcwd(), "icon"))  #
        print(path)
        path = os.path.join(path, "icon.ico")  # 在线转换 http://www.topdf.cn/img2icon
        print(path)
        icon = QIcon(path)
        self.setWindowIcon(icon)

        #关联按钮
        self.pus_0.clicked.connect(self.buttonClick)
        self.pus_1.clicked.connect(self.buttonClick)
        self.pus_2.clicked.connect(self.buttonClick)
        self.pus_3.clicked.connect(self.buttonClick)
        self.pus_4.clicked.connect(self.buttonClick)
        self.pus_5.clicked.connect(self.buttonClick)
        self.pus_6.clicked.connect(self.buttonClick)
        self.pus_7.clicked.connect(self.buttonClick)
        self.pus_8.clicked.connect(self.buttonClick)
        self.pus_9.clicked.connect(self.buttonClick)
        self.pus_Clear.clicked.connect(self.buttonClick)
        self.pus_Bck.clicked.connect(self.buttonClick)
        self.pus_devide.clicked.connect(self.buttonClick)
        self.pus_sub.clicked.connect(self.buttonClick)
        self.pus_equare.clicked.connect(self.buttonClick)
        self.pus_point.clicked.connect(self.buttonClick)
        self.pus_add.clicked.connect(self.buttonClick)
        self.pus_multi.clicked.connect(self.buttonClick)
        self.pus_Close.clicked.connect(self.buttonClick)
        self.pus_percentage.clicked.connect(self.buttonClick)
        self.pus_pingfanggen.clicked.connect(self.buttonClick)
        self.pus_cifang.clicked.connect(self.buttonClick)
        self.last_result = 0

    def buttonClick(self):         #定义一个函数，判断对应按钮点击并作出预设的动作
        pus = self.sender()
        try:
            if pus.objectName() == "pus_0":         #判断点击的是不是按钮0，是的话就进入这个判断语句
                text = self.lineEdit.text()          #读取文本编辑框的内容
                if text == "0" or text =="0.0":      #这里是计算器初始化为0，如若处于初始化状态可直接替换
                    text= "0"
                else:           #前面有数字则在文本加上一个数字
                    text += "0"
                self.lineEdit.setText(text)     #将更改后的文本写入在文本编辑框，显示出来

            if pus.objectName() == "pus_1":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "1"
                else:
                    text += "1"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_2":
                text = self.lineEdit.text()
                if text == "0" or text == "0.0":
                    text = "2"
                else:
                    text += "2"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_3":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "3"
                else:
                    text += "3"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_4":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "4"
                else:
                    text += "4"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_5":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "5"
                else:
                    text += "5"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_6":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "6"
                else:
                    text += "6"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_7":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "7"
                else:
                    text += "7"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_8":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "8"
                else:
                    text += "8"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_9":
                text = self.lineEdit.text()
                if text == "0" or text =="0.0":
                    text = "9"
                else:
                    text += "9"
                self.lineEdit.setText(text)

            if pus.objectName() == "pus_add":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    if "+" in text or "-" in text or "*" in text or "/" in text:
                        if "+" in text:
                            numbers_after_split = text.split("+")
                            self.last_result = float(numbers_after_split[0]) + float(numbers_after_split[1])
                        if "-" in text:
                            numbers_after_split = text.split("-")
                            self.last_result = float(numbers_after_split[0]) - float(numbers_after_split[1])
                        if "*" in text:
                            numbers_after_split = text.split("*")
                            self.last_result = float(numbers_after_split[0]) * float(numbers_after_split[1])
                        if "/" in text:
                            numbers_after_split = text.split("/")
                            self.last_result = float(numbers_after_split[0]) / float(numbers_after_split[1])
                        # 计算结束，把式子的结果显示到lineEdit
                        self.lineEdit.setText(str(self.last_result))

                     # 重新读取一遍文本框的内容，追加“*”
                    text = self.lineEdit.text()
                    text += "+"
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_point":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    text += "."
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_Clear":
                self.lineEdit.clear()
                self.lineEdit.setText("0")

            if pus.objectName() == "pus_Bck":
                text = self.lineEdit.text()
                print(text)
                if len(text) > 0:
                    new_text = text[0:-1]
                    self.lineEdit.setText(new_text)

            if pus.objectName() == "pus_sub":
                text = self.lineEdit.text()
                if text =="0":
                    text = "-"
                    self.lineEdit.setText(text)
                elif len(text) > 0 and text[-1].isnumeric():
                    if "+" in text or "-" in text or "*" in text or "/" in text:
                        if "+" in text:
                            numbers_after_split = text.split("+")
                            self.last_result = float(numbers_after_split[0]) + float(numbers_after_split[1])
                        if "-" in text:
                            numbers_after_split = text.split("-")
                            self.last_result = float(numbers_after_split[0]) - float(numbers_after_split[1])
                        if "*" in text:
                            numbers_after_split = text.split("*")
                            self.last_result = float(numbers_after_split[0]) * float(numbers_after_split[1])
                        if "/" in text:
                            numbers_after_split = text.split("/")
                            self.last_result = float(numbers_after_split[0]) / float(numbers_after_split[1])
                        #计算结束，把式子的结果显示到lineEdit
                        self.lineEdit.setText(str(self.last_result))

                        # 重新读取一遍文本框的内容，追加“*”
                    text = self.lineEdit.text()
                    text +="-"
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")
            if pus.objectName() == "pus_cifang":
                text = self.lineEdit.text()
                if len(text)>0 and text[-1].isnumeric():
                    if "^" in text:
                        print("erron")
                    else:
                        text += "^"
                        self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_multi":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    if "+" in text or "-" in text or "*" in text or "/" in text:
                        if "+" in text:
                             numbers_after_split = text.split("+")
                             self.last_result = float(numbers_after_split[0]) + float(numbers_after_split[1])
                        if "-" in text:
                            numbers_after_split = text.split("-")
                            self.last_result = float(numbers_after_split[0]) - float(numbers_after_split[1])
                        if "*" in text:
                            numbers_after_split = text.split("*")
                            self.last_result = float(numbers_after_split[0]) * float(numbers_after_split[1])
                        if "/" in text:
                            numbers_after_split = text.split("/")
                            self.last_result = float(numbers_after_split[0]) / float(numbers_after_split[1])
                        #计算结束，把式子的结果显示到lineEdit
                        self.lineEdit.setText(str(self.last_result))

                        #重新读取一遍文本框的内容，追加“*”
                    text = self.lineEdit.text()
                    text +="*"
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_Close":
                self.close()

            if pus.objectName() == "pus_devide":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    if "+" in text or "-" in text or "*" in text or "/" in text:
                        if "+" in text:
                            numbers_after_split = text.split("+")
                            self.last_result = float(numbers_after_split[0]) + float(numbers_after_split[1])
                        if "-" in text:
                            numbers_after_split = text.split("-")
                            self.last_result = float(numbers_after_split[0]) - float(numbers_after_split[1])
                        if "*" in text:
                            numbers_after_split = text.split("*")
                            self.last_result = float(numbers_after_split[0]) * float(numbers_after_split[1])
                        if "/" in text:
                            numbers_after_split = text.split("/")
                            self.last_result = float(numbers_after_split[0]) / float(numbers_after_split[1])
                        # 计算结束，把式子的结果显示到lineEdit
                        self.last_result.setText(str(self.last_result))

                        # 重新读取一遍文本框的内容，追加“*”
                    text = self.lineEdit.text()
                    text += "/"
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_pingfanggen":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    if len(text) == 1:
                        text_sqrt = math.sqrt(float(text))
                        self.lineEdit.setText(str(text_sqrt))
                        print(text_sqrt)
                    if len(text) >1 and text[-1].isnumeric():
                        text_sqrt = math.sqrt(float(text))
                        self.lineEdit.setText(str(text_sqrt))
                        print(text_sqrt)
                else:
                    print("前一位非数字，不处理")

            if pus.objectName() == "pus_percentage":
                text = self.lineEdit.text()
                if len(text) > 0 and text[-1].isnumeric():
                    text += "%"
                    self.lineEdit.setText(text)
                else:
                    print("前一位非数字，不处理")


            if pus.objectName() == "pus_equare":
                text = self.lineEdit.text()
                if "^" in text:
                    text_pow=text.split("^")
                    n_square = pow(float(text_pow[0]),float(text_pow[1]))         #计算次方根，pow()也是一种预定义方法，用于找出数字的幂，它以两个参数作为输入，第一个是数字本身，第二个是该数字的幂。
                    self.lineEdit.setText(str(n_square))
                result = self.calculate(self.lineEdit.text())
                self.lineEdit.setText(str(result))



        except Exception as ex:
            print(ex)
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))

    def calculate(self,num_str="1-(23*777/76/123*11/8*89)+83-91-(33*433/78*23)"):
        try:
            # 减法替换成加法
            num_str = num_str.replace('-', "+-", len(num_str))
            # 分离加法元素，得到多个乘除式子的元素
            list_after_split_add = num_str.split('+')
            # for item in list_after_split_add:
            #     print(item)
            # 1
            # -23 * 777 / 76 / 123 * 11 / 8 * 89 = -233.9498956996149
            # 83
            # -91
            # -33 * 433 / 78 * 23   = -4213.423076923077

            add_result = 0
            # 对每个式子都进行乘除法运算
            for item in list_after_split_add:
                """
                item可能的值为：
                1
                -23*777/76/123*11/8*89
                83
                -91
                -33*433/78*23
                """
                list_after_split_multi = item.split('*')
                # 第1个数作为因数，后面的全是因数
                multiplication_result = 1
                # 分割之后，每个i元素内只剩下除法运算
                for i in list_after_split_multi:
                    """
                    i可能的值为：
                    -23
                    777/76/123
                    11/8
                    89
                    """
                    # print(i)
                    list_after_split_division = i.split('/')
                    # 除式的结果
                    division_result = float(list_after_split_division[0])
                    # print("第1个数作为被除数，后面的全是除数", list_after_split_division[0], division_result)
                    if len(list_after_split_division) > 1:
                        for number in list_after_split_division[1:]:
                            # number = list_after_split_division[0]
                            """
                            number可能的值为：
                            777
                            76
                            123
                            """
                            division_result /= float(number)
                    # 打印每个除式的计算结果
                    # print(list_after_split_division, "每个除式的计算结果:", division_result)
                    # 将每个除式的结果作为乘式的因数，进行乘法计算
                    # print("之前的乘式结果multiplication_result=", multiplication_result, "因数division_result=", division_result)
                    multiplication_result *= division_result
                    # print("目前的乘式结果multiplication_result=", multiplication_result)
                print("之前的加式结果add_result=", add_result, "加数multiplication_result=", multiplication_result)
                add_result += multiplication_result
                print("目前的加式结果add_result=", add_result)
                print(add_result)
            return add_result
        except Exception as ex:
            print(ex)
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CandyWindow.createWindow(Calculator(), 'blue')
    ex.setWindowTitle('计算器')
    ex = Calculator()
    sys.exit(app.exec_())