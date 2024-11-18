class ROI:

    def __init__(self, price, income, costs):
        self.price = price
        self.income = income
        self.costs = costs

    def calculate_roi(self):
        yearlyincome = self.income * 12
        yearlycosts = self.costs * 12
        yearlyincomeafter = yearlyincome - yearlycosts
        roi = yearlyincomeafter / self.price
        ROIP = roi * 100
        print(f'ROI percentage is {ROIP}% per year')


price = float(input("What is the investment cost(Downpayment +Closing costs +Rehab budget +Misc other): "))
income = float(input("What is the monthly income(Rental Income + Laundry Income + Storage Income + Misc Income): "))
costs = float(input("What is the costs per month(Taxes + Insurance + Water/Sewer + Garbage + Electric/Gas + HOA Fee + Lawn/Snow + Vacancy + Repairs + CapEx + Prop. Mgmt + Mortgage): "))


croi = ROI(price, income, costs)
croi.calculate_roi()