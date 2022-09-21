from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        simple_report = SimpleReport.generate(products_list)

        product_quantity = ""

        company_name = [
            company["nome_da_empresa"] for company in products_list
        ]

        company_quantity = dict(Counter(company_name))

        for company, quantity in company_quantity.items():
            product_quantity += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{product_quantity}"
        )
