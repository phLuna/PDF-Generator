from generate_report import GenerateReport
from models import ReportModel, ClientModel, BillingModel, MonthlyUseModel, QuarterlyModel

client = ClientModel(
    client_name = 'Pedro',
    contract_type = 'Venda de Alma',
    monthly_hours = 666,
    quarterly_hours = 40,
    monthly_billing = 1200,
    hourly_rate = 450,
    client_additional_hour_rate = 80
)

monthly_use = MonthlyUseModel(
    month = 'Março',
    incidents = 10,
    monthly_hours_used = 6
)

billing = BillingModel(
    monthly_billing = 60,
    additional_services_or_parts = 48,
    previous_quarter_additional_hour_value = 74
)

quarterly = QuarterlyModel(
    first_month="January",
    hours_first_month=40,
    second_month="February",
    hours_second_month=35,
    third_month="March",
    hours_third_month=45,
    contracted_hours=120,
    quarterly_hours_used=120,
    balance=0,
    quarterly_additional_hour_rate=50,
    quarterly_additional_hours=10
)

report = ReportModel(
    file_name    = 'ReportTunado.pdf',
    client       = client,
    monthly_use  = monthly_use,
    billing      = billing,
    quarterly    = quarterly
)

rel = GenerateReport(report)
rel.start()