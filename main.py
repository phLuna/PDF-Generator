from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

def gerar_pdf(
        nome_arquivo: str,
        
        #Relacionado ao cliente.
        nome_cliente: str='',
        horas_mensais: int=0,
        horas_trimestrais: int=0,
        valor_mensal: int=0,
        valor_hora: int=0,
        valor_hora_adicional_cliente: int=0,


        #Relacionado ao mês.
        mes: str='',
        quantidade_mes: int=0,
        chamados: int=0,
        horas_utilizadas_mes: int=0,


        #Relacionado ao trimestre.
        mes_1: str='',
        horas_mes_1: int=0,
        mes_2: str='',
        horas_mes_2: int=0,
        mes_3: str='',
        horas_mes_3: int=0,

        horas_contratadas: int=0,
        horas_utilizadas_trimestre: int=0,
        saldo: int=0,
        valor_hora_adicional_trimestre: int=0,
        adicional_de_horas_trimestre: int=0,

        #Relacionado ao faturamento.
        valor_mensal_faturamento: int=0,
        serviços_adicionais_ou_peças: int=0,
        valor_de_horas_adicionais_do_trimestre_anterior: int=0
        ) -> None:
    
    """Uma função para gerar um arquivo PDF."""
    #Configuração do documento
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
    elements = []
    
    #Estilos de texto.
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']

    #Título.
    titulo = "Relatório de gerenciamento de chamados"
    paragrafo_titulo = Paragraph(titulo, estilo_titulo)
    elements.append(paragrafo_titulo)
    
    #Função para criar tabelas
    def criar_tabela(dados, estilo=None):
        tabela = Table(dados)
        if estilo:
            tabela.setStyle(estilo)
        return tabela

    #Cabeçalho/tabela do cliente.
    dados_cliente = [[f'Cliente: {nome_cliente}'], ['Horas Mensais:', f'{horas_mensais} horas mensais, {horas_trimestrais} horas trimestrais.'], ['Valor mensal:', f'R${valor_mensal}'], ['Valor hora:', f'R${valor_hora}',], ['Valor hora adicional:', f'R${valor_hora_adicional_cliente}']]
    estilo_cliente = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.blue), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_cliente, estilo_cliente))
    elements.append(Spacer(1, 12))

    #Primeira tabela.
    dados_tabela_1 = [[f'{mes}'], [f'{mes}', f'{quantidade_mes}'], ['Chamados', f'{chamados}'], ['Horas utilizadas', f'{horas_utilizadas_mes}']]
    estilo_tabela_1 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.blue), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_tabela_1, estilo_tabela_1))
    elements.append(Spacer(1, 12))

    #Segunda tabela - Dividida em duas.
    dados_tabela_2_1 = [['Trimestre'], [f'Mês', f'{mes_1}', f'{mes_2}', f'{mes_3}', 'Tempo Total'], ['Horas', f'{horas_mes_1}', f'{horas_mes_2}', f'{horas_mes_3}', f'{horas_mes_1 + horas_mes_2 + horas_mes_3}']]
    dados_tabela_2_2 = [['Horas Contratadas', f'{horas_contratadas}'], ['Horas utilizadas', f'{horas_utilizadas_trimestre}'], ['Saldo', f'{saldo}'], ['Valor hora adicional', f'R${valor_hora_adicional_trimestre}'], ['Adicional de horas', f'R${adicional_de_horas_trimestre}']]
    estilo_tabela_2_1 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.blue), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    estilo_tabela_2_2 = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])


    elements.append(criar_tabela(dados_tabela_2_1, estilo_tabela_2_1))
    elements.append(Spacer(1, 12))
    elements.append(criar_tabela(dados_tabela_2_2, estilo_tabela_2_2))
    elements.append(Spacer(1, 12))

    #Terceira tabela.
    dados_tabela_3 = [['Faturamento'], ['Valor mensal', f'R${valor_mensal_faturamento}'], ['Serviços adicionais / peças', f'R${serviços_adicionais_ou_peças}'], ['Valor de horas adicionais do trimestre anterior', f'R${valor_de_horas_adicionais_do_trimestre_anterior}'], ['Total geral', f'R${valor_mensal_faturamento + serviços_adicionais_ou_peças + valor_de_horas_adicionais_do_trimestre_anterior}']]
    estilo_tabela_3 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.blue), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_tabela_3, estilo_tabela_3))
    elements.append(Spacer(1, 12))

    #Criar o documento.
    doc.build(elements)

gerar_pdf('arquivo.pdf')