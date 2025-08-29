# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vrijeme_app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_central = QVBoxLayout(self.centralwidget)
        self.verticalLayout_central.setObjectName(u"verticalLayout_central")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName(u"main_tabs")
        self.tab_trenutno = QWidget()
        self.tab_trenutno.setObjectName(u"tab_trenutno")
        self.verticalLayout_trenutno = QVBoxLayout(self.tab_trenutno)
        self.verticalLayout_trenutno.setObjectName(u"verticalLayout_trenutno")
        self.label_title_current = QLabel(self.tab_trenutno)
        self.label_title_current.setObjectName(u"label_title_current")
        self.label_title_current.setAlignment(Qt.AlignCenter)
        self.label_title_current.setStyleSheet(u"font-weight: 600; font-size: 18px;")

        self.verticalLayout_trenutno.addWidget(self.label_title_current)

        self.hLayout_city_input = QHBoxLayout()
        self.hLayout_city_input.setObjectName(u"hLayout_city_input")
        self.city_input = QLineEdit(self.tab_trenutno)
        self.city_input.setObjectName(u"city_input")

        self.hLayout_city_input.addWidget(self.city_input)

        self.fetch_button = QPushButton(self.tab_trenutno)
        self.fetch_button.setObjectName(u"fetch_button")

        self.hLayout_city_input.addWidget(self.fetch_button)


        self.verticalLayout_trenutno.addLayout(self.hLayout_city_input)

        self.grid_current = QGridLayout()
        self.grid_current.setObjectName(u"grid_current")
        self.city_label = QLabel(self.tab_trenutno)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setAlignment(Qt.AlignLeft)
        self.city_label.setStyleSheet(u"font-size: 16px;")

        self.grid_current.addWidget(self.city_label, 0, 0, 1, 2)

        self.icon_label = QLabel(self.tab_trenutno)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(100, 100))
        self.icon_label.setFrameShape(QFrame.NoFrame)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet(u"background: transparent;")

        self.grid_current.addWidget(self.icon_label, 1, 0, 1, 1)

        self.vLayout_stats = QVBoxLayout()
        self.vLayout_stats.setObjectName(u"vLayout_stats")
        self.temp_label = QLabel(self.tab_trenutno)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setStyleSheet(u"font-size: 32px; font-weight: 600;")

        self.vLayout_stats.addWidget(self.temp_label)

        self.desc_label = QLabel(self.tab_trenutno)
        self.desc_label.setObjectName(u"desc_label")

        self.vLayout_stats.addWidget(self.desc_label)

        self.humidity_label = QLabel(self.tab_trenutno)
        self.humidity_label.setObjectName(u"humidity_label")

        self.vLayout_stats.addWidget(self.humidity_label)

        self.wind_label = QLabel(self.tab_trenutno)
        self.wind_label.setObjectName(u"wind_label")

        self.vLayout_stats.addWidget(self.wind_label)


        self.grid_current.addLayout(self.vLayout_stats, 1, 1, 1, 1)


        self.verticalLayout_trenutno.addLayout(self.grid_current)

        self.main_tabs.addTab(self.tab_trenutno, "")
        self.tab_prognoza = QWidget()
        self.tab_prognoza.setObjectName(u"tab_prognoza")
        self.verticalLayout_prognoza = QVBoxLayout(self.tab_prognoza)
        self.verticalLayout_prognoza.setObjectName(u"verticalLayout_prognoza")
        self.forecast_table = QTableWidget(self.tab_prognoza)
        if (self.forecast_table.columnCount() < 3):
            self.forecast_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.forecast_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.forecast_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.forecast_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.forecast_table.setObjectName(u"forecast_table")
        self.forecast_table.setColumnCount(3)
        self.forecast_table.setRowCount(0)

        self.verticalLayout_prognoza.addWidget(self.forecast_table)

        self.graph_label = QLabel(self.tab_prognoza)
        self.graph_label.setObjectName(u"graph_label")
        self.graph_label.setMinimumSize(QSize(300, 180))
        self.graph_label.setFrameShape(QFrame.StyledPanel)
        self.graph_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_prognoza.addWidget(self.graph_label)

        self.main_tabs.addTab(self.tab_prognoza, "")
        self.tab_postavke = QWidget()
        self.tab_postavke.setObjectName(u"tab_postavke")
        self.verticalLayout_postavke = QVBoxLayout(self.tab_postavke)
        self.verticalLayout_postavke.setObjectName(u"verticalLayout_postavke")
        self.formLayout_settings = QFormLayout()
        self.formLayout_settings.setObjectName(u"formLayout_settings")
        self.label_api_text = QLabel(self.tab_postavke)
        self.label_api_text.setObjectName(u"label_api_text")

        self.formLayout_settings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_api_text)

        self.api_key_input = QLineEdit(self.tab_postavke)
        self.api_key_input.setObjectName(u"api_key_input")

        self.formLayout_settings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.api_key_input)

        self.label_units_text = QLabel(self.tab_postavke)
        self.label_units_text.setObjectName(u"label_units_text")

        self.formLayout_settings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_units_text)

        self.units_combo = QComboBox(self.tab_postavke)
        self.units_combo.addItem("")
        self.units_combo.addItem("")
        self.units_combo.setObjectName(u"units_combo")

        self.formLayout_settings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.units_combo)


        self.verticalLayout_postavke.addLayout(self.formLayout_settings)

        self.save_settings_button = QPushButton(self.tab_postavke)
        self.save_settings_button.setObjectName(u"save_settings_button")

        self.verticalLayout_postavke.addWidget(self.save_settings_button)

        self.verticalSpacer_postavke = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_postavke.addItem(self.verticalSpacer_postavke)

        self.main_tabs.addTab(self.tab_postavke, "")

        self.verticalLayout_central.addWidget(self.main_tabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.main_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vrijeme App", None))
        self.label_title_current.setText(QCoreApplication.translate("MainWindow", u"Trenutno vrijeme", None))
        self.city_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unesite grad (npr. Zagreb)", None))
        self.fetch_button.setText(QCoreApplication.translate("MainWindow", u"Dohvati vrijeme", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"Grad, Dr\u017eava", None))
        self.icon_label.setText("")
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"--.-\u00b0C", None))
        self.desc_label.setText(QCoreApplication.translate("MainWindow", u"Opis vremena", None))
        self.humidity_label.setText(QCoreApplication.translate("MainWindow", u"Vla\u017enost: --%", None))
        self.wind_label.setText(QCoreApplication.translate("MainWindow", u"Brzina vjetra: -- m/s", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_trenutno), QCoreApplication.translate("MainWindow", u"Trenutno", None))
        ___qtablewidgetitem = self.forecast_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Vrijeme", None));
        ___qtablewidgetitem1 = self.forecast_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None));
        ___qtablewidgetitem2 = self.forecast_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Opis", None));
        self.graph_label.setText(QCoreApplication.translate("MainWindow", u"Graf promjene temperature", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_prognoza), QCoreApplication.translate("MainWindow", u"Prognoza", None))
        self.label_api_text.setText(QCoreApplication.translate("MainWindow", u"OpenWeather API klju\u010d:", None))
        self.api_key_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unesite API klju\u010d", None))
        self.label_units_text.setText(QCoreApplication.translate("MainWindow", u"Jedinice:", None))
        self.units_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Celzijus", None))
        self.units_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Fahrenheit", None))

        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Spremi postavke", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab_postavke), QCoreApplication.translate("MainWindow", u"Postavke", None))
    # retranslateUi

