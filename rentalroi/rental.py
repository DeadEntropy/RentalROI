from collections import namedtuple
from mortgage import Loan

Cashflow = namedtuple('Cashflow', 'number rent hoa management_fee tax insurance interest principal')

class Rental:    
    def __init__(self, price, rent, hoa, management_fee = 0.0, tax_rate = 0.0035, insurance_rate = 0.0035, loan_ratio = 0.85, \
                 loan_term = 15, loan_rate = 0.06, income_tax_rate = 0.37, additional_investment = 0.0):
        self._price = price
        self._additional_investment = additional_investment
        self._rent = rent
        self._hoa = hoa
        self._management_fee = rent*management_fee
        self._tax = price*tax_rate/12
        self._insurance = price*insurance_rate/12
        self._loan = Loan(principal=(price + additional_investment)*loan_ratio, interest=loan_rate, term=loan_term)
        self._schedule = self._initialize_schedule()
        self._income_tax_rate = income_tax_rate
        
    def schedule(self, nth_payment=None):
        if nth_payment:
            data = self._schedule[nth_payment]
        else:
            data = self._schedule
        return data
    
    def _initialize_schedule(self):
        initialize = Cashflow(number=0,
                              rent=0,
                              hoa=0,
                              management_fee=0,
                              tax=0,
                              insurance=0,
                              interest=0,
                              principal=0)
        
        schedule = []
                
        for loan_sch in self._loan.schedule():
            cashflow = Cashflow(number=loan_sch.number,
                                rent=self._rent,
                                hoa=self._hoa,
                                management_fee=self._management_fee,
                                tax=self._tax,
                                insurance=self._insurance,
                                interest=float(loan_sch.interest),
                                principal=float(loan_sch.principal))

            schedule.append(cashflow)
        return schedule
    
    @property
    def summarize(self):
        print('Property Purchase Price:  {}{:>11,.0f}'.format(self._loan._currency, self._price))
        print('Additional Setup Cost:    {}{:>11,.0f}'.format(self._loan._currency, self._additional_investment))
        print('')
        original_investment =  self._price + self._additional_investment - float(self._loan.principal)
        print('Initial Investment:       {}{:>11,.0f}'.format(self._loan._currency, original_investment))
        print('Loan Principal:           {}{:>11,.0f}'.format(self._loan._currency, self._loan.principal))
        print('')
        print('Monthly Rent:             {}{:>11,.0f}'.format(self._loan._currency, self._rent))
        tax_deductibles = float(self._loan.schedule(1).interest) + self._insurance + self._management_fee + self._hoa + self._tax
        not_tax_deductibles = float(self._loan.schedule(1).principal)
        print('Monthly Costs:            {}{:>11,.0f}'.format(self._loan._currency, tax_deductibles + not_tax_deductibles))        
        print(' - Loan Payment:          {}{:>11,.0f}'.format(self._loan._currency, self._loan.monthly_payment))        
        print('   * Principal:           {}{:>11,.0f}'.format(self._loan._currency, self._loan.schedule(1).principal))        
        print('   * Interest:            {}{:>11,.0f}'.format(self._loan._currency, self._loan.schedule(1).interest))
        print(' - HOA:                   {}{:>11,.0f}'.format(self._loan._currency, self._hoa))
        print(' - Management Fees:       {}{:>11,.0f}'.format(self._loan._currency, self._management_fee))
        print(' - Tax:                   {}{:>11,.0f}'.format(self._loan._currency, self._tax))
        print(' - Insurnace:             {}{:>11,.0f}'.format(self._loan._currency, self._insurance))
        print('')
        print('Tax Deductibles:          {}{:>11,.0f} p.a.'.format(self._loan._currency, tax_deductibles * 12))
        taxable_income = self._rent - tax_deductibles
        print('Taxable Income:           {}{:>11,.0f} p.a.'.format(self._loan._currency, taxable_income * 12))
        income_after_tax = taxable_income * 12 * (1 - self._income_tax_rate)
        print('Income After Tax:         {}{:>11,.0f} p.a.'.format(self._loan._currency, income_after_tax))
        print('Cashflow:                 {}{:>11,.0f} p.a.'.format(self._loan._currency, income_after_tax - not_tax_deductibles * 12))
        print('')
        print('Net ROI:                    {:>10,.0%} p.a.'.format((taxable_income * 12) * (1 - self._income_tax_rate) / original_investment))
        print('Loan Leverage:              {:>10,.1f}'.format(1+ float(self._loan.principal) / original_investment))