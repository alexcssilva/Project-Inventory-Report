from datetime import date


class SimpleReport:

    @classmethod
    def generate(cls, products_list):
        old_date = min(
            [product["data_de_fabricacao"] for product in products_list]
        )

        next_date = min(
            [
                product["data_de_validade"]
                for product in products_list
                if product["data_de_validade"] >= str(date.today())
            ]
        )

        company_name = [
            product["nome_da_empresa"] for product in products_list
        ]

        biggest_product = max(set(company_name), key=company_name.count)

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {next_date}\n"
            f"Empresa com mais produtos: {biggest_product}"
        )
