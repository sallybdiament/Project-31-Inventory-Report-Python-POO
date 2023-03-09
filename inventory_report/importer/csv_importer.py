from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        list_file = []
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            readerCSV = csv.DictReader(file)
            for item in readerCSV:
                list_file.append(item)
        return list_file
