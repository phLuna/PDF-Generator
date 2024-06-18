from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

def gerar_pdf(nome_arquivo):
    # Configuração do documento
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
    elements = []
    
    # Estilos de texto
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']

    # Cabeçalho com título e cinco informações
    titulo = "Relatório de gerenciamento de chamados"
    paragrafo_titulo = Paragraph(titulo, estilo_titulo)
    elements.append(paragrafo_titulo)
    
    # Função para criar tabelas
    def criar_tabela(dados, estilo=None):
        tabela = Table(dados)
        if estilo:
            tabela.setStyle(estilo)
        return tabela

    # Cabeçalho do cliente.
    dados_cliente = [['Cliente:', '[NOME]'], ['Horas Mensais:', '[HORAS]'], ['Valor mensal:', '[VALOR]'], ['Valor hora:', '[VALOR]]',], ['Valor hora adicional:', '[VALOR]]']]
    estilo_cliente = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_cliente, estilo_cliente))
    elements.append(Spacer(1, 12))

    # Primeira tabela
    dados_tabela_1 = [['Março'], ['Março', 'Quantidade'], ['Chamados', '40'], ['Horas utilizadas', '19.11']]
    estilo_tabela_1 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_tabela_1, estilo_tabela_1))
    elements.append(Spacer(1, 12))

    # Segunda tabela - Dividida em duas
    dados_tabela_2_1 = [['Trimestre'], ['Mês', 'Janeiro', 'Fevereiro', 'Março', 'Tempo total'], ['Horas', '39.99', '17.6', '19,11', '76,70']]
    dados_tabela_2_2 = [['Horas Contratadas', '90'], ['Horas utilizadas', '76.70'], ['Saldo', '13,3'], ['Valor hora adicional', 'R$99,00'], ['Adicional de horas', 'R$0,00']]
    estilo_tabela_2_1 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    estilo_tabela_2_2 = TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])


    elements.append(criar_tabela(dados_tabela_2_1, estilo_tabela_2_1))
    elements.append(Spacer(1, 12))
    elements.append(criar_tabela(dados_tabela_2_2, estilo_tabela_2_2))
    elements.append(Spacer(1, 12))

    # Terceira tabela
    dados_tabela_3 = [['Faturamento'], ['Valor mensal', 'R$2.700,00'], ['Serviços adicionais / peças', 'R$0,00'], ['Valor de horas adicionais do trimestre anterior', 'R$0,00'], ['Total geral', 'R$2.700,00']]
    estilo_tabela_3 = TableStyle([('SPAN', (0, 0), (-1, 0)), ('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    elements.append(criar_tabela(dados_tabela_3, estilo_tabela_3))
    elements.append(Spacer(1, 12))

    # Construir o documento
    doc.build(elements)

# Chamando a função para gerar o PDF
gerar_pdf("arquivo.pdf")
