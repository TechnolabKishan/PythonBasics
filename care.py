class Auto:
    def __init__(self, model, year, color, for_Sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_Sale = for_Sale

    def drive(self):
        print(f'you drive the {self.color} {self.model}')

    def stop(self):
        print(f'you stopped the {self.color} {self.model}')

    def describe(self):
        print(f'{self.year} {self.color} {self.model}')