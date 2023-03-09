from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, relatoryType):
        list_file = []
        if path.endswith(".csv"):
            with open(path) as file:
                reader = csv.DictReader(file)
                for item in reader:
                    list_file.append(item)
        if relatoryType == 'completo':
            return CompleteReport.generate(list_file)
        else:
            return SimpleReport.generate(list_file)
