from pydantic import BaseModel

class ClientModel(BaseModel):
        client_name: str
        contract_type: str
        monthly_hours: int
        quarterly_hours: int
        monthly_billing: float
        hourly_rate: int
        client_additional_hour_rate: int

class MonthlyUseModel(BaseModel):
        month: str
        incidents: int
        monthly_hours_used: int

class QuarterlyModel(BaseModel):
        first_month: str
        hours_first_month: int
        second_month: str
        hours_second_month: int
        third_month: str
        hours_third_month: int
        contracted_hours: int
        quarterly_hours_used: int
        balance: int
        quarterly_additional_hour_rate: int
        quarterly_additional_hours: int

class BillingModel(BaseModel):
        monthly_billing: int
        additional_services_or_parts: int
        previous_quarter_additional_hour_value: int

class ReportModel(BaseModel):
        file_name: str
        client: ClientModel
        monthly_use: MonthlyUseModel
        quarterly: QuarterlyModel
        billing: BillingModel

