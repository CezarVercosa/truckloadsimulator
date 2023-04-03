from PyQt5 import QtCore, QtGui, QtWidgets

        #classe da UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_frame = QtWidgets.QFrame(self.centralwidget)
        self.app_frame.setGeometry(QtCore.QRect(0, 0, 981, 601))
        self.app_frame.setStyleSheet("background-color:#191a24;")
        self.app_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_frame.setObjectName("app_frame")
        self.close_and_minimize_frame = QtWidgets.QFrame(self.app_frame)
        self.close_and_minimize_frame.setGeometry(QtCore.QRect(0, 0, 981, 25))
        self.close_and_minimize_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.close_and_minimize_frame.setStyleSheet("background-color: #393c4f;")
        self.close_and_minimize_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_and_minimize_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_and_minimize_frame.setObjectName("close_and_minimize_frame")
        self.close_label = QtWidgets.QLabel(self.close_and_minimize_frame)
        self.close_label.setGeometry(QtCore.QRect(940, 2, 21, 21))
        self.close_label.setText("")
        self.close_label.setPixmap(QtGui.QPixmap("imgs/closebtn.png"))
        self.close_label.setScaledContents(True)
        self.close_label.setObjectName("close_label")
        self.minimize_label = QtWidgets.QLabel(self.close_and_minimize_frame)
        self.minimize_label.setGeometry(QtCore.QRect(907, 3, 21, 21))
        self.minimize_label.setText("")
        self.minimize_label.setPixmap(QtGui.QPixmap("imgs/minimize_btn.png"))
        self.minimize_label.setScaledContents(True)
        self.minimize_label.setObjectName("minimize_label")
        self.close_button = QtWidgets.QPushButton(self.close_and_minimize_frame)
        self.close_button.setGeometry(QtCore.QRect(940, 2, 21, 21))
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.close_button.setAutoFillBackground(False)
        self.close_button.setStyleSheet("background-color: transparent;")
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")
        self.minimize_button = QtWidgets.QPushButton(self.close_and_minimize_frame)
        self.minimize_button.setGeometry(QtCore.QRect(907, 3, 21, 21))
        self.minimize_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.minimize_button.setAutoFillBackground(False)
        self.minimize_button.setStyleSheet("background-color: transparent;")
        self.minimize_button.setText("")
        self.minimize_button.setObjectName("minimize_button")
        self.header_frame = QtWidgets.QFrame(self.app_frame)
        self.header_frame.setGeometry(QtCore.QRect(0, 28, 981, 61))
        self.header_frame.setStyleSheet("background-color: #12151c;")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.consulte_cadastre_button = QtWidgets.QPushButton(self.header_frame)
        self.consulte_cadastre_button.setGeometry(QtCore.QRect(62, 15, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(1)
        self.consulte_cadastre_button.setFont(font)
        self.consulte_cadastre_button.setStyleSheet("color: white; font-size: 20px; border: none;")
        self.consulte_cadastre_button.setObjectName("consulte_cadastre_button")
        self.registered_button = QtWidgets.QPushButton(self.header_frame)
        self.registered_button.setGeometry(QtCore.QRect(348, 15, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(1)
        self.registered_button.setFont(font)
        self.registered_button.setStyleSheet("color: white; font-size: 20px; border: none;")
        self.registered_button.setObjectName("registered_button")
        self.black_frame = QtWidgets.QFrame(self.app_frame)
        self.black_frame.setGeometry(QtCore.QRect(-10, 26, 991, 5))
        self.black_frame.setStyleSheet("background-color: black;")
        self.black_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.black_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.black_frame.setObjectName("black_frame")
        self.content_frame = QtWidgets.QFrame(self.app_frame)
        self.content_frame.setGeometry(QtCore.QRect(0, 90, 981, 511))
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.origin_box = QtWidgets.QComboBox(self.content_frame)
        self.origin_box.setGeometry(QtCore.QRect(60, 50, 185, 25))
        self.origin_box.setStyleSheet("#origin_box{\n"
                "    padding-left: 10px;\n"
                "    background-color: #12151c;\n"
                "    color:white;\n"
                "    selection-background-color: transparent;\n"
                "\n"
                "}\n"
                "#origin_box::drop-down{\n"
                "    border: none;\n"
                "}\n"
                "\n"
                "#origin_box::down-arrow{\n"
                "    image: url(imgs/expand-button.ico);\n"
                "    width: 12px;\n"
                "    height: 12px;\n"
                "    margin-right: 15px;\n"
                "    margin-top: 4px\n"
                "}\n"
                "\n"
                "QComboBox:items{\n"
                "    color: white;\n"
                "}\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: #4d4d4d;\n"
                "}\n"
                "\n"
                "QListView{\n"
                "    color: white;\n"
                "}\n"
                "\n"
                "#origin_box QListView:item:hover{\n"
                "    color: white;\n"
                "}\n"
                "\n"
                "")
        self.origin_box.setObjectName("origin_box")
        self.origin_text = QtWidgets.QLabel(self.content_frame)
        self.origin_text.setGeometry(QtCore.QRect(65, 28, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.origin_text.setFont(font)
        self.origin_text.setStyleSheet("color: white;")
        self.origin_text.setAlignment(QtCore.Qt.AlignCenter)
        self.origin_text.setObjectName("origin_text")
        self.destiny_box = QtWidgets.QComboBox(self.content_frame)
        self.destiny_box.setGeometry(QtCore.QRect(60, 120, 185, 25))
        self.destiny_box.setStyleSheet("#destiny_box{\n"
                "    padding-left: 10px;\n"
                "    background-color: #12151c;\n"
                "    color: white;\n"
                "selection-background-color: transparent;\n"
                "    \n"
                "\n"
                "}\n"
                "#destiny_box::drop-down{\n"
                "    border: none;\n"
                "}\n"
                "\n"
                "#destiny_box::down-arrow{\n"
                "    image: url(imgs/expand-button.ico);\n"
                "    width: 12px;\n"
                "    height: 12px;\n"
                "    margin-right: 15px;\n"
                "    margin-top: 4px\n"
                "\n"
                "}\n"
                "\n"
                "QComboBox:items{\n"
                "    color: white;\n"
                "}\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: #4d4d4d;\n"
                "}\n"
                "\n"
                "QListView{\n"
                "    color: white;\n"
                "}")
        self.destiny_box.setObjectName("destiny_box")
        self.destiny_text = QtWidgets.QLabel(self.content_frame)
        self.destiny_text.setGeometry(QtCore.QRect(67, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.destiny_text.setFont(font)
        self.destiny_text.setStyleSheet("color: white;")
        self.destiny_text.setAlignment(QtCore.Qt.AlignCenter)
        self.destiny_text.setObjectName("destiny_text")
        self.stop_box = QtWidgets.QComboBox(self.content_frame)
        self.stop_box.setGeometry(QtCore.QRect(60, 183, 185, 25))
        self.stop_box.setStyleSheet("#stop_box{\n"
                "    padding-left: 10px;\n"
                "    background-color: #12151c;\n"
                "    color: white;\n"
                "selection-background-color: transparent;\n"
                "\n"
                "}\n"
                "#stop_box::drop-down{\n"
                "    border: none;\n"
                "}\n"
                "\n"
                "#stop_box::down-arrow{\n"
                "    image: url(imgs/expand-button.ico);\n"
                "    width: 12px;\n"
                "    height: 12px;\n"
                "    margin-right: 15px;\n"
                "    margin-top: 4px\n"
                "\n"
                "}\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: #4d4d4d;\n"
                "}\n"
                "\n"
                "QComboBox:items{\n"
                "    color: white;\n"
                "}\n"
                "\n"
                "QListView{\n"
                "    color: white;\n"
                "}")
        self.stop_box.setObjectName("stop_box")
        self.stop_text = QtWidgets.QLabel(self.content_frame)
        self.stop_text.setGeometry(QtCore.QRect(65, 163, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stop_text.setFont(font)
        self.stop_text.setStyleSheet("color: white;")
        self.stop_text.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_text.setObjectName("stop_text")
        self.truck_box = QtWidgets.QComboBox(self.content_frame)
        self.truck_box.setGeometry(QtCore.QRect(60, 288, 185, 25))
        self.truck_box.setStyleSheet("#truck_box{\n"
                "    padding-left: 10px;\n"
                "    background-color: #12151c;\n"
                "    color: white;\n"
                "selection-background-color: transparent;\n"
                "\n"
                "}\n"
                "#truck_box::drop-down{\n"
                "    border: none;\n"
                "}\n"
                "\n"
                "#truck_box::down-arrow{\n"
                "    image: url(imgs/expand-button.ico);\n"
                "    width: 12px;\n"
                "    height: 12px;\n"
                "    margin-right: 15px;\n"
                "    margin-top: 4px\n"
                "\n"
                "}\n"
                "\n"
                "QComboBox:items{\n"
                "    color: white;\n"
                "}\n"
                "QComboBox QAbstractItemView {\n"
                "    selection-background-color: #4d4d4d;\n"
                "}\n"
                "\n"
                "QListView{\n"
                "    color: white;\n"
                "}")
        self.truck_box.setObjectName("truck_box")
        self.truck_text = QtWidgets.QLabel(self.content_frame)
        self.truck_text.setGeometry(QtCore.QRect(69, 266, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.truck_text.setFont(font)
        self.truck_text.setStyleSheet("color: white;")
        self.truck_text.setAlignment(QtCore.Qt.AlignCenter)
        self.truck_text.setObjectName("truck_text")

        self.warning_box = QtWidgets.QLabel(self.content_frame)
        self.warning_box.setObjectName("warning_box")
        self.warning_box.setGeometry(QtCore.QRect(6, 396, 301, 20))
        self.warning_box.setFont(font)
        self.warning_box.setStyleSheet("color: red;")
        self.warning_box.setAlignment(QtCore.Qt.AlignHCenter)

        self.consulte_button = QtWidgets.QPushButton(self.content_frame)
        self.consulte_button.setGeometry(QtCore.QRect(89, 426, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(14)
        self.consulte_button.setFont(font)
        self.consulte_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.consulte_button.setStyleSheet("color: white; background-color: #12151c; border-radius: 5px; border: 1px solid;")
        self.consulte_button.setObjectName("consulte_button")
        self.separation_frame = QtWidgets.QFrame(self.content_frame)
        self.separation_frame.setGeometry(QtCore.QRect(309, 24, 2, 460))
        self.separation_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0.1)")
        self.separation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.separation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separation_frame.setObjectName("separation_frame")
        self.separation_frame_2 = QtWidgets.QFrame(self.content_frame)
        self.separation_frame_2.setGeometry(QtCore.QRect(663, 24, 2, 460))
        self.separation_frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 0.1)")
        self.separation_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.separation_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separation_frame_2.setObjectName("separation_frame_2")
        self.price_text = QtWidgets.QLabel(self.content_frame)
        self.price_text.setGeometry(QtCore.QRect(457, 86, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.price_text.setFont(font)
        self.price_text.setStyleSheet("color: white;")
        self.price_text.setAlignment(QtCore.Qt.AlignCenter)
        self.price_text.setObjectName("price_text")
        self.price_box = QtWidgets.QLabel(self.content_frame)
        self.price_box.setGeometry(QtCore.QRect(438, 111, 101, 31))
        self.price_box.setStyleSheet("background-color: #12151c; border: 1px solid; color: white")
        self.price_box.setText("")
        self.price_box.setAlignment(QtCore.Qt.AlignCenter)
        self.price_box.setObjectName("price_box")
        self.distance_text = QtWidgets.QLabel(self.content_frame)
        self.distance_text.setGeometry(QtCore.QRect(454, 179, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.distance_text.setFont(font)
        self.distance_text.setStyleSheet("color: white;")
        self.distance_text.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_text.setObjectName("distance_text")
        self.distance_box = QtWidgets.QLabel(self.content_frame)
        self.distance_box.setGeometry(QtCore.QRect(438, 207, 101, 31))
        self.distance_box.setStyleSheet("background-color: #12151c; border: 1px solid; color: white;")
        self.distance_box.setText("")
        self.distance_box.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_box.setObjectName("distance_box")
        self.item_text = QtWidgets.QLabel(self.content_frame)
        self.item_text.setGeometry(QtCore.QRect(741, 27, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.item_text.setFont(font)
        self.item_text.setStyleSheet("color: white;")
        self.item_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_text.setObjectName("item_text")
        self.regex = QtCore.QRegExp("[a-zA-Z]+")
        self.strValidator = QtGui.QRegExpValidator(self.regex)
        self.item_box = QtWidgets.QLineEdit(self.content_frame)
        self.item_box.setGeometry(QtCore.QRect(735, 50, 171, 25))
        self.item_box.setStyleSheet("#item_box{\n"
                "    border-top: 0.5px solid;\n"
                "    border-left: 0.5px solid;\n"
                "    background-color: #12161C;\n"
                "    padding-left: 10px;\n"
                "    color: rgb(255,255,255);\n"
                "\n"
                "}")
        self.item_box.setObjectName("item_box")
        self.item_box.setValidator(self.strValidator)
        self.quantity_text = QtWidgets.QLabel(self.content_frame)
        self.quantity_text.setGeometry(QtCore.QRect(745, 95, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.intValidator = QtGui.QIntValidator()
        self.quantity_text.setFont(font)
        self.quantity_text.setStyleSheet("color: white;")
        self.quantity_text.setAlignment(QtCore.Qt.AlignCenter)
        self.quantity_text.setObjectName("quantity_text")
        self.quantity_box = QtWidgets.QLineEdit(self.content_frame)
        self.quantity_box.setGeometry(QtCore.QRect(736, 120, 171, 25))
        self.quantity_box.setStyleSheet("#quantity_box{\n"
                "    border-top: 0.5px solid;\n"
                "    border-left: 0.5px solid;\n"
                "    background-color: #12161C;\n"
                "    padding-left: 10px;\n"
                "    color: rgb(255,255,255);\n"
                "\n"
                "}")
        self.quantity_box.setObjectName("quantity_box")
        self.quantity_box.setValidator(self.intValidator)
        self.register_button = QtWidgets.QPushButton(self.content_frame)
        self.register_button.setGeometry(QtCore.QRect(762, 426, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(14)
        self.register_button.setFont(font)
        self.register_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.register_button.setStyleSheet("color: white; background-color: #12151c; border-radius: 5px; border: 1px solid;")
        self.register_button.setObjectName("register_button")
        self.item_cadastre_button = QtWidgets.QPushButton(self.content_frame)
        self.item_cadastre_button.setGeometry(QtCore.QRect(770, 254, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(14)
        self.item_cadastre_button.setFont(font)
        self.item_cadastre_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.item_cadastre_button.setStyleSheet("color: white; background-color: #12151c; border-radius: 5px; border: 1px solid;")
        self.item_cadastre_button.setObjectName("item_cadastre_button")
        self.confirme_item_text = QtWidgets.QLabel(self.content_frame)
        self.confirme_item_text.setGeometry(QtCore.QRect(667, 224, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.confirme_item_text.setFont(font)
        self.confirme_item_text.setStyleSheet("color: red;")
        self.confirme_item_text.setText("")
        self.confirme_item_text.setAlignment(QtCore.Qt.AlignCenter)
        self.confirme_item_text.setObjectName("confirme_item_text")
        self.weight_box = QtWidgets.QLineEdit(self.content_frame)
        self.weight_box.setGeometry(QtCore.QRect(736, 183, 171, 25))
        self.weight_box.setStyleSheet("#weight_box{\n"
                "    border-top: 0.5px solid;\n"
                "    border-left: 0.5px solid;\n"
                "    background-color: #12161C;\n"
                "    padding-left: 10px;\n"
                "    color: rgb(255,255,255);\n"
                "\n"
                "}")
        self.weight_box.setObjectName("weight_box")
        self.weight_box.setValidator(self.intValidator)
        self.weight_text = QtWidgets.QLabel(self.content_frame)
        self.weight_text.setGeometry(QtCore.QRect(747, 160, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.weight_text.setFont(font)
        self.weight_text.setStyleSheet("color: white;")
        self.weight_text.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_text.setObjectName("weight_text")
        self.itemScroll = QtWidgets.QScrollArea(self.content_frame)
        self.itemScroll.setGeometry(QtCore.QRect(691, 292, 261, 121))
        self.itemScroll.setStyleSheet("border: 0.5px solid rgba(128, 128, 128, 0.1);")
        self.itemScroll.setWidgetResizable(True)
        self.itemScroll.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.itemScroll.setObjectName("itemScroll")
        self.itemScrollWidgetContents = QtWidgets.QWidget()
        self.itemScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 119))
        self.itemScrollWidgetContents.setObjectName("itemScrollWidgetContents")
        self.verticalItemLayout = QtWidgets.QVBoxLayout(self.itemScrollWidgetContents)
        self.verticalItemLayout.setObjectName("verticalItemLayout")
        self.itemScroll.setWidget(self.itemScrollWidgetContents)
        self.pop_up_frame = QtWidgets.QFrame(self.content_frame)
        self.pop_up_frame.setGeometry(QtCore.QRect(190, 40, 661, 351))
        self.pop_up_frame.setStyleSheet("background-color: rgb(25,26,36);\n"
        "")
        self.pop_up_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pop_up_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pop_up_frame.setObjectName("pop_up_frame")
        self.pop_up_city_stop_text = QtWidgets.QLabel(self.pop_up_frame)
        self.pop_up_city_stop_text.setGeometry(QtCore.QRect(132, 22, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.pop_up_city_stop_text.setFont(font)
        self.pop_up_city_stop_text.setStyleSheet("color: white;")
        self.pop_up_city_stop_text.setAlignment(QtCore.Qt.AlignCenter)
        self.pop_up_city_stop_text.setObjectName("pop_up_city_stop_text")
        self.pop_up_scroll = QtWidgets.QScrollArea(self.pop_up_frame)
        self.pop_up_scroll.setGeometry(QtCore.QRect(125, 71, 411, 181))
        self.pop_up_scroll.setStyleSheet("border: none;")
        self.pop_up_scroll.setWidgetResizable(True)
        self.pop_up_scroll.setObjectName("pop_up_scroll")
        self.pop_up_scroll_WidgetContents = QtWidgets.QWidget()
        self.pop_up_scroll_WidgetContents.setGeometry(QtCore.QRect(0, 0, 411, 181))
        self.pop_up_scroll_WidgetContents.setObjectName("pop_up_scroll_WidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pop_up_scroll_WidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pop_up_scroll.setWidget(self.pop_up_scroll_WidgetContents)
        self.confirme_stop_button = QtWidgets.QPushButton(self.pop_up_frame)
        self.confirme_stop_button.setGeometry(QtCore.QRect(270, 286, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Black")
        font.setPointSize(14)
        self.confirme_stop_button.setFont(font)
        self.confirme_stop_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.confirme_stop_button.setStyleSheet("color: white; background-color: #12151c; border-radius: 5px; border: 1px solid;")
        self.confirme_stop_button.setObjectName("confirme_stop_button")
        self.registered_frame = QtWidgets.QFrame(self.app_frame)
        self.registered_frame.setGeometry(QtCore.QRect(0, 90, 971, 511))
        self.registered_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registered_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registered_frame.setObjectName("registered_frame")
        self.scrollArea = QtWidgets.QScrollArea(self.registered_frame)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 961, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 959, 489))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.close_button.clicked.connect(MainWindow.close)
        self.minimize_button.clicked.connect(MainWindow.lower)
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.consulte_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.consulte_cadastre_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registered_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.item_cadastre_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #função responsavel por setar os textos padroes das telas da UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.consulte_cadastre_button.setText(_translate("MainWindow", "Consultar/Cadastrar"))
        self.registered_button.setText(_translate("MainWindow", "Cadastrados"))
        self.origin_text.setText(_translate("MainWindow", "Origem *"))
        self.destiny_text.setText(_translate("MainWindow", "Destino *"))
        self.stop_text.setText(_translate("MainWindow", "Parada"))
        self.truck_text.setText(_translate("MainWindow", "Modalidade *"))
        self.consulte_button.setText(_translate("MainWindow", "Consultar"))
        self.price_text.setText(_translate("MainWindow", "Custo"))
        self.distance_text.setText(_translate("MainWindow", "Distancia"))
        self.item_text.setText(_translate("MainWindow", "Item *"))
        self.quantity_text.setText(_translate("MainWindow", "Quantidade *"))
        self.register_button.setText(_translate("MainWindow", "Cadastrar"))
        self.item_cadastre_button.setText(_translate("MainWindow", "Adicionar"))
        self.weight_text.setText(_translate("MainWindow", "Peso(KG) *"))
        self.confirme_stop_button.setText(_translate("MainWindow", "Confirmar"))
