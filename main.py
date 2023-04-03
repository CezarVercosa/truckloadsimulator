from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pandas, sys





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #função de inicialização da interface
    def __init__(self):
        super().__init__()  
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Antonio Cezar Verçosa Cavalcante')
        self.defaultItems()
        self.readerFile()
        self.listItems = list()
        self.itemMediaList = list()
        self.counter = 1
        self.pop_up_frame.setVisible(False)
        self.content_frame.setVisible(False)
        self.registered_frame.setVisible(False)
        self.item_cadastre_button.clicked.connect(self.addItems)
        self.consulte_cadastre_button.clicked.connect(self.registerSearchButtons)
        self.registered_button.clicked.connect(self.registeredTruckLoads)
        self.consulte_button.clicked.connect(self.calculate)
        self.register_button.clicked.connect(self.registerTruckload)
        self.confirme_stop_button.clicked.connect(self.confirmPopUp)
        
    #função para os botoes consultar/registrar
    def registerSearchButtons(self):
        self.consulte_cadastre_button.setStyleSheet('border: 1px solid rgba(128, 128, 128, 0.3); border-radius: 15px; color: white; font-size: 20px;')
        self.registered_button.setStyleSheet('border: none; color: white; font-size: 20px;')
        self.registered_frame.setVisible(False)
        self.content_frame.setVisible(True)
        self.registered_frame.setVisible(False)
        
    #função para acessar as cargas registradas
    def registeredTruckLoads(self):
        if self.registered_frame.isVisible():
            return
        self.registered_button.setStyleSheet('border: 1px solid rgba(128, 128, 128, 0.3); border-radius: 15px; color: white; font-size: 20px;')
        self.consulte_cadastre_button.setStyleSheet('border: none; color: white; font-size: 20px;')
        self.content_frame.setVisible(False)
        self.registered_frame.setVisible(True)
             
    #função para adicionar itens ao registro
    def addItems(self):
        itemName = self.item_box.text()
        itemQuantity = self.quantity_box.text()
        itemWeight = self.weight_box.text()
        if itemName == "" or itemQuantity == "" or itemWeight == "":
            self.confirme_item_text.setText("Preencha os campos obrigatorios")
        else:   
            self.confirme_item_text.setText("")
            self.description_item_text = QtWidgets.QLabel(self.itemScrollWidgetContents)
            self.description_item_text.setMinimumSize(QtCore.QSize(0, 20))
            self.description_item_text.setMaximumSize(QtCore.QSize(16777215, 20))
            self.description_item_text.setStyleSheet("color: white;")
            self.description_item_text.setObjectName("description_item_text")
            self.description_item_text.setText(f"Item: {itemName} - Qtd: {itemQuantity} - Peso: {itemWeight}")
            self.verticalItemLayout.addWidget(self.description_item_text)
            self.itemObject = {}
            self.itemObject[itemName] = [itemQuantity, itemWeight]
            self.listItems.append(self.itemObject)
            self.item_box.clear()
            self.quantity_box.clear()
            self.weight_box.clear()
            
    #função para registrar os itens para a tela de popup      
    def confirmItems(self, name, quantity, weight):
        self.pop_up_item_frame = QtWidgets.QFrame(self.pop_up_scroll_WidgetContents)
        self.pop_up_item_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.pop_up_item_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pop_up_item_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pop_up_item_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pop_up_item_frame.setObjectName("pop_up_item_frame")
        self.pop_up_item_text = QtWidgets.QLabel(self.pop_up_item_frame)
        self.pop_up_item_text.setGeometry(QtCore.QRect(0, 0, 277, 30))
        self.pop_up_item_text.setMinimumSize(QtCore.QSize(0, 30))
        self.pop_up_item_text.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pop_up_item_text.setStyleSheet("color: white; border: 0.5px solid rgba(128, 128, 128, 0.1);")
        self.pop_up_item_text.setTextFormat(QtCore.Qt.AutoText)
        self.pop_up_item_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pop_up_item_text.setObjectName("pop_up_item_text")
        self.pop_up_item_quantity_box = QtWidgets.QLineEdit(self.pop_up_item_frame)
        self.pop_up_item_quantity_box.setGeometry(QtCore.QRect(279, 2, 90, 25))
        self.pop_up_item_quantity_box.setStyleSheet("background-color: #12151c; border-top: 0.5px solid;border-left: 0.5px solid; color: white;")
        self.pop_up_item_quantity_box.setObjectName("pop_up_item_quantity_box")
        self.intValidator = QtGui.QIntValidator()
        self.pop_up_item_quantity_box.setValidator(self.intValidator)
        self.pop_up_item_text.setText(f"Item: {name} - Quantidade: {quantity} - Peso: {weight} KG ")
    
        self.verticalLayout_2.addWidget(self.pop_up_item_frame)
        
    #função para calcular a viagem e enviar para os cards
    def calculeTravel(self):
        originCity = self.origin_box.currentText()
        endCity = self.destiny_box.currentText()
        localizationEnd = self.database.columns.get_loc(endCity)
        stopCity = "Não se aplica"
        weightTotal = 0
        quantityTotal = 0
        distance1 = 0
        distance2 = 0
        smallTruck = 0
        mediumTruck = 0
        bigTruck = 0
        mediaKm = 0
        totalTrucks = 0
        distancePrice = 0
        distanceTotal = 0
        costSmallTruck = 0
        costMediumTruck = 0
        costBigTruck = 0
        snippetTwo = ""

        

        for dict in self.listItems:
            itemName = list(dict.keys())[0]
            items = dict[itemName]
            quantity = items[0]
            weight = items[1]
            weightTotal += int(weight)
            quantityTotal += int(quantity)

        while weightTotal > 0:
            if weightTotal > 0 and weightTotal <= 1000:
                smallTruck += 1
                weightTotal -= 1000
            elif weightTotal > 1000 and weightTotal <= 4000:
                mediumTruck += 1
                weightTotal -= 4000
            elif weightTotal > 4000:
                bigTruck += 1
                weightTotal -= 10000
        
        totalTrucks = smallTruck + mediumTruck + bigTruck
        
        if self.stop_box.currentText() != "Não se aplica":
            stopCity = self.stop_box.currentText()
            localizationStop = self.database.columns.get_loc(stopCity)
            distance1 += self.database[originCity][localizationStop]
            distance2 += self.database[stopCity][localizationEnd]
            distanceTotal = distance1 + distance2

            if smallTruck >= 1:
                distancePrice = int(distanceTotal) * (smallTruck * 4.87)
                costSmallTruck = distancePrice
            if mediumTruck >= 1:
                distancePrice += int(distanceTotal) * (mediumTruck * 11.92)
                costMediumTruck = int(distance1) * (mediumTruck * 11.92)
            if bigTruck >= 1:
                distancePrice += int(distanceTotal) * (bigTruck * 27.44)
                costBigTruck = int(distance1) * (bigTruck * 27.44)
            
            for dict in self.listItems:
                itemName = list(dict.keys())[0]
                items = dict[itemName]
                quantity = items[0]
                self.itemMediaList.append(str(f"{itemName} - R${distancePrice / float(quantity):.2f}"))

            formSmallTruck = f"R${costSmallTruck:.2f}"
            formMediumTruck = f"R${costMediumTruck:.2f}"
            formBigTruck = f"R${costBigTruck:.2f}"
            mediaKm = f"R${distancePrice / distanceTotal:.2f}"
            snippetOne = f"{originCity} => {stopCity}"
            snippetTwo = f"{stopCity} => {endCity}"
            formDistance = f"{distance1:.2f} KM"
            formDistancePriceTotal = f"R${distancePrice:.2f}"
            formDistance2 = f"{distance2:.2f} KM"
            

            
            self.cards(str(totalTrucks), str(quantityTotal), str(mediaKm), str(snippetOne), str(snippetTwo), str(formDistance), 
                   str(formDistancePriceTotal), str(formSmallTruck), str(formMediumTruck), str(formBigTruck), str(formDistance2))

            
            
        else:
            distance1 += self.database[originCity][localizationEnd]
            distanceTotal = distance1
            
            if smallTruck >= 1:
                distancePrice = int(distanceTotal) * (smallTruck * 4.87)
                costSmallTruck = distancePrice
            if mediumTruck >= 1:
                distancePrice += int(distanceTotal) * (mediumTruck * 11.92)
                costMediumTruck = int(distance1) * (mediumTruck * 11.92)
            if bigTruck >= 1:
                distancePrice += int(distanceTotal) * (bigTruck * 27.44)
                costBigTruck = int(distance1) * (bigTruck * 27.44)

            
            for dict in self.listItems:
                itemName = list(dict.keys())[0]
                items = dict[itemName]
                quantity = items[0]
                self.itemMediaList.append(str(f"{itemName} - R${distancePrice / float(quantity):.2f}"))

                
            formSmallTruck = f"R${costSmallTruck:.2f}"
            formMediumTruck = f"R${costMediumTruck:.2f}"
            formBigTruck = f"R${costBigTruck:.2f}"
            mediaKm = f"R${distancePrice / distanceTotal:.2f}"
            snippet = f"{originCity} => {endCity}"
            formDistance = f"{distanceTotal:.2f} KM"
            formDistancePriceTotal = f"R${distancePrice:.2f}"
            formDistance2 = ""
            

            self.cards(str(totalTrucks), str(quantityTotal), str(mediaKm), str(snippet), str(stopCity), str(formDistance), 
                   str(formDistancePriceTotal), str(formSmallTruck), str(formMediumTruck), str(formBigTruck), str(formDistance2))

    #função para registrar o transporte
    def registerTruckload(self):
        self.itemMediaList.clear()
        cityInitial = self.origin_box.currentText()
        cityStop = ""
        cityEnd = self.destiny_box.currentText()
        
            
        if self.origin_box.currentText() == "Selecione" or self.destiny_box.currentText() == "Selecione":
            self.warning_box.setText('Preencha os campos obrigatorios')
            return
        else:
            self.warning_box.setText("")
        if len(self.listItems) == 0:
            self.confirme_item_text.setText('Adicione ao menos um item')
            return
        else:
            self.confirme_item_text.setText("")
            
        
        if self.stop_box.currentText() != "Não se aplica":
            self.pop_up_frame.setVisible(True)
            cityStop = self.stop_box.currentText()
            self.pop_up_city_stop_text.setText(f"Quais itens serão deixados em: {cityStop}")
            for dict in self.listItems:
                itemName = list(dict.keys())[0]
                items = dict[itemName]
                quantity = items[0]
                weight = items[1]
                self.confirmItems(itemName, quantity, weight)
            self.calculeTravel()
        else:
            self.calculeTravel()
            self.clearFields()

    #função para limpar os campos
    def clearFields(self):
        self.origin_box.setCurrentIndex(0)
        self.destiny_box.setCurrentIndex(0)
        self.stop_box.setCurrentIndex(0)
        self.truck_box.setCurrentIndex(0)
        self.price_box.setText('')
        self.distance_box.setText('')
        self.item_box.setText('')
        self.quantity_box.setText('')
        self.weight_box.setText('')
        
        self.listItems.clear()
        widget = self.itemScroll.widget()
        self.removeScrollItems(widget)
        widget = self.pop_up_scroll.widget()
        self.removePopUpItems(widget)
                
    #função para limpar o scroll da tela do popup
    def removePopUpItems(self, viewport):
        for widget in viewport.findChildren(QtWidgets.QWidget):
            layout = viewport.layout()
            layout.removeWidget(widget)
            widget.deleteLater()

    #função para limpar o scroll da tela principal
    def removeScrollItems(self, widget):
        for filho in widget.findChildren(QtWidgets.QWidget):
            if isinstance(filho, QtWidgets.QFrame):
                layout = widget.layout()
                layout.removeWidget(filho)
                filho.deleteLater()
            else:
                self.removeScrollItems(self, filho)

    #função do botao confirmar do popup
    def confirmPopUp(self):
        self.clearFields()
        self.pop_up_frame.setVisible(False)
        
    #função para setar os itens padroes das boxs
    def defaultItems(self):
        self.truck_box.addItems(["Selecione", "Pequeno", "Médio", "Grande"])
        self.origin_box.addItem("Selecione")
        self.destiny_box.addItem("Selecione")
        self.stop_box.addItem("Não se aplica")
    
    #função de leitura do arquivo csv
    def readerFile(self):
        self.database = pandas.read_csv("DNIT-Distancias.csv", sep=";")
        cityList = self.database.columns.tolist()  
        self.setCityBox(cities=cityList)

    #função de setar nas box as cidades do arquivo csv
    def setCityBox(self, cities):
        self.origin_box.addItems(list(cities))
        self.destiny_box.addItems(list(cities))
        self.stop_box.addItems(list(cities))
    
    #função de calculo da rota
    def calculate(self):
        if self.truck_box.currentText() == "Selecione" or self.origin_box.currentText() == "Selecione" or self.destiny_box.currentText() == "Selecione":
            self.warning_box.setText("Preencha os campos obrigatorios.")
            self.distance_box.setText("")
            self.price_box.setText("")
            return
        else:
            self.warning_box.setText("")
            cityInitial = self.origin_box.currentText()
            endCity = self.destiny_box.currentText()
            localizationEnd = self.database.columns.get_loc(endCity)
            distance = 0
            if self.stop_box.currentText() != "Não se aplica":
                stopCity = self.stop_box.currentText()
                localizationStop = self.database.columns.get_loc(stopCity)
                distance = self.database[cityInitial][localizationStop]
                distance = distance + self.database[stopCity][localizationEnd]
                truckType = self.truck_box.currentText()
                
            else:
                distance = self.database[cityInitial][localizationEnd]
                truckType = self.truck_box.currentText()
                distancePrice = 0
            if truckType == "Pequeno":
                distancePrice = int(distance) * 4.87
            if truckType == "Médio":
                distancePrice = int(distance) * 11.92
            if truckType == "Grande":
                distancePrice = int(distance) * 27.44
            self.distance_box.setText(str(distance) + " KM")
            finalValue = str("R$ %.2f" % distancePrice).replace(".", ",")
            self.price_box.setText(finalValue)
    
    #função responsavel pela criação dos cards das cargas registradas
    def cards(self, totalVehicles, totalItems, mediaKm, cityStartEnd, cityStop, formDistance, formDistancePriceTotal, smallCostTruck, mediumCostTruck, bigCostTruck, formDistance2):
        self.registerer_card = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.registerer_card.setEnabled(True)
        self.registerer_card.setMaximumSize(QtCore.QSize(400, 16777215))
        self.registerer_card.setStyleSheet("background-color: #12151c; border: 1px solid black;")
        self.registerer_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registerer_card.setMinimumSize(QtCore.QSize(400, 16777215))
        self.registerer_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registerer_card.setObjectName("registerer_card")
        self.number_card_effect = QtWidgets.QLabel(self.registerer_card)
        self.number_card_effect.setGeometry(QtCore.QRect(-49, -50, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Gilroy-ExtraBold")
        font.setPointSize(14)
        self.number_card_effect.setFont(font)
        self.number_card_effect.setStyleSheet("#number_card_effect{\n"
            "    background-color: white;\n"
            "    border: 1px solid;\n"
            "    border-radius: 50%;\n"
            "    border-color: white;\n"
            "\n"
            "}")
        self.number_card_effect.setText("")
        self.number_card_effect.setAlignment(QtCore.Qt.AlignCenter)
        self.number_card_effect.setObjectName("number_card_effect")
        self.number_card_box = QtWidgets.QLabel(self.registerer_card)
        self.number_card_box.setGeometry(QtCore.QRect(8, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.number_card_box.setFont(font)
        self.number_card_box.setStyleSheet("background-color: white; border: none;")
        self.number_card_box.setAlignment(QtCore.Qt.AlignCenter)
        self.number_card_box.setObjectName("number_card_box")
        self.card_effects = QtWidgets.QLabel(self.registerer_card)
        self.card_effects.setGeometry(QtCore.QRect(349, 6, 30, 5))
        self.card_effects.setStyleSheet("background-color: white;")
        self.card_effects.setText("")
        self.card_effects.setObjectName("card_effects")
        self.card_effects_2 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_2.setGeometry(QtCore.QRect(380, 6, 5, 5))
        self.card_effects_2.setStyleSheet("background-color: white;")
        self.card_effects_2.setText("")
        self.card_effects_2.setObjectName("card_effects_2")
        self.card_effects_3 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_3.setGeometry(QtCore.QRect(385, 6, 5, 5))
        self.card_effects_3.setStyleSheet("background-color: white;")
        self.card_effects_3.setText("")
        self.card_effects_3.setObjectName("card_effects_3")
        self.card_effects_4 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_4.setGeometry(QtCore.QRect(390, 6, 5, 5))
        self.card_effects_4.setStyleSheet("background-color: white;")
        self.card_effects_4.setText("")
        self.card_effects_4.setObjectName("card_effects_4")
        self.card_effects_5 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_5.setGeometry(QtCore.QRect(25, 465, 30, 5))
        self.card_effects_5.setStyleSheet("background-color: white;")
        self.card_effects_5.setText("")
        self.card_effects_5.setObjectName("card_effects_5")
        self.card_effects_6 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_6.setGeometry(QtCore.QRect(19, 465, 5, 5))
        self.card_effects_6.setStyleSheet("background-color: white;")
        self.card_effects_6.setText("")
        self.card_effects_6.setObjectName("card_effects_6")
        self.card_effects_7 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_7.setGeometry(QtCore.QRect(13, 465, 5, 5))
        self.card_effects_7.setStyleSheet("background-color: white;")
        self.card_effects_7.setText("")
        self.card_effects_7.setObjectName("card_effects_7")
        self.card_effects_8 = QtWidgets.QLabel(self.registerer_card)
        self.card_effects_8.setGeometry(QtCore.QRect(7, 465, 5, 5))
        self.card_effects_8.setStyleSheet("background-color: white;")
        self.card_effects_8.setText("")
        self.card_effects_8.setObjectName("card_effects_8")
        self.cost_total_text = QtWidgets.QLabel(self.registerer_card)
        self.cost_total_text.setGeometry(QtCore.QRect(158, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cost_total_text.setFont(font)
        self.cost_total_text.setStyleSheet("color: white; border: none;")
        self.cost_total_text.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_total_text.setObjectName("cost_total_text")
        self.cost_total_box = QtWidgets.QLabel(self.registerer_card)
        self.cost_total_box.setGeometry(QtCore.QRect(164, 40, 91, 21))
        self.cost_total_box.setStyleSheet("color: white")
        self.cost_total_box.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_total_box.setObjectName("cost_total_box")
        self.cost_medium_text = QtWidgets.QLabel(self.registerer_card)
        self.cost_medium_text.setGeometry(QtCore.QRect(18, 90, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cost_medium_text.setFont(font)
        self.cost_medium_text.setStyleSheet("color: white; border: none;")
        self.cost_medium_text.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_medium_text.setObjectName("cost_medium_text")
        self.cost_medium_box = QtWidgets.QLabel(self.registerer_card)
        self.cost_medium_box.setGeometry(QtCore.QRect(18, 109, 121, 21))
        self.cost_medium_box.setStyleSheet("color: white")
        self.cost_medium_box.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_medium_box.setObjectName("cost_medium_box")
        self.total_items_text = QtWidgets.QLabel(self.registerer_card)
        self.total_items_text.setGeometry(QtCore.QRect(283, 90, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_items_text.setFont(font)
        self.total_items_text.setStyleSheet("color: white; border: none;")
        self.total_items_text.setAlignment(QtCore.Qt.AlignCenter)
        self.total_items_text.setObjectName("total_items_text")
        self.total_tems_box = QtWidgets.QLabel(self.registerer_card)
        self.total_tems_box.setGeometry(QtCore.QRect(279, 109, 111, 21))
        self.total_tems_box.setStyleSheet("color: white")
        self.total_tems_box.setAlignment(QtCore.Qt.AlignCenter)
        self.total_tems_box.setObjectName("total_tems_box")
        self.total_vehicles_text = QtWidgets.QLabel(self.registerer_card)
        self.total_vehicles_text.setGeometry(QtCore.QRect(144, 90, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_vehicles_text.setFont(font)
        self.total_vehicles_text.setStyleSheet("color: white; border: none;")
        self.total_vehicles_text.setAlignment(QtCore.Qt.AlignCenter)
        self.total_vehicles_text.setObjectName("total_vehicles_text")
        self.total_vehicles_box = QtWidgets.QLabel(self.registerer_card)
        self.total_vehicles_box.setGeometry(QtCore.QRect(145, 109, 131, 21))
        self.total_vehicles_box.setStyleSheet("color: white")
        self.total_vehicles_box.setAlignment(QtCore.Qt.AlignCenter)
        self.total_vehicles_box.setObjectName("total_vehicles_box")
        self.media_items_content = QtWidgets.QFrame(self.registerer_card)
        self.media_items_content.setGeometry(QtCore.QRect(18, 329, 156, 121))
        self.media_items_content.setStyleSheet("")
        self.media_items_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.media_items_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.media_items_content.setObjectName("media_items_content")
        


        self.media_cost_itens_title_text = QtWidgets.QLabel(self.registerer_card)
        self.media_cost_itens_title_text.setGeometry(QtCore.QRect(19, 306, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.media_cost_itens_title_text.setFont(font)
        self.media_cost_itens_title_text.setStyleSheet("color: white; border: none;")
        self.media_cost_itens_title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.media_cost_itens_title_text.setObjectName("media_cost_itens_title_text")
        self.modality_content = QtWidgets.QFrame(self.registerer_card)
        self.modality_content.setGeometry(QtCore.QRect(225, 329, 156, 121))
        self.modality_content.setStyleSheet("")
        self.modality_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modality_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modality_content.setObjectName("modality_content")
        self.small_modality_cost_text = QtWidgets.QLabel(self.modality_content)
        self.small_modality_cost_text.setGeometry(QtCore.QRect(57, 3, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        self.small_modality_cost_text.setFont(font)
        self.small_modality_cost_text.setStyleSheet("Color: white; border: none;")
        self.small_modality_cost_text.setAlignment(QtCore.Qt.AlignCenter)
        self.small_modality_cost_text.setObjectName("small_modality_cost_text")
        self.small_modality_cost_box = QtWidgets.QLabel(self.modality_content)
        self.small_modality_cost_box.setGeometry(QtCore.QRect(35, 20, 91, 16))
        self.small_modality_cost_box.setStyleSheet("color: white")
        self.small_modality_cost_box.setAlignment(QtCore.Qt.AlignCenter)
        self.small_modality_cost_box.setObjectName("small_modality_cost_box")
        self.medium_modality_cost_text = QtWidgets.QLabel(self.modality_content)
        self.medium_modality_cost_text.setGeometry(QtCore.QRect(53, 40, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        self.medium_modality_cost_text.setFont(font)
        self.medium_modality_cost_text.setStyleSheet("Color: white; border: none;")
        self.medium_modality_cost_text.setAlignment(QtCore.Qt.AlignCenter)
        self.medium_modality_cost_text.setObjectName("medium_modality_cost_text")
        self.medium_modality_cost_box = QtWidgets.QLabel(self.modality_content)
        self.medium_modality_cost_box.setGeometry(QtCore.QRect(35, 58, 91, 16))
        self.medium_modality_cost_box.setStyleSheet("color: white")
        self.medium_modality_cost_box.setAlignment(QtCore.Qt.AlignCenter)
        self.medium_modality_cost_box.setObjectName("medium_modality_cost_box")
        self.big_modality_cost_text = QtWidgets.QLabel(self.modality_content)
        self.big_modality_cost_text.setGeometry(QtCore.QRect(56, 76, 45, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        self.big_modality_cost_text.setFont(font)
        self.big_modality_cost_text.setStyleSheet("Color: white; border: none;")
        self.big_modality_cost_text.setAlignment(QtCore.Qt.AlignCenter)
        self.big_modality_cost_text.setObjectName("big_modality_cost_text")
        self.big_modality_cost_box = QtWidgets.QLabel(self.modality_content)
        self.big_modality_cost_box.setGeometry(QtCore.QRect(35, 94, 91, 16))
        self.big_modality_cost_box.setStyleSheet("color: white")
        self.big_modality_cost_box.setAlignment(QtCore.Qt.AlignCenter)
        self.big_modality_cost_box.setObjectName("big_modality_cost_box")
        self.modality_cost_title_text = QtWidgets.QLabel(self.registerer_card)
        self.modality_cost_title_text.setGeometry(QtCore.QRect(227, 306, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modality_cost_title_text.setFont(font)
        self.modality_cost_title_text.setStyleSheet("color: white; border: none;")
        self.modality_cost_title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.modality_cost_title_text.setObjectName("modality_cost_title_text")
        self.snippet_content = QtWidgets.QFrame(self.registerer_card)
        self.snippet_content.setGeometry(QtCore.QRect(10, 169, 381, 131))
        self.snippet_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.snippet_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.snippet_content.setObjectName("snippet_content")
        self.snippet_cost_text = QtWidgets.QLabel(self.snippet_content)
        self.snippet_cost_text.setGeometry(QtCore.QRect(73, 4, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.snippet_cost_text.setFont(font)
        self.snippet_cost_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.snippet_cost_text.setStyleSheet("color: white; border: none;")
        self.snippet_cost_text.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_cost_text.setObjectName("snippet_cost_text")
        self.snippet_box = QtWidgets.QLabel(self.snippet_content)
        self.snippet_box.setGeometry(QtCore.QRect(1, 20, 201, 20))
        self.snippet_box.setStyleSheet("color: white; border: none;")
        self.snippet_box.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_box.setObjectName("snippet_box")
        self.snippet_cost_box = QtWidgets.QLabel(self.snippet_content)
        self.snippet_cost_box.setGeometry(QtCore.QRect(49, 42, 71, 16))
        self.snippet_cost_box.setStyleSheet("color: white")
        self.snippet_cost_box.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_cost_box.setObjectName("snippet_cost_box")
        self.snippet_cost_text_2 = QtWidgets.QLabel(self.snippet_content)
        self.snippet_cost_text_2.setGeometry(QtCore.QRect(74, 71, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.snippet_cost_text_2.setFont(font)
        self.snippet_cost_text_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.snippet_cost_text_2.setStyleSheet("color: white; border: none;")
        self.snippet_cost_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_cost_text_2.setObjectName("snippet_cost_text_2")
        self.snippet_box_2 = QtWidgets.QLabel(self.snippet_content)
        self.snippet_box_2.setGeometry(QtCore.QRect(1, 88, 201, 20))
        self.snippet_box_2.setStyleSheet("color: white; border: none;")
        self.snippet_box_2.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_box_2.setObjectName("snippet_box_2")
        self.snippet_cost_box_2 = QtWidgets.QLabel(self.snippet_content)
        self.snippet_cost_box_2.setGeometry(QtCore.QRect(49, 110, 71, 16))
        self.snippet_cost_box_2.setStyleSheet("color: white")
        self.snippet_cost_box_2.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_cost_box_2.setObjectName("snippet_cost_box_2")
        self.snippet_total_cust_text = QtWidgets.QLabel(self.snippet_content)
        self.snippet_total_cust_text.setGeometry(QtCore.QRect(260, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.snippet_total_cust_text.setFont(font)
        self.snippet_total_cust_text.setStyleSheet("color: white; border: none;")
        self.snippet_total_cust_text.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_total_cust_text.setObjectName("snippet_total_cust_text")
        self.snippet_total_cost_box = QtWidgets.QLabel(self.snippet_content)
        self.snippet_total_cost_box.setGeometry(QtCore.QRect(266, 60, 91, 21))
        self.snippet_total_cost_box.setStyleSheet("color: white")
        self.snippet_total_cost_box.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_total_cost_box.setObjectName("snippet_total_cost_box")
        self.snippet_costs_title_text = QtWidgets.QLabel(self.registerer_card)
        self.snippet_costs_title_text.setGeometry(QtCore.QRect(155, 150, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.snippet_costs_title_text.setFont(font)
        self.snippet_costs_title_text.setStyleSheet("color: white; border: none;")
        self.snippet_costs_title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.snippet_costs_title_text.setObjectName("snippet_costs_title_text")
        self.horizontalLayout.addWidget(self.registerer_card)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.number_card_box.setText(str(self.counter))
        self.counter = self.counter + 1
        self.cost_total_text.setText("Custo Total")
        self.cost_total_box.setText("0")
        self.cost_medium_text.setText("Custo Médio KM")
        self.cost_medium_box.setText("0")
        self.total_items_text.setText("Total De Itens")
        self.total_tems_box.setText("0")
        self.total_vehicles_text.setText("Total De Veículos")
        self.total_vehicles_box.setText("0")

        #scroll media items
        self.media_scroll = QtWidgets.QScrollArea(self.media_items_content)
        self.media_scroll.setGeometry(QtCore.QRect(4, 4, 150, 115))
        self.media_scroll.setStyleSheet("border: none;")
        self.media_scroll.setWidgetResizable(True)
        self.media_scroll.setObjectName("media_scroll")
        self.media_scrollWidgetContents = QtWidgets.QWidget()
        self.media_scrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 150, 115))
        self.media_scrollWidgetContents.setObjectName("media_scrollWidgetContents")
        self.media_item_layout = QtWidgets.QVBoxLayout(self.media_scrollWidgetContents)
        self.media_item_layout.setObjectName("media_item_layout")
        

        for i in self.itemMediaList:
            self.item_media_frame = QtWidgets.QFrame(self.media_scrollWidgetContents)
            self.item_media_frame.setMinimumSize(QtCore.QSize(130, 20))
            self.item_media_frame.setMaximumSize(QtCore.QSize(16777215, 20))
            self.item_media_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.item_media_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.item_media_frame.setObjectName("item_media_frame")
            self.media_item_box = QtWidgets.QLabel(self.item_media_frame)
            self.media_item_box.setGeometry(QtCore.QRect(1, 0, 131, 20))
            self.media_item_box.setMinimumSize(QtCore.QSize(0, 20))
            self.media_item_box.setMaximumSize(QtCore.QSize(16777215, 20))
            self.media_item_box.setStyleSheet("border:none; color: white;")
            self.media_item_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.media_item_box.setObjectName("media_item_box")
            self.media_item_box.setText(i)
            self.media_item_layout.addWidget(self.item_media_frame)
            self.media_scroll.setWidget(self.media_scrollWidgetContents)
            

        self.total_vehicles_box.setText(totalVehicles)
        self.total_tems_box.setText(totalItems)
        self.cost_medium_box.setText(mediaKm)
        self.snippet_box.setText(cityStartEnd)
        self.snippet_cost_box.setText(formDistance)
        self.small_modality_cost_box.setText(smallCostTruck)
        self.medium_modality_cost_box.setText(mediumCostTruck)
        self.big_modality_cost_box.setText(bigCostTruck)
        self.cost_total_box.setText(formDistancePriceTotal)
        self.snippet_total_cost_box.setText(formDistancePriceTotal)


        if cityStop == "Não se aplica":
            self.snippet_cost_text_2.setVisible(False)
            self.snippet_box_2.setVisible(False)
            self.snippet_cost_box_2.setVisible(False)
            self.snippet_total_cost_box.setText(formDistancePriceTotal)
        else:
           self.snippet_cost_text_2.setVisible(True)
           self.snippet_box_2.setVisible(True)
           self.snippet_cost_box_2.setVisible(True)
           self.snippet_box_2.setText(cityStop)
           self.snippet_cost_box_2.setText(formDistance2)
           



        self.media_cost_itens_title_text.setText("Custos Médios Itens")
        self.small_modality_cost_text.setText("Pequeno")
        self.medium_modality_cost_text.setText("Médio")
        self.big_modality_cost_text.setText("Grande")
        self.modality_cost_title_text.setText("Custos Modalidades")
        self.snippet_cost_text.setText("1")
        self.snippet_cost_text_2.setText("2")
        self.snippet_total_cust_text.setText("Custo Total")
        self.snippet_costs_title_text.setText("Trechos")

         

#função de inicialização da interface
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())   