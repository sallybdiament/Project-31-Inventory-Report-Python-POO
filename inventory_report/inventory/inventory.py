from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def read_xml_file(path):
        list_file = []
        with open(path) as file:
            readXML = ET.parse(file)
            iterableResult = readXML.getroot()
            for item in iterableResult:
                row = {}
                for line in item:
                    row[line.tag] = line.text
            list_file.append(row)
        return list_file

    @staticmethod
    def read_file(path):
        list_file = []
        if path.endswith(".csv"):
            with open(path) as file:
                readerCSV = csv.DictReader(file)
                for item in readerCSV:
                    list_file.append(item)
        elif path.endswith(".json"):
            with open(path) as file:
                list_file = json.load(file)
        else:
            list_file = Inventory.read_xml_file(path)
        return list_file

    @staticmethod
    def import_data(path, relatoryType):
        list_file = Inventory.read_file(path)
        if relatoryType == 'completo':
            return CompleteReport.generate(list_file)
        else:
            return SimpleReport.generate(list_file)
