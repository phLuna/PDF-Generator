from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.units import cm
from datetime import datetime

# Função para criar tabelas
def criar_tabela(dados, estilo=None, largura_colunas=None):
    tabela = Table(dados, colWidths=largura_colunas)
    if estilo:
        tabela.setStyle(estilo)
    return tabela

def gerar_pdf(
        nome_arquivo: str,
        ano=datetime.now().year,
        
        # Relacionado ao cliente.
        nome_cliente: str='',
        tipo_de_contrato: str='',
        horas_mensais: int=0,
        horas_trimestrais: int=0,
        valor_mensal: int=0,
        valor_hora: int=0,
        valor_hora_adicional_cliente: int=0,

        # Relacionado ao mês.
        mes: str='',
        chamados: int=0,
        horas_utilizadas_mes: int=0,

        # Relacionado ao trimestre.
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

        # Relacionado ao faturamento.
        valor_mensal_faturamento: int=0,
        serviços_adicionais_ou_peças: int=0,
        valor_de_horas_adicionais_do_trimestre_anterior: int=0
        ) -> None:
    """Uma função para gerar um arquivo PDF."""

    # Configuração do documento
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4, leftMargin=15, rightMargin=15, topMargin=30, bottomMargin=0)
    elements = []
    
    # Estilos de texto
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']
    estilo_texto_centralizado = ParagraphStyle(
        'Centralizado',
        parent=estilos['BodyText'],
        alignment=1 # 1 centraliza
    )
    estilo_normal = estilos['BodyText']

    # Título
    titulo = "Relatório de gerenciamento de chamados"
    paragrafo_titulo = Paragraph(titulo, estilo_titulo)
    elements.append(paragrafo_titulo)
    elements.append(Spacer(1, 12))

    # Introdução
    texto = f'{mes} de {ano}'
    paragrafo_texto = Paragraph(texto, estilo_texto_centralizado)
    elements.append(paragrafo_texto)
    elements.append(Spacer(1, 12))

    # Cabeçalho/tabela do cliente
    dados_cliente = [
        [Paragraph(f'Cliente: {nome_cliente}', estilo_normal)],
        ['Tipo de Contrato:', Paragraph(f'{tipo_de_contrato}', estilo_normal)],
        ['Horas Mensais:', Paragraph(f'{horas_mensais} horas mensais, {horas_trimestrais} horas trimestrais.', estilo_normal)],
        ['Valor mensal:', Paragraph(f'R${valor_mensal}', estilo_normal)],
        ['Valor hora:', Paragraph(f'R${valor_hora}', estilo_normal)],
        ['Valor hora adicional:', Paragraph(f'R${valor_hora_adicional_cliente}', estilo_normal)]
    ]
    estilo_cliente = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')
    ])
    largura_cliente = [5 * cm, 14. * cm]  # Largura
    tabela_cliente = criar_tabela(dados_cliente, estilo_cliente, largura_cliente)
    tabela_cliente.hAlign = 'LEFT'

    # Primeira tabela - Mês
    dados_tabela_mes = [
        [Paragraph(f'{mes}', estilo_normal)],
        [Paragraph(f'{mes}', estilo_normal), Paragraph('Quantidade', estilo_normal)],
        [Paragraph('Chamados', estilo_normal), Paragraph(f'{chamados}', estilo_normal)],
        [Paragraph('Horas utilizadas', estilo_normal), Paragraph(f'{horas_utilizadas_mes}', estilo_normal)]
    ]
    estilo_tabela_mes = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold')
    ])
    largura_mes = [4 * cm, 4 * cm]
    tabela_mes = criar_tabela(dados_tabela_mes, estilo_tabela_mes, largura_mes)
    tabela_mes.hAlign = 'LEFT'

    # Segunda tabela - Trimestre
    dados_tabela_trimestre_1 = [
        [Paragraph('Trimestre', estilo_normal)],
        [Paragraph('Mês', estilo_normal), Paragraph(f'{mes_1}', estilo_normal), Paragraph(f'{mes_2}', estilo_normal), Paragraph(f'{mes_3}', estilo_normal), Paragraph('Tempo Total', estilo_normal)],
        [Paragraph('Horas', estilo_normal), Paragraph(f'{horas_mes_1}', estilo_normal), Paragraph(f'{horas_mes_2}', estilo_normal), Paragraph(f'{horas_mes_3}', estilo_normal), Paragraph(f'{horas_mes_1 + horas_mes_2 + horas_mes_3}', estilo_normal)]
    ]
    estilo_tabela_trimestre_1 = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold')
    ])
    largura_trimestre_1 = [1.5 * cm, 2 * cm, 2 * cm, 2 * cm, 3 * cm]
    tabela_trimestre_1 = criar_tabela(dados_tabela_trimestre_1, estilo_tabela_trimestre_1, largura_trimestre_1)

    dados_tabela_trimestre_2 = [
        [Paragraph('Horas Contratadas', estilo_normal), Paragraph(f'{horas_contratadas}', estilo_normal)],
        [Paragraph('Horas utilizadas', estilo_normal), Paragraph(f'{horas_utilizadas_trimestre}', estilo_normal)],
        [Paragraph('Saldo', estilo_normal), Paragraph(f'{saldo}', estilo_normal)],
        [Paragraph('Valor hora adicional', estilo_normal), Paragraph(f'R${valor_hora_adicional_trimestre}', estilo_normal)],
        [Paragraph('Adicional de horas', estilo_normal), Paragraph(f'R${adicional_de_horas_trimestre}', estilo_normal)]
    ]
    estilo_tabela_trimestre_2 = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 2), (-1, 2), 'Helvetica-Bold'),
    ])
    largura_trimestre_2 = [5 * cm, 5 * cm]  # Ajustando a largura
    tabela_trimestre_2 = criar_tabela(dados_tabela_trimestre_2, estilo_tabela_trimestre_2, largura_trimestre_2)

    # Template com as tabelas dentro
    dados_template = [
        [tabela_cliente],
        [tabela_mes, tabela_trimestre_1],
        ['', tabela_trimestre_2]
    ]
    estilo_template = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    largura_template = [10 * cm, 10 * cm]  # Largura
    tabela_template = criar_tabela(dados_template, estilo_template, largura_template)
    elements.append(tabela_template)
    elements.append(Spacer(1, 12))

    # Terceira tabela - Faturamento
    dados_tabela_faturamento = [
        [Paragraph('Faturamento', estilo_normal)],
        [Paragraph('Valor mensal', estilo_normal), Paragraph(f'R${valor_mensal_faturamento}', estilo_normal)],
        [Paragraph('Serviços adicionais / peças', estilo_normal), Paragraph(f'R${serviços_adicionais_ou_peças}', estilo_normal)],
        [Paragraph('Valor de horas adicionais do trimestre anterior', estilo_normal), Paragraph(f'R${valor_de_horas_adicionais_do_trimestre_anterior}', estilo_normal)],
        [Paragraph('Total geral', estilo_normal), Paragraph(f'R${valor_mensal_faturamento + serviços_adicionais_ou_peças + valor_de_horas_adicionais_do_trimestre_anterior}', estilo_normal)]
    ]
    estilo_tabela_faturamento = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 4), (-1, 5), 'Helvetica-Bold')
    ])
    largura_faturamento = [8 * cm]  # Ajustando a largura para ficar centralizado
    tabela_faturamento = criar_tabela(dados_tabela_faturamento, estilo_tabela_faturamento, largura_faturamento)
    elements.append(tabela_faturamento)

    # Criar o documento
    doc.build(elements)

#Exemplo de chamada da função com parâmetros fictícios
gerar_pdf(
    nome_arquivo = 'relatorio.pdf',
    nome_cliente = 'Cliente XYZ',
    tipo_de_contrato = 'Contrato PCH',
    horas_mensais = 120,
    horas_trimestrais = 360,
    valor_mensal = 1000,
    valor_hora = 50,
    valor_hora_adicional_cliente = 75,
    mes = 'Janeiro',
    chamados = 10,
    horas_utilizadas_mes = 100,
    mes_1 = 'Janeiro',
    horas_mes_1 = 100,
    mes_2 = 'Fevereiro',
    horas_mes_2 = 110,
    mes_3 = 'Março',
    horas_mes_3 = 120,
    horas_contratadas = 360,
    horas_utilizadas_trimestre = 330,
    saldo = 30,
    valor_hora_adicional_trimestre = 80,
    adicional_de_horas_trimestre = 1600,
    valor_mensal_faturamento = 1000,
    serviços_adicionais_ou_peças = 200,
    valor_de_horas_adicionais_do_trimestre_anterior = 300
)