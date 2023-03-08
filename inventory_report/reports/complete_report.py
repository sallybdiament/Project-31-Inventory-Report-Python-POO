from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista):
        company_name_dict = {}
        list_qty = ""

        for item in lista:
            if item['nome_da_empresa'] in company_name_dict:
                company_name_dict[item['nome_da_empresa']] += 1
            else:
                company_name_dict[item['nome_da_empresa']] = 1

        for key, value in company_name_dict.items():
            list_qty += f"- {key}: {value}\n"

        return (
            f"{SimpleReport.generate(lista)}"
            f"\nProdutos estocados por empresa:\n"
            f"{list_qty}"
        )
