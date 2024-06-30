from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.units import cm
from datetime import datetime

from models import ReportModel

class GenerateReport:
    def __init__(self, report: ReportModel) -> None:
        self.report = report
        
        self.doc = SimpleDocTemplate(self.report.file_name, pagesize=A3)
        self.elements = []
        
        self.styles = getSampleStyleSheet()


    def start(self):
        self._make_styles()
        self._make_title()
        self._make_subtitle()
        self._generate_client_table()
        self._generate_month_table()
        self._generate_quarterly_table_1()
        self._generate_quarterly_table_2()
        self._generate_billing_table()
        self._generate_page_template()
        self._make_pdf()


    def _make_styles(self):
        self.title_style = self.styles['Title']
        self.centered_text_style = ParagraphStyle(
            'Centered',
            parent = self.styles['BodyText'],
            alignment=1 # 1 centers the text
        )

        self.normal_style = self.styles['BodyText']

        self.bold_style = self.styles['Normal']
        self.bold_style.fontName = 'Helvetica-Bold'
        self.bold_style.alignment = 1


    def _make_title(self):
        title = "Incident Management Report"
        title_paragraph = Paragraph(title, self.title_style)
        self.elements.append(title_paragraph)


    def _make_subtitle(self):
        year = datetime.now().year
        text = f'{self.report.monthly_use.month} of {year}'
        text_paragraph = Paragraph(text, self.centered_text_style)
        self.elements.append(text_paragraph)
        self.elements.append(Spacer(1, 12))


    def __generate_table(self, data, style=None, largura_colunas=None):
        table = Table(data, colWidths=largura_colunas)
        if style:
            table.setStyle(style)
        return table


    def _generate_page_template(self):
        template_data = [
            [self.client_table],
            [self.month_table, self.quarterly_table_1],
            ['', self.quarterly_table_2]
            [self.billing_table]
        ]
        template_style = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('ALIGN', (0, 0), (-1, 3), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        template_width = [14 * cm, 14 * cm]
        template_table = self.__generate_table(template_data, template_style, template_width)
        self.elements.append(template_table)
        self.elements.append(Spacer(1, 12))


    def _generate_client_table(self):
        client = self.report.client
        dados_cliente = [
        [f'Cliente: {client.client_name}'],
        ['Tipo de Contrato:', Paragraph(f'{client.contract_type}')],
        ['Horas Mensais:', Paragraph(f'{client.monthly_hours} horas mensais, {client.quarterly_hours} horas trimestrais.')],
        ['Valor mensal:', Paragraph(f'R${client.monthly_billing}')],
        ['Valor hora:', Paragraph(f'R${client.hourly_rate}')],
        ['Valor hora adicional:', Paragraph(f'R${client.client_additional_hour_rate}')]
        ]
        estilo_cliente = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), (0.1, 0.4, 0.9)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ('FONT', (0, 0), (0, -1), 'Helvetica-Bold')
        ])
        largura_cliente = [5 * cm, 22 * cm]
        client_table = self.__generate_table(dados_cliente, estilo_cliente, largura_cliente)
        client_table.hAlign = 'LEFT'
        self.client_table = client_table


    def _generate_month_table(self):
        monthly_use = self.report.monthly_use
        month_table_data = [
            [f'{monthly_use.month}'],
            [Paragraph(f'{monthly_use.month}', self.bold_style), Paragraph('Quantidade', self.bold_style)],
            [Paragraph('Chamados', self.centered_text_style), Paragraph(f'{monthly_use.incidents}', self.centered_text_style)],
            [Paragraph('Horas utilizadas', self.centered_text_style), Paragraph(f'{monthly_use.monthly_hours_used}', self.centered_text_style)]
        ]
        month_table_style = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), (0.1, 0.4, 0.9)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        month_width = [6.7 * cm, 6.7 * cm]
        month_table = self.__generate_table(month_table_data, month_table_style, month_width)
        self.month_table = month_table


    def _generate_quarterly_table_1(self):
        quarterly = self.report.quarterly
        data_quarterly_table_1 = [
            ['Trimestre'],
            [Paragraph('Mês', self.bold_style), Paragraph(f'{quarterly.first_month}', self.bold_style), Paragraph(f'{quarterly.second_month}', self.bold_style), Paragraph(f'{quarterly.second_month}', self.bold_style), Paragraph('Tempo Total', self.bold_style)],
            [Paragraph('Horas', self.centered_text_style), Paragraph(f'{quarterly.first_month}', self.centered_text_style), Paragraph(f'{quarterly.second_month}', self.centered_text_style), Paragraph(f'{quarterly.hours_second_month}', self.centered_text_style), Paragraph(f'{quarterly.hours_first_month + quarterly.hours_second_month + quarterly.hours_third_month}', self.centered_text_style)],
            ['']
        ]
        style_quarterly_table_1 = TableStyle([
            ('SPAN', (0, -1), (-1, -1)),
            ('SPAN', (0, 0), (-1, 0)),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, 0), (0.1, 0.4, 0.9)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, -1), (-1, -1), 1, colors.white),
            ('FONT', (0, 0), (-1, 1), 'Helvetica-Bold')
        ])
        width_quarterly_table_1 = [1.9 * cm, 2.4 * cm, 2.4 * cm, 2.4 * cm, 3.4 * cm]
        quarterly_table_1 = self.__generate_table(data_quarterly_table_1, style_quarterly_table_1, width_quarterly_table_1)
        self.quarterly_table_1 = quarterly_table_1


    def _generate_quarterly_table_2(self):
        quarterly = self.report.quarterly
        quarterly_table_data = [
            [Paragraph('Horas Contratadas', self.centered_text_style), Paragraph(f'{quarterly.contracted_hours}', self.centered_text_style)],
            [Paragraph('Horas utilizadas', self.centered_text_style), Paragraph(f'{quarterly.quarterly_hours_used}', self.centered_text_style)],
            [Paragraph('Saldo', self.bold_style), Paragraph(f'{quarterly.balance}', self.centered_text_style)],
            [Paragraph('Valor hora adicional', self.centered_text_style), Paragraph(f'R${quarterly.quarterly_additional_hour_rate}', self.centered_text_style)],
            [Paragraph('Adicional de horas', self.centered_text_style), Paragraph(f'R${quarterly.quarterly_additional_hours}', self.centered_text_style)]
        ]
        quarterly_table_2_data = TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONT', (0, 2), (-1, 2), 'Helvetica-Bold'),
        ])
        quarterly_table_2_widht = [5 * cm, 5 * cm]  # Ajustando a largura
        quarterly_table_2 = self.__generate_table(quarterly_table_data, quarterly_table_2_data, quarterly_table_2_widht)
        self.quarterly_table_2 = quarterly_table_2


    def _generate_billing_table(self):
        billing = self.report.billing
        billing_table_data = [
            ['Faturamento'],
            [Paragraph('Valor mensal', self.centered_text_style), Paragraph(f'R${billing.monthly_billing}', self.centered_text_style)],
            [Paragraph('Serviços adicionais / peças', self.centered_text_style), Paragraph(f'R${billing.additional_services_or_parts}', self.centered_text_style)],
            [Paragraph('Valor de horas adicionais do trimestre anterior', self.centered_text_style), Paragraph(f'R${billing.previous_quarter_additional_hour_value}', self.centered_text_style)],
            [Paragraph('Total geral', self.bold_style), Paragraph(f'R${billing.monthly_billing + billing.additional_services_or_parts + billing.previous_quarter_additional_hour_value}', self.bold_style)]
        ]
        billing_table_style = TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), (0.1, 0.4, 0.9)),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONT', (0, 4), (-1, 5), 'Helvetica-Bold'),
        ])
        billing_table_width = [12 * cm]
        billing_table = self.__generate_table(billing_table_data, billing_table_style, billing_table_width)
        self.billing_table = billing_table


    def _make_pdf(self) -> None:
        self.doc.build(self.elements)
