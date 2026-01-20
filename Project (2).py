# DBMS Project
import requests
from re import A 
from sqlite3 import Cursor, connect
import sys
from time import strftime
from typing import Self
from unittest import installHandler
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox
from PyQt5.QtGui import QPixmap
import sql
import mysql.connector
from datetime import date
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QCoreApplication

""

#the source is "https://www.w3schools.com/python/python_mysql_insert.asp" for reference.

""
import os
import random
import twilio
import twilio.rest
from twilio.rest
import Client

class Welcome_screen(QDialog):
    def __init__(self):
        super(Welcome_screen, self).__init__()
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Welcome_UI_Screen.ui", self);
       
        (Relative Path-loadUi(r"Project_Source_Code\Welcome_UI_Screen.ui",self")
        self.Login.clicked.connect(self.gotoLogin)
        self.Create_an_Account.clicked.connect(self.gotoCreate)
        
    def gotoLogin(self):
        login = Login_screen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) # Creating a whole bunch/ list of widgets across windows/ screens
        # Helps in displaying the next window on being clicked
    
    def gotoCreate(self):
        create = Create_Screen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

EmaiWidget.setRowCount(0)
Self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    
result = cursor.fetchall()
if cursor.rowcount == 0:
    self.Error_Popup_Message.setText("No Data to fetch from!")
    for row_number, row_data in enumerate(result):
        self.Available_Flights_Table_Widget.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

elif Timing == "Select" and Airline_Company != "Select":

                if Airline_Company == "Indivo":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



                elif Airline_Company == "MetAirways":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Company = 'MetAirways' or F_Company = 'MetAir')"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Picejet":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Picejet'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Nistara":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Timing != "Select" and Airline_Company != "Select":
                    if Timing == "Day":
                        if Airline_Company == "Indivo":

                    
                            query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)
Row(row_number)

for column_number, data in enumerate(row_data):
                    self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
                    

if Airline_Company == "Indivo":
                        
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")

F_ID = result[0][0]
            
F_Dept_Location = result[0][1]
F_Arr_Location = result[0][2]
F_Company = result[0][3]
F_Duration = result[0][4]
F_Dept_Time = result[0][5]
F_Arr_Time = result[0][6]
F_Seats = result[0][7]
C_ID = result[0][8]

FlightID = F_ID
Company_ID = C_ID
            

F_Info_Customer = [F_ID, F_Dept_Location, F_Arr_Location, F_Company, F_Duration, str(F_Dept_Time), str(F_Arr_Time), F_Seats, C_ID]
cursor.execute('INSERT INTO Cust_Choice_Flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', F_Info_Customer)

db.commit()
db.close()

print("Succesfully inserted values in the Customer Choice Flight relation") # Displaying in VS Terminal for the developers to know client side

print(cursor.statement)

o_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(d["Date"])),

print()

self.User_Flight_Details.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
self.User_Flight_Details.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


result = cursor.fetchall()
print(result)
for row_number, row_data in enumerate(result):
                self.User_Flight_Details.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.User_Flight_Details.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



db.commit()

def gotoSummary_Information(self):
        global FlightID
        global Company_ID
        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)
        User_input_Flight_ID = self.Flight_ID.text()


        if len(User_input_Flight_ID) != 0:
            query = "SELECT * FROM flights WHERE F_ID = %s"

            tuple_1 = (User_input_Flight_ID)
            cursor.execute(query, (tuple_1, ))
            result = cursor.fetchall()
            User_input_Flight_ID = self.Flight_ID.text()
            F_ID = User_input_Flight_ID
            F_Dept_Location = result[0][1]
            F_Arr_Location = result[0][2]
            F_Company = result[0][3]
            F_Duration = result[0][4]
            F_Dept_Time = result[0][5]
            F_Arr_Time = result[0][6]
            F_Seats = result[0][7]
            C_ID = result[0][8]

            Company_ID = C_ID
            

            F_Info_Customer = [F_ID, F_Dept_Location, F_Arr_Location, F_Company, F_Duration, str(F_Dept_Time), str(F_Arr_Time), F_Seats, C_ID, FlightID]


            query = "UPDATE Cust_Choice_Flight SET F_ID = %s, F_Dept_Location = %s, F_Arr_Location = %s, F_Company = %s, F_Duration = %s, F_Dept_Time = %s, F_Arr_Time = %s, F_Seats = %s, C_ID = %s WHERE F_ID = %s"
            print()

            cursor.execute(query, F_Info_Customer)

            db.commit()
            db.close()

            FlightID = F_ID
            print("Succesfully Updated values of the Customer Choice Flight relation") # Displaying in VS Terminal for the developers to know client side

            print(cursor.statement)

            
            sum = Summary()
            widget.addWidget(sum)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class Summary(QDialog):
    def __init__(self):

        super(Summary, self).__init__()
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Summary_Screen.ui", self)
        # Relative Path - loadUi(r"Project_Source_Code\Summary_Screen.ui", self")
        
        self.Customer_Info_pushButton.clicked.connect(self.gotoUpdateCustomerInfo)
        self.Flight_Info_pushButton.clicked.connect(self.gotoUpdateFlightInfo)
        self.Yes_Button.clicked.connect(self.gotoPaymentInfo)
        self.No_Button.clicked.connect(self.gotoPaymentBooking_Screen)

        self.See_Additional_Info_button.clicked.connect(self.gotoAdditionalFlightInfo)
        

        # Declaing the use of Global variables here.
        global Email_Field
        global FlightID


        self.Customer_Info_TableWidget.setColumnWidth(0, 175)
        self.Customer_Info_TableWidget.setColumnWidth(1, 175)
        self.Customer_Info_TableWidget.setColumnWidth(3, 175)
        self.Customer_Info_TableWidget.setColumnWidth(4, 175)

        self.Customer_Info_TableWidget.setColumnWidth(5, 175)
        self.Customer_Info_TableWidget.setColumnWidth(6, 175)
        self.Customer_Info_TableWidget.setColumnWidth(7, 175)
        self.Customer_Info_TableWidget.setColumnWidth(8, 175)


        self.User_Selected_Flights_TableWidget.setColumnWidth(0, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(1, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(2, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(3, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(4, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(5, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(6, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(7, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(8, 175)
        

        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        query = "SELECT * FROM FULL_CUSTOMER_INFORMATION WHERE Customer_Name = %s;" # Displaying the Information from the VIEW FULL_CUSTOMER_INFORMATION which includes a cartesian product of 
        # the tables initial_info_account and full_profile_account where the Username of Customer_Name columns of the respective relations match.
        tpl = (Email_Field, )           
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()
        self.Customer_Info_TableWidget.setRowCount(0)
        self.Customer_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        result = cursor.fetchall()
        for row_number, row_data in enumerate(result):
            self.Customer_Info_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.Customer_Info_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


        
        query = "SELECT * FROM flights WHERE F_ID = %s"

        tuple_1 = (FlightID)
        cursor.execute(query, (tuple_1, ))
        

        print(cursor.statement)

        self.User_Selected_Flights_TableWidget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
        self.User_Selected_Flights_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        result = cursor.fetchall()
        print(result)
        for row_number, row_data in enumerate(result):
            self.User_Selected_Flights_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.User_Selected_Flights_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))




        
        self.Cancellation_Info_TableWidget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
        self.Cancellation_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        data = [{"Cancellation ID" : self.Cancellation_ID, "Cancellation Payment ID" : Payment_ID, "Cancellation Refund": self.Refund_Cost, "Cancellation Date" : self.Cancellation_Date}]
        row = 0

            





#Main
app = QApplication(sys.argv) # Launching the app with this variable
welcome = Welcome_screen() # Creating an instance for the class created above

widget = QStackedWidget() # Helps in moving between various screens/windows
widget.addWidget(welcome)
widget.setFixedHeight(800) # Fixing the Height of the GUI Window to 800
widget.setFixedWidth(1200) # Fixing the Width of the GUI Window to 1200
widget.show() # Displaying the whole Application

try: # In case the app doesn't exit.
    sys.exit(app.exec())
except:
    print("Exiting...") # Printing confirmation message of Application exit in VS Terminal.