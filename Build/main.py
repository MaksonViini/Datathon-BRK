import pandas as pd
priority_columns = ['index',
                    'Município',
                    'Parcela das moradias sem banheiro de uso exclusivo (% das habitações) (IBGE)',
                    'Parcela da população que não recebe água com regularidade adequada (%) (% da população) (IBGE)',
                    'Parcela da população total que mora em domicílios sem acesso à água tratada (% da população) (SNIS)',
                    'Volume de água consumida per capita (litros diários por pessoa) (SNIS)',
                    'Volume de esgoto coletado (mil m³) (SNIS)',
                    'Volume de esgoto tratado (mil m³) (SNIS)',
                    'Volume de esgoto não tratado (água consumida - esgoto tratado) (mil m³) (SNIS)',
                    'Tarifa média de água, em R$ por m³ (R$/m³) (SNIS)',
                    'Tarifa média de coleta de esgoto, em R$ por m³ (R$/m³) (SNIS)',
                    'Tarifa média ponderada dos serviços de saneamento, em R$ por m³ (R$/m³) (SNIS)',
                    'Custo total dos operadores com os serviços de saneamento, em R$ (R$) (SNIS)',
                    'Custo total dos operadores com produtos químicos, em R$ (R$) (SNIS)',
                    'Custo total dos operadores com energia elétrica, em R$ (R$) (SNIS)',
                    'Internações por doenças associadas à falta de saneamento (Número de internações) (DATASUS)',
                    'Taxa de incidência de internações por doenças associadas à falta de saneamento (Internações por 10 mil habitantes) (DATASUS)',
                    'Atraso escolar das pessoas que moram em residências com saneamento básico (Anos de atraso na educação) (IBGE)',
                    'Atraso escolar das pessoas que moram em residências sem saneamento (Anos de atraso na educação) (IBGE)',
                    'Investimentos per capita em saneamento, em R$ de 2019 (R$ a preços de 2019) (ITB)',
                    'Renda induzida gerada pelas operação de saneamento, em R$ a preços de 2019 (R$ a preços de 2019) (ITB)',
                    'Renda total gerada pelas operação de saneamento, em R$ a preços de 2019 (R$ a preços de 2019) (ITB)',
                    'Redução dos custos com a saúde, em R$ milhões a preços de 2017, média anual de 2017 a 2037 (R$ milhões a preços de 2017) (ITB)',
                    ]

priority_rename = ['Ano',
                   'Município',
                   'Parcela das moradias sem banheiro de uso exclusivo',
                   'Parcela da população que não recebe água com regularidade adequada',
                   'Parcela da população total que mora em domicílios sem acesso à água tratada',
                   'Volume de água consumida per capita',
                   'Volume de esgoto coletado',
                   'Volume de esgoto tratado',
                   'Volume de esgoto não tratado',
                   'Tarifa média de água',
                   'Tarifa média de coleta de esgoto',
                   'Tarifa média ponderada dos serviços de saneamento',
                   'Custo total dos operadores com os serviços de saneamento',
                   'Custo total dos operadores com produtos químicos',
                   'Custo total dos operadores com energia elétrica',
                   'Internações por doenças associadas à falta de saneamento',
                   'Taxa de incidência de internações por doenças associadas à falta de saneamento',
                   'Atraso escolar das pessoas que moram em residências com saneamento básico',
                   'Atraso escolar das pessoas que moram em residências sem saneamento',
                   'Investimentos per capita em saneamento',
                   'Renda induzida gerada pelas operação de saneamento',
                   'Renda total gerada pelas operação de saneamento',
                   'Redução dos custos com a saúde',
                   ]


def transform_datasets():
    columns = []
    [columns.append(x.replace(' ', '_')) for x in priority_rename]
    data = pd.read_excel(
        '/home/maksonvinicio/Documents/GitHub/Datathon-BRK/Data/839_municipios_retornados/110011.xlsx', header=1,)

    data.loc[-1] = 'Município'
    data.loc[-1][data.columns[1::]] = data.columns[0]

    data_pivot = data.T
    data_pivot.columns = data_pivot.iloc[0, :]
    data_pivot = data_pivot.drop(data_pivot.index[0]).reset_index()

    data_pivot = data_pivot[priority_columns]
    data_pivot.columns = columns
    data_pivot['Ano'] = [2019, 2018, 2017, 2016,
                         2015, 2014, 2013, 2012, 2011, 2010]
    data_pivot.to_csv('Data/110011.csv', index=False)


if __name__ == '__main__':
    transform_datasets()
