from PyQt5.QtGui import QTextLine
from PyQt5.QtWidgets import *
import sys
 
class MainWidget(QMainWindow): #Создание главного окна меню
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("MS параметры из SpectRelax")
        self.resize(500,500)
        self.setAcceptDrops(True)
        Vvod_texta='Программа позволяет  сохранять в таблицу-файл мессбауэровские параметры SpectRelax \n \n \n 1 Перетащите нужный файл "имя.csv" в окно программы \n 2 Выходной файл с параметрами сохранится в ту же папку с "имя_output.csv"'

        lbl1 = QLabel(Vvod_texta, self)
        lbl1.move(10, 0)
        lbl1.resize(500,300)
    


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            
            # -*- coding: utf-8 -*-
            import re;
            import csv

            path_to_MS_spectra=str(f)
            textfile = open(path_to_MS_spectra, encoding='utf8')
            filetext = textfile.read()
            textfile.close()
             # Счетчик для подсчета количества строк и вывода заголовков столбцов
            Okruglenie=3 #Округление до 3 знака после запятой

            # Выходные данные 
            Output_Hat=(f'Component	δ, mm/s 	ε, mm/s 	Hhf, kOe	Γ, mm/s	    S, %	    I2/I1	    I3/I1\n')
            Output_Sextet=''
            Output_Doublet=''
            Output_Singlet=''
            Output_Sextet_D=''
            Output_Doublet_D=''

            #Поиск Xi2 и последующая запись в конце файла значения Xi2
            with open(path_to_MS_spectra, encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ";")
                x='Χ²'
                for row in reader:
                    Xi=round(float(row[x]),Okruglenie)
                    String_Xi=str(Xi)    
                    Output_Xi='Χ² =  '+String_Xi

            # Поиск секстета 
            count_Sextet=1
            name_Sextet='PseudoVoigt sextet'
            str_count_Sextet=str(count_Sextet) 
            while count_Sextet<16:
                str_count_Sextet=str(count_Sextet) #Ищем 1PseudoVoigt sextet, если находим то index_Sextet равно цифре count_Sextet
                search_sextet=str_count_Sextet+name_Sextet
                if re.search(search_sextet,filetext):
                    index_Sextet=count_Sextet
                    str_index_Sextet=str(index_Sextet)
                    with open(path_to_MS_spectra, encoding='utf-8') as r_file:
                        # Создаем объект DictReader, указываем символ-разделитель ","
                        file_reader = csv.DictReader(r_file, delimiter = ";")

                         #Поиск значений, с двумя именами          
                        name_sextet_search1=' / PseudoVoigt sextet [simple] (57Fe)'
                        name_sextet_search2='PseudoVoigt sextet [simple] (57Fe)'

                         # Поиск мессбауэровских параметров
                        a1='δ / '+str_index_Sextet+name_sextet_search1
                        a2='ε / ' +str_index_Sextet+name_sextet_search1
                        a3='Hn / '+str_index_Sextet+name_sextet_search1
                        a4='Γ₁ / '+str_index_Sextet+name_sextet_search1
                        a5='I% / ' +str_index_Sextet+name_sextet_search2
                        a6='I₂/I₁ / '+str_index_Sextet+name_sextet_search1 #I2/I1
                        a7='I₃/I₁ / '+str_index_Sextet+name_sextet_search1 #I3/I1

                       # Поиск ошибок мессбауэровских параметров
                        a11='Δδ / '+str_index_Sextet+name_sextet_search1
                        a22='Δε / ' +str_index_Sextet+name_sextet_search1
                        a33='ΔHn / '+str_index_Sextet+name_sextet_search1
                        a44='ΔΓ₁ / '+str_index_Sextet+name_sextet_search1
                        a55='ΔI% / ' +str_index_Sextet+name_sextet_search2



                        # Считывание данных из CSV файла
                        for row in file_reader:
                            #Округляем данные: переводим строку в число и число в строку
                            row1=round(float(row[a1]),Okruglenie)
                            row11=round(float(row[a11]),Okruglenie)
                            String_row1=str(row1)
                            String_row11=str(row11)

                            row2=round(float(row[a2]),Okruglenie)
                            row22=round(float(row[a22]),Okruglenie)
                            String_row2=str(row2)
                            String_row22=str(row22)

                            row3=round(float(row[a3]),Okruglenie)
                            row33=round(float(row[a33]),Okruglenie)
                            String_row3=str(row3)
                            String_row33=str(row33)

                            row4=round(float(row[a4]),Okruglenie)
                            row44=round(float(row[a44]),Okruglenie)
                            String_row4=str(row4)
                            String_row44=str(row44)

                            row5=round(float(row[a5]),Okruglenie)
                            row55=round(float(row[a55]),Okruglenie)
                            String_row5=str(row5)
                            String_row55=str(row55)

                            row6=round(float(row[a6]),Okruglenie)                
                            String_row6=str(row6)

                            row7=round(float(row[a7]),Okruglenie)                
                            String_row7=str(row7)


                            Output_cicle_sextet=(f' Sextet {count_Sextet}	{String_row1}{"±"}{String_row11}	{String_row2}{"±"}{String_row22}	{String_row3}{"±"}{String_row33}	{String_row4}{"±"}{String_row44}	{String_row5}{"±"}{String_row55}	{String_row6}	{String_row7}\n')               
                        # Вывод строки, содержащей заголовки для столбцов
                        # Вывод строк всех
                    Output_Sextet+=Output_cicle_sextet   
                    count_Sextet+=1
                else:        
                    count_Sextet+=1
            #print(Output_Sextet)



            #Поиск дублета
            count_Doublet=1
            name_Doublet='PseudoVoigt doublet'
            str_count_Doublet=str(count_Doublet)

            while count_Doublet<16:
                str_count_Doublet=str(count_Doublet)
                search_doublet=str_count_Doublet+name_Doublet
                if re.search(search_doublet,filetext):
                    index_Doublet=count_Doublet
                    str_index_Doublet=str(index_Doublet)
                    with open(path_to_MS_spectra, encoding='utf-8') as r_file:
                        # Создаем объект DictReader, указываем символ-разделитель ","
                        file_reader = csv.DictReader(r_file, delimiter = ";")

                        name_doublet_search1=' / PseudoVoigt doublet'
                        name_doublet_search2='PseudoVoigt doublet'
                        a1_Doublet='δ / '+str_index_Doublet+name_doublet_search1
                        a2_Doublet='ε / ' +str_index_Doublet+name_doublet_search1            
                        a3_Doublet='Γ₁ / '+str_index_Doublet+name_doublet_search1
                        a4_Doublet='I% / ' +str_index_Doublet+name_doublet_search2
                        a5_Doublet='I₂/I₁ / '+str_index_Doublet+name_doublet_search1 #I2/I1

                        a11_Doublet='Δδ / '+str_index_Doublet+name_doublet_search1
                        a22_Doublet='Δε / ' +str_index_Doublet+name_doublet_search1            
                        a33_Doublet='ΔΓ₁ / '+str_index_Doublet+name_doublet_search1
                        a44_Doublet='ΔI% / ' +str_index_Doublet+name_doublet_search2

                        # Считывание данных из CSV файла
                        for row in file_reader:
                            #Округляем данные: переводим строку в число и число в строку
                            row1_Doublet=round(float(row[a1_Doublet]),Okruglenie)
                            row11_Doublet=round(float(row[a11_Doublet]),Okruglenie)
                            String_row1_Doublet=str(row1_Doublet)
                            String_row11_Doublet=str(row11_Doublet)

                            row2_Doublet=round(float(row[a2_Doublet]),Okruglenie)
                            row22_Doublet=round(float(row[a22_Doublet]),Okruglenie)
                            String_row2_Doublet=str(row2_Doublet)
                            String_row22_Doublet=str(row22_Doublet)

                            row3_Doublet=round(float(row[a3_Doublet]),Okruglenie)
                            row33_Doublet=round(float(row[a33_Doublet]),Okruglenie)
                            String_row3_Doublet=str(row3_Doublet)
                            String_row33_Doublet=str(row33_Doublet)

                            row4_Doublet=round(float(row[a4_Doublet]),Okruglenie)
                            row44_Doublet=round(float(row[a44_Doublet]),Okruglenie)
                            String_row4_Doublet=str(row4_Doublet)
                            String_row44_Doublet=str(row44_Doublet)

                            row5_Doublet=round(float(row[a5_Doublet]),Okruglenie)                
                            String_row5_Doublet=str(row5_Doublet)

                            Output_cicle_doublet=(f' Doublet {count_Doublet}	{String_row1_Doublet}{"±"}{String_row11_Doublet}	{String_row2_Doublet}{"±"}{String_row22_Doublet}	{"-"}	{String_row3_Doublet}{"±"}{String_row33_Doublet}	{String_row4_Doublet}{"±"}{String_row44_Doublet}	{String_row5_Doublet}\n')
                        # Вывод строки, содержащей заголовки для столбцов
                        # Вывод строк всех
                    Output_Doublet+=Output_cicle_doublet    
                    count_Doublet+=1
                else:        
                    count_Doublet+=1

            #PVSinglet

            count_Singlet=1
            name_Singlet='PseudoVoigt singlet'
            str_name_Singlet=str(count_Singlet)

            while count_Singlet<16:
                str_name_Singlet=str(count_Singlet)
                search_Singlet=str_name_Singlet+name_Singlet
                if re.search(search_Singlet,filetext):
                    index_Singlet=count_Singlet
                    str_index_Singlet=str(index_Singlet)
                    with open(path_to_MS_spectra, encoding='utf-8') as r_file:
                        # Создаем объект DictReader, указываем символ-разделитель ","
                        file_reader = csv.DictReader(r_file, delimiter = ";")

                        name_singlet_search1=' / PseudoVoigt singlet'
                        name_singlet_search2='PseudoVoigt singlet'
                        a1_Singlet='δ / '+str_index_Singlet+name_singlet_search1                       
                        a2_Singlet='Γ / '+str_index_Singlet+name_singlet_search1
                        a3_Singlet='I% / ' +str_index_Singlet+name_singlet_search2            

                        a11_Singlet='Δδ / '+str_index_Singlet+name_singlet_search1                       
                        a22_Singlet='ΔΓ / '+str_index_Singlet+name_singlet_search1
                        a33_Singlet='ΔI% / ' +str_index_Singlet+name_singlet_search2

                        # Считывание данных из CSV файла
                        for row in file_reader:
                            #Округляем данные: переводим строку в число и число в строку
                            row1_Singlet=round(float(row[a1_Singlet]),Okruglenie)
                            row11_Singlet=round(float(row[a11_Singlet]),Okruglenie)
                            String_row1_Singlet=str(row1_Singlet)
                            String_row11_Singlet=str(row11_Singlet)

                            row2_Singlet=round(float(row[a2_Singlet]),Okruglenie)
                            row22_Singlet=round(float(row[a22_Singlet]),Okruglenie)
                            String_row2_Singlet=str(row2_Singlet)
                            String_row22_Singlet=str(row22_Singlet)

                            row3_Singlet=round(float(row[a3_Singlet]),Okruglenie)
                            row33_Singlet=round(float(row[a33_Singlet]),Okruglenie)
                            String_row3_Singlet=str(row3_Singlet)
                            String_row33_Singlet=str(row33_Singlet)

                            Output_cicle_singlet=(f' Singlet {count_Singlet}	{String_row1_Singlet}{"±"}{String_row11_Singlet}	{"-"}	    {"-"}	{String_row2_Singlet}{"±"}{String_row22_Singlet}	{String_row3_Singlet}{"±"}{String_row33_Singlet}\n')
                        # Вывод строки, содержащей заголовки для столбцов
                        # Вывод строк всех
                    Output_Singlet+=Output_cicle_singlet    
                    count_Singlet+=1
                else:        
                    count_Singlet+=1







            # Поиск Распределения секстетов 
            count_Sextet_D=1
            name_Sextet_D=re.escape('[D] PseudoVoigt sextet [simple] (57Fe)') #ВНИМАНИЕ! Обязательно использовать re.escape так как в строке есть спец символы - [] и (). Я долго мучался
            str_count_Sextet_D=str(count_Sextet_D) 

            while count_Sextet_D<10:
                str_count_Sextet_D=str(count_Sextet_D) #Ищем 1PseudoVoigt sextet, если находим то index_Sextet равно цифре count_Sextet
                search_sextet_D=str_count_Sextet_D+name_Sextet_D
                if re.search(search_sextet_D,filetext):
                    index_Sextet_D=count_Sextet_D
                    str_index_Sextet_D=str(index_Sextet_D)
                    with open(path_to_MS_spectra, encoding='utf-8') as r_file:
                        # Создаем объект DictReader, указываем символ-разделитель ","
                        file_reader = csv.DictReader(r_file, delimiter = ";")

                         #Поиск значений, с двумя именами          
                        name_sextet_search1_D=' / [D] PseudoVoigt sextet [simple] (57Fe)'
                        name_sextet_search2_D='[D] PseudoVoigt sextet [simple] (57Fe)'

                         # Поиск мессбауэровских параметров
                        a1_D='δmax / '+str_index_Sextet_D+name_sextet_search1_D
                        a2_D='εmax / ' +str_index_Sextet_D+name_sextet_search1_D
                        a3_D='Hnmax / '+str_index_Sextet_D+name_sextet_search1_D
                        a4_D='Γ₁ / '+str_index_Sextet_D+name_sextet_search1_D
                        a5_D='I% / ' +str_index_Sextet_D+name_sextet_search2_D
                        a6_D='I₂/I₁ / '+str_index_Sextet_D+name_sextet_search1_D #I2/I1
                        a7_D='I₃/I₁ / '+str_index_Sextet_D+name_sextet_search1_D #I3/I1

                       # Поиск ошибок мессбауэровских параметров
                        a11_D='Δδmax / '+str_index_Sextet_D+name_sextet_search1_D
                        a22_D='Δεmax / ' +str_index_Sextet_D+name_sextet_search1_D
                        a33_D='ΔHnmax / '+str_index_Sextet_D+name_sextet_search1_D
                        a44_D='ΔΓ₁ / '+str_index_Sextet_D+name_sextet_search1_D
                        a55_D='ΔI% / ' +str_index_Sextet_D+name_sextet_search2_D



                        # Считывание данных из CSV файла
                        for row in file_reader:
                            #Округляем данные: переводим строку в число и число в строку
                            row1_D=round(float(row[a1_D]),Okruglenie)
                            row11_D=round(float(row[a11_D]),Okruglenie)
                            String_row1_D=str(row1_D)
                            String_row11_D=str(row11_D)

                            row2_D=round(float(row[a2_D]),Okruglenie)
                            row22_D=round(float(row[a22_D]),Okruglenie)
                            String_row2_D=str(row2_D)
                            String_row22_D=str(row22_D)

                            row3_D=round(float(row[a3_D]),Okruglenie)
                            row33_D=round(float(row[a33_D]),Okruglenie)
                            String_row3_D=str(row3_D)
                            String_row33_D=str(row33_D)

                            row4_D=round(float(row[a4_D]),Okruglenie)
                            row44_D=round(float(row[a44_D]),Okruglenie)
                            String_row4_D=str(row4_D)
                            String_row44_D=str(row44_D)

                            row5_D=round(float(row[a5_D]),Okruglenie)
                            row55_D=round(float(row[a55_D]),Okruglenie)
                            String_row5_D=str(row5_D)
                            String_row55_D=str(row55_D)

                            row6_D=round(float(row[a6_D]),Okruglenie)                
                            String_row6_D=str(row6_D)

                            row7_D=round(float(row[a7_D]),Okruglenie)                
                            String_row7_D=str(row7_D)


                            Output_cicle_sextet_D=(f' Sextet {count_Sextet_D}	{String_row1_D}{"±"}{String_row11_D}	{String_row2_D}{"±"}{String_row22_D}	{String_row3_D}{"±"}{String_row33_D}	{String_row4_D}{"±"}{String_row44_D}	{String_row5_D}{"±"}{String_row55_D}	{String_row6_D}	{String_row7_D}\n')               
                        # Вывод строки, содержащей заголовки для столбцов
                        # Вывод строк всех
                    Output_Sextet_D+=Output_cicle_sextet_D   
                    count_Sextet_D+=1
                else:        
                    count_Sextet_D+=1
            

            #Поиск распределения дублета
            count_Doublet_D=1
            name_Doublet_D=re.escape('[D] PseudoVoigt doublet') #ВНИМАНИЕ! Обязательно использовать re.escape так как в строке есть спец символы - [] и (). Я долго мучался
            str_count_Doublet_D=str(count_Doublet_D)

            while count_Doublet_D<16:
                str_count_Doublet_D=str(count_Doublet_D)
                search_doublet_D=str_count_Doublet_D+name_Doublet_D
                if re.search(search_doublet_D,filetext):
                    index_Doublet_D=count_Doublet_D
                    str_index_Doublet_D=str(index_Doublet_D)
                    with open(path_to_MS_spectra, encoding='utf-8') as r_file:
                        # Создаем объект DictReader, указываем символ-разделитель ","
                        file_reader = csv.DictReader(r_file, delimiter = ";")

                        name_doublet_search1_D=' / [D] PseudoVoigt doublet'
                        name_doublet_search2_D='[D] PseudoVoigt doublet'
                        a1_Doublet_D='δmax / '+str_index_Doublet_D+name_doublet_search1_D
                        a2_Doublet_D='εmax / ' +str_index_Doublet_D+name_doublet_search1_D            
                        a3_Doublet_D='Γ₁ / '+str_index_Doublet_D+name_doublet_search1_D
                        a4_Doublet_D='I% / ' +str_index_Doublet_D+name_doublet_search2_D
                        a5_Doublet_D='I₂/I₁ / '+str_index_Doublet_D+name_doublet_search1_D #I2/I1

                        a11_Doublet_D='Δδmax / '+str_index_Doublet_D+name_doublet_search1_D
                        a22_Doublet_D='Δεmax / ' +str_index_Doublet_D+name_doublet_search1_D            
                        a33_Doublet_D='ΔΓ₁ / '+str_index_Doublet_D+name_doublet_search1_D
                        a44_Doublet_D='ΔI% / ' +str_index_Doublet_D+name_doublet_search2_D

                        # Считывание данных из CSV файла
                        for row in file_reader:
                            #Округляем данные: переводим строку в число и число в строку
                            row1_Doublet_D=round(float(row[a1_Doublet_D]),Okruglenie)
                            row11_Doublet_D=round(float(row[a11_Doublet_D]),Okruglenie)
                            String_row1_Doublet_D=str(row1_Doublet_D)
                            String_row11_Doublet_D=str(row11_Doublet_D)

                            row2_Doublet_D=round(float(row[a2_Doublet_D]),Okruglenie)
                            row22_Doublet_D=round(float(row[a22_Doublet_D]),Okruglenie)
                            String_row2_Doublet_D=str(row2_Doublet_D)
                            String_row22_Doublet_D=str(row22_Doublet_D)

                            row3_Doublet_D=round(float(row[a3_Doublet_D]),Okruglenie)
                            row33_Doublet_D=round(float(row[a33_Doublet_D]),Okruglenie)
                            String_row3_Doublet_D=str(row3_Doublet_D)
                            String_row33_Doublet_D=str(row33_Doublet_D)

                            row4_Doublet_D=round(float(row[a4_Doublet_D]),Okruglenie)
                            row44_Doublet_D=round(float(row[a44_Doublet_D]),Okruglenie)
                            String_row4_Doublet_D=str(row4_Doublet_D)
                            String_row44_Doublet_D=str(row44_Doublet_D)

                            row5_Doublet_D=round(float(row[a5_Doublet_D]),Okruglenie)                
                            String_row5_Doublet_D=str(row5_Doublet_D)

                            Output_cicle_doublet_D=(f' Doublet {count_Doublet_D}	{String_row1_Doublet_D}{"±"}{String_row11_Doublet_D}	{String_row2_Doublet_D}{"±"}{String_row22_Doublet_D}	{"-"}	{String_row3_Doublet_D}{"±"}{String_row33_Doublet_D}	{String_row4_Doublet_D}{"±"}{String_row44_Doublet_D}	{String_row5_Doublet_D}\n')
                        # Вывод строки, содержащей заголовки для столбцов
                        # Вывод строк всех
                    Output_Doublet_D+=Output_cicle_doublet_D    
                    count_Doublet_D+=1
                else:        
                    count_Doublet_D+=1


            Result=Output_Hat+Output_Sextet+Output_Doublet+Output_Singlet+Output_Sextet_D+Output_Doublet_D+Output_Xi


            # Запись в файл
            # -*- coding: utf-8 -*-
            #import re;
            path_output = re.sub(r'.csv', '_output.csv', path_to_MS_spectra) #Поиск .txt в названии начального пути и последующая замена на _output.txt

            f = open(path_output, 'wb') #Создание файла с новым выходным путем
            f.write(bytes(Result, 'utf8')) #Запись каких нибудь значений например строку data
            f.close() #Обязательно закрываем

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())