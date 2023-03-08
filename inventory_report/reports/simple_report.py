class SimpleReport:

    @staticmethod
    def generate(cls, lista):
        company_name_dict = {}
        fabr_date = []
        valid_date = []

        for item in lista:
            if item['nome_da_empresa'] in company_name_dict:
                company_name_dict[item['nome_da_empresa']] += 1
            else:
                company_name_dict[item['nome_da_empresa']] = 1
            fabr_date.append(item['data_de_fabricacao'])
            valid_date.append(item['data_de_fabricacao'])

        max_company = max(company_name_dict, key=company_name_dict.get)
        oldest_fabr_date = min(fabr_date)
        max_valid_date = max(valid_date)

        return (
            f"Data de fabricação mais antiga: {oldest_fabr_date}\n"
            f"Data de validade mais próxima: {max_valid_date}\n"
            f"Empresa com mais produtos: {max_company}.\n"
        )
