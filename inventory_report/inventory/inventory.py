from csv import DictReader
from json import load
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def file_csv(cls, path):
        read_csv = DictReader(path, delimiter=",", quotechar='"')
        products_list = list(row for row in read_csv)
        return products_list

    @classmethod
    def file_json(cls, path):
        return load(path)

    @classmethod
    def file_xml(cls, path):
        xml = ET.parse(path).getroot()
        result = [
            {element.tag: element.text for element in document}
            for document in xml
        ]
        return result

    # Como ler arquivo xml em python
    # https://acervolima.com/ler-e-escrever-arquivos-xml-em-python/#:~:text=Lendo%20arquivos%20XML&text=Ent%C3%A3o%20peguei%20a%20raiz%20(tag,attrib%20.

    @classmethod
    def file_type(clas, file, path):
        if path.endswith(".csv"):
            return Inventory.file_csv(file)
        if path.endswith(".json"):
            return Inventory.file_json(file)
        if path.endswith(".xml"):
            return Inventory.file_xml(file)

    @classmethod
    def import_data(cls, path, report):
        with open(path, encoding="utf-8") as file:
            result = Inventory.file_type(file, path)
        file.close()

        if report.lower() == "simples":
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)
