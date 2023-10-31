import os
from zipfile import ZipFile
import psutil
from xml.dom import minidom
import json
import xml.etree.ElementTree as ET

class FileTxt:
    "Файлы TXT"
    def __init__(self):
        self.txtfilename = ""
    def txtpath(self):
        print("Введите название текстового файла и его тип: ")
        self.txtfilename = str(input())
        return self.txtfilename
    def createtxtfile(self):
        file = open(self.txtfilename, "w")
        file.close()
    def stringtxtfile(self):
        print("Введите строку:")
        string = str(input())
        file = open(self.txtfilename, "w")
        file.write(string)
        file.close()
    def consoletxtfile(self):
        file = open(self.txtfilename, "r")
        print(file.read())
        file.close()

class FileXml(object):
    "Файлы XML"
    def __init__(self):
        self.xmlfilename = ""
    def xmlpath(self):
        print("Введите название xml-файла и его тип: ")
        self.xmlfilename = str(input())
        return self.xmlfilename
    def xmlread(self):
        mydoc = minidom.parse(self.xmlfilename)
        titles = mydoc.getElementsByTagName('title')
        for elem in titles:
            print(elem.firstChild.data)
    def xmldata(self):
        tree = ET.parse(self.xmlfilename)
        root = tree.getroot()
        new_data = input("Введите новые данные для XML (в формате 'элемент:значение'): ")
        element, value = new_data.split(':')
        new_element = ET.SubElement(root, element.strip())
        new_element.text = value.strip()
        tree.write(self.xmlfilename)
        print("Новые данные успешно добавлены в XML-файл.")
class FileJson(object):
    "Файлы JSON"
    def __init__(self):
        self.jsonfilename = ""
    def jsonpath(self):
        print("Введите название json-файла и его тип: ")
        self.jsonfilename = str(input())
        return self.jsonfilename
    def jsonread(self):
        with open(self.jsonfilename, 'r', encoding='utf-8') as f:
            text = json.load(f)
            print(text)

    def jsonobject(self):
        print("Введите новый объект: ")
        new_data = str(input())
        with open(self.jsonfilename, encoding='utf8') as f:
            data = json.load(f)
        data['personal'].append(new_data)
        with open(self.jsonfilename, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)

class FileZip(object):
    "Архивы ZIP"
    def __init__(self):
        self.zipfilename = ""
        self.filename = ""
    def zippath(self):
        print("Введите название zip-архива: ")
        self.zipfilename = str(input())
        return self.zipfilename
    def filenamepath(self):
        print("Введите название файла, которое хотите добавить в архив: ")
        self.filename = str(input())
        return self.filename
    def addfile(self):
        with ZipFile(self.zipfilename, "w") as myzip:
            myzip.write(self.filename)
    def createzipfile(self):
        myzip = ZipFile(self.zipfilename, "w")
        myzip.close()
    def extractfile(self):
        with ZipFile(self.filename, "a") as myzip:
            print(myzip.infolist())
            myzip.extractall()


while True:
    print("1. Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы \n"
          "2. Работа с файлами \n"
          "3. Работа с форматом JSON \n"
          "4. Работа с форматорм XML \n"
          "5. Создание zip архива, добавление туда файла, определение размера архива")
    n = int(input())
    if n == 1:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"Диск {partition.device}:")
            print(f"\tТочка монтирования: {partition.mountpoint}")
            print(f"\tФайловая система: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            print(f"\tОбщий объем: {partition_usage.total / (1024 * 1024 * 1024):.2f} ГБ")
            print(f"\tИспользовано: {partition_usage.used / (1024 * 1024 * 1024):.2f} ГБ")
            print(f"\tСвободно: {partition_usage.free / (1024 * 1024 * 1024):.2f} ГБ")
            print(f"\tПроцент использования: {partition_usage.percent}%")
    elif n == 2:
        txtfile = FileTxt()
        print("1. Создать файл \n"
              "2. Записать в файл строку, введённую пользователем \n"
              "3. Прочитать файл в консоль \n"
              "4. Удалить файл")
        m = int(input())
        if m == 1:
            txtfile.txtpath()
            txtfile.createtxtfile()
        if m == 2:
            txtfile.txtpath()
            txtfile.stringtxtfile()
        if m == 3:
            txtfile.txtpath()
            txtfile.consoletxtfile()
        if m == 4:
            os.remove(txtfile.txtpath())
    elif n == 3:
        jsonfile = FileJson()
        print("1. Создать файл формате JSON в любом редакторе или с использованием данных, введенных пользовователем \n"
              "2. Создать новый объект. Выполнить сериализацию объекта в формате JSON и записывать в файл \n"
              "3. Прочитать файл в консоль \n"
              "4. Удалить файл")
        m = int(input())
        if m == 1:
            print()
        if m == 2:
            jsonfile.jsonpath()
            jsonfile.jsonobject()
        if m == 3:
            jsonfile.jsonpath()
            jsonfile.jsonread()
        if m == 4:
            os.remove(jsonfile.jsonpath())
    elif n == 4:
        xmlfile = FileXml()
        print("1. Создать файл в формате XML из редактора \n"
              "2. Записать в файл новые данные из консоли \n"
              "3. Прочитать файл в консоль \n"
              "4. Удалить файл")
        m = int(input())
        if m == 1:
            print()
        if m == 2:
            xmlfile.xmlpath()
            xmlfile.xmldata()
        if m == 3:
            xmlfile.xmlpath()
            xmlfile.xmlread()
        if m == 4:
            os.remove(xmlfile.xmlpath())
    elif n == 5:
        zipfile = FileZip()
        print("1. Создать архив в формате zip \n"
              "2. Добавить файл, выбранный пользователем, в архив \n"
              "3. Разархивировать файл и вывести данныне о нём \n"
              "4. Удалить файл и архив")
        m = int(input())
        if m == 1:
            zipfile.zippath()
            zipfile.createzipfile()
        if m == 2:
            zipfile.zippath()
            zipfile.filenamepath()
            zipfile.addfile()
        if m == 3:
            zipfile.zippath()
            zipfile.filenamepath()
            zipfile.extractfile()
        if m == 4:
            os.remove(zipfile.zippath())




