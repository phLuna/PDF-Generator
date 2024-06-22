from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Frame, PageTemplate
from reportlab.lib.units import cm  # Importando a unidade de medida cm

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
    
    #Estilos de texto
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']

    #Título
    titulo = "Relatório de gerenciamento de chamados"
    paragrafo_titulo = Paragraph(titulo, estilo_titulo)
    elements.append(paragrafo_titulo)
    elements.append(Spacer(1, 12))
    
    #Função para criar tabelas
    def criar_tabela(dados, estilo=None, largura_colunas=None):
        tabela = Table(dados, colWidths=largura_colunas)
        if estilo:
            tabela.setStyle(estilo)
        return tabela

    #Cabeçalho/tabela do cliente
    dados_cliente = [
        [f'Cliente: {nome_cliente}'],
        ['Horas Mensais:', f'{horas_mensais} horas mensais, {horas_trimestrais} horas trimestrais.'],
        ['Valor mensal:', f'R${valor_mensal}'],
        ['Valor hora:', f'R${valor_hora}'],
        ['Valor hora adicional:', f'R${valor_hora_adicional_cliente}']
    ]
    estilo_cliente = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.white)
    ])
    largura_cliente = [5 * cm, 13 * cm]  #Largura
    tabela_cliente = criar_tabela(dados_cliente, estilo_cliente, largura_cliente)
    elements.append(tabela_cliente)
    elements.append(Spacer(1, 12))

    #Primeira tabela - Mês
    dados_tabela_1 = [
        [f'{mes}'],
        [f'{mes}', 'Quantidade'],
        ['Chamados', f'{chamados}'],
        ['Horas utilizadas', f'{horas_utilizadas_mes}']
    ]
    estilo_tabela_1 = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    largura_mes = [4 * cm, 4 * cm]  # Ajustando a largura
    tabela_mes = criar_tabela(dados_tabela_1, estilo_tabela_1, largura_mes)
    tabela_mes.hAlign = 'LEFT'
    elements.append(tabela_mes)
    elements.append(Spacer(1, 12))

    #Segunda tabela - Trimestre
    dados_tabela_2_1 = [
        ['Trimestre'],
        ['Mês', f'{mes_1}', f'{mes_2}', f'{mes_3}', 'Tempo Total'],
        ['Horas', f'{horas_mes_1}', f'{horas_mes_2}', f'{horas_mes_3}', f'{horas_mes_1 + horas_mes_2 + horas_mes_3}']
    ]
    estilo_tabela_2_1 = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    largura_trimestre_1 = [1.5 * cm, 2 * cm, 2 * cm, 2 * cm, 3 * cm]
    tabela_trimestre_1 = criar_tabela(dados_tabela_2_1, estilo_tabela_2_1, largura_trimestre_1)
    tabela_trimestre_1.hAlign = 'RIGHT'
    elements.append(tabela_trimestre_1)
    elements.append(Spacer(1, 12))

    dados_tabela_2_2 = [
        ['Horas Contratadas', f'{horas_contratadas}'],
        ['Horas utilizadas', f'{horas_utilizadas_trimestre}'],
        ['Saldo', f'{saldo}'],
        ['Valor hora adicional', f'R${valor_hora_adicional_trimestre}'],
        ['Adicional de horas', f'R${adicional_de_horas_trimestre}']
    ]
    estilo_tabela_2_2 = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    largura_trimestre_2 = [5 * cm, 5 * cm]  # Ajustando a largura
    tabela_trimestre_2 = criar_tabela(dados_tabela_2_2, estilo_tabela_2_2, largura_trimestre_2)
    tabela_trimestre_2.hAlign = 'RIGHT'
    elements.append(tabela_trimestre_2)
    elements.append(Spacer(1, 12))

    #Terceira tabela - Faturamento
    dados_tabela_3 = [
        ['Faturamento'],
        ['Valor mensal', f'R${valor_mensal_faturamento}'],
        ['Serviços adicionais / peças', f'R${serviços_adicionais_ou_peças}'],
        ['Valor de horas adicionais do trimestre anterior', f'R${valor_de_horas_adicionais_do_trimestre_anterior}'],
        ['Total geral', f'R${valor_mensal_faturamento + serviços_adicionais_ou_peças + valor_de_horas_adicionais_do_trimestre_anterior}']
    ]
    estilo_tabela_3 = TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    largura_faturamento = [8 * cm]  # Ajustando a largura para ficar centralizado
    tabela_faturamento = criar_tabela(dados_tabela_3, estilo_tabela_3, largura_faturamento)
    elements.append(tabela_faturamento)

    #Criar o documento
    doc.build(elements)

#Exemplo de chamada da função com parâmetros fictícios
gerar_pdf(
    nome_arquivo='relatorio.pdf',
    nome_cliente='Cliente XYZ',
    horas_mensais=120,
    horas_trimestrais=360,
    valor_mensal=1000,
    valor_hora=50,
    valor_hora_adicional_cliente=75,
    mes='Janeiro',
    chamados=10,
    horas_utilizadas_mes=100,
    mes_1='Janeiro',
    horas_mes_1=100,
    mes_2='Fevereiro',
    horas_mes_2=110,
    mes_3='Março',
    horas_mes_3=120,
    horas_contratadas=360,
    horas_utilizadas_trimestre=330,
    saldo=30,
    valor_hora_adicional_trimestre=80,
    adicional_de_horas_trimestre=1600,
    valor_mensal_faturamento=1000,
    serviços_adicionais_ou_peças=200,
    valor_de_horas_adicionais_do_trimestre_anterior=300
)