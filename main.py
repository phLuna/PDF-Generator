from reportlab.lib.pagesizes import A3
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
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A3)
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
    
    estilo_negrito = estilos['Normal']
    estilo_negrito.fontName = 'Helvetica-Bold'
    estilo_negrito.alignment = 1

    # Título
    titulo = "Relatório de gerenciamento de chamados"
    paragrafo_titulo = Paragraph(titulo, estilo_titulo)
    elements.append(paragrafo_titulo)

    # Introdução
    texto = f'{mes} de {ano}'
    paragrafo_texto = Paragraph(texto, estilo_texto_centralizado)
    elements.append(paragrafo_texto)
    elements.append(Spacer(1, 12))

    # Cabeçalho/tabela do cliente
    dados_cliente = [
    [Paragraph(f'Cliente: {nome_cliente}', estilo_normal)],
    ['Tipo de Contrato:', Paragraph(f'{tipo_de_contrato}')],
    ['Horas Mensais:', Paragraph(f'{horas_mensais} horas mensais, {horas_trimestrais} horas trimestrais.')],
    ['Valor mensal:', Paragraph(f'R${valor_mensal}')],
    ['Valor hora:', Paragraph(f'R${valor_hora}')],
    ['Valor hora adicional:', Paragraph(f'R${valor_hora_adicional_cliente}')]
    ]
    estilo_cliente = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold')
    ])
    largura_cliente = [5 * cm, 22 * cm]
    tabela_cliente = criar_tabela(dados_cliente, estilo_cliente, largura_cliente)
    tabela_cliente.hAlign = 'LEFT'

    # Primeira tabela - Mês
    dados_tabela_mes = [
        [Paragraph(f'{mes}', estilo_texto_centralizado)],
        [Paragraph(f'{mes}', estilo_negrito), Paragraph('Quantidade', estilo_negrito)],
        [Paragraph('Chamados', estilo_texto_centralizado), Paragraph(f'{chamados}', estilo_texto_centralizado)],
        [Paragraph('Horas utilizadas', estilo_texto_centralizado), Paragraph(f'{horas_utilizadas_mes}', estilo_texto_centralizado)]
    ]
    estilo_tabela_mes = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    largura_mes = [6.7 * cm, 6.7 * cm]
    tabela_mes = criar_tabela(dados_tabela_mes, estilo_tabela_mes, largura_mes)

    # Segunda tabela - Trimestre
    dados_tabela_trimestre_1 = [
        [Paragraph('Trimestre', estilo_texto_centralizado)],
        [Paragraph('Mês', estilo_negrito), Paragraph(f'{mes_1}', estilo_negrito), Paragraph(f'{mes_2}', estilo_negrito), Paragraph(f'{mes_3}', estilo_negrito), Paragraph('Tempo Total', estilo_negrito)],
        [Paragraph('Horas', estilo_texto_centralizado), Paragraph(f'{horas_mes_1}', estilo_texto_centralizado), Paragraph(f'{horas_mes_2}', estilo_texto_centralizado), Paragraph(f'{horas_mes_3}', estilo_texto_centralizado), Paragraph(f'{horas_mes_1 + horas_mes_2 + horas_mes_3}', estilo_texto_centralizado)]
    ]
    estilo_tabela_trimestre_1 = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold')
    ])
    largura_trimestre_1 = [1.9 * cm, 2.4 * cm, 2.4 * cm, 2.4 * cm, 3.4 * cm]
    tabela_trimestre_1 = criar_tabela(dados_tabela_trimestre_1, estilo_tabela_trimestre_1, largura_trimestre_1)

    dados_tabela_trimestre_2 = [
        [Paragraph('Horas Contratadas', estilo_texto_centralizado), Paragraph(f'{horas_contratadas}', estilo_texto_centralizado)],
        [Paragraph('Horas utilizadas', estilo_texto_centralizado), Paragraph(f'{horas_utilizadas_trimestre}', estilo_texto_centralizado)],
        [Paragraph('Saldo', estilo_negrito), Paragraph(f'{saldo}', estilo_texto_centralizado)],
        [Paragraph('Valor hora adicional', estilo_texto_centralizado), Paragraph(f'R${valor_hora_adicional_trimestre}', estilo_texto_centralizado)],
        [Paragraph('Adicional de horas', estilo_texto_centralizado), Paragraph(f'R${adicional_de_horas_trimestre}', estilo_texto_centralizado)]
    ]
    estilo_tabela_trimestre_2 = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
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
        ('ALIGN', (0, 0), (-1, 3), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),
    ])
    largura_template = [14 * cm, 14 * cm]
    tabela_template = criar_tabela(dados_template, estilo_template, largura_template)
    elements.append(tabela_template)
    elements.append(Spacer(1, 12))

    # Terceira tabela - Faturamento
    dados_tabela_faturamento = [
        [Paragraph('Faturamento', estilo_texto_centralizado)],
        [Paragraph('Valor mensal', estilo_texto_centralizado), Paragraph(f'R${valor_mensal_faturamento}', estilo_texto_centralizado)],
        [Paragraph('Serviços adicionais / peças', estilo_texto_centralizado), Paragraph(f'R${serviços_adicionais_ou_peças}', estilo_texto_centralizado)],
        [Paragraph('Valor de horas adicionais do trimestre anterior', estilo_texto_centralizado), Paragraph(f'R${valor_de_horas_adicionais_do_trimestre_anterior}', estilo_texto_centralizado)],
        [Paragraph('Total geral', estilo_negrito), Paragraph(f'R${valor_mensal_faturamento + serviços_adicionais_ou_peças + valor_de_horas_adicionais_do_trimestre_anterior}', estilo_negrito)]
    ]
    estilo_tabela_faturamento = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 4), (-1, 5), 'Helvetica-Bold'),
    ])
    largura_faturamento = [12 * cm]
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