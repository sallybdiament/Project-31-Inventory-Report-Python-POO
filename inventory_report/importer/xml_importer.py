from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
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
