class InvestmentCalculator:
    def __init__(self, initial_investment, interest_rate, interval,years):
        self.initial_investment = initial_investment
        self.interest_rate = interest_rate
        self.interval = interval
        self.years = years
        self.total = self.calculate()

    def calculate(self):
        return self.initial_investment * (1 + self.interest_rate / 100) ** (self.interval_to_amount(self.interval) * self.years)

    def interval_to_amount(self, interval):
        if interval == 'daily':
            return 365
        elif interval == 'monthly':
            return 12
        elif interval == 'quarterly':
            return 4
        elif interval == 'annually':
            return 1
        

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')

def get_interval(prompt):
    while True:
        interval = input(prompt)
        if interval in ['daily', 'monthly', 'quarterly', 'annually']:
            return interval
        print('Invalid input. Please enter daily, monthly, quarterly, or annually.')

def main():
    initial_investment = get_float('Enter the initial investment: ')
    interest_rate = get_float('Enter the interest rate: ')
    interval = get_interval('Enter the compounding interval ("daily", "monthly", "quarterly", "annually"): ')
    years = get_int('Enter the number of years: ')

    investment_calculator = InvestmentCalculator(initial_investment, interest_rate, interval, years)
    investment_calculator.calculate()
    print(f'Initial Investment: ${round(initial_investment, 2)}, at {interest_rate}%, compounding {interval}, final balance: ${round(investment_calculator.total, 2)}')

if __name__ == '__main__':
    main()
