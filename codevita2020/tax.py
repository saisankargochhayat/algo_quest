"""
https://blog.taxact.com/how-tax-brackets-work/
"""
class TaxCalculator (object):
    def __init__ (self, taxBracket):
        self.taxBracket = taxBracket
        self._init()

    def computeTax (self, salary):

        if not self.taxBracket or len(self.taxBracket) == 0 or salary == 0:
            return 0

        totalTax = 0
        prevTaxableAmount = 0
        taxableIncome = 0

        for tax in self.taxBracket:
            if salary > tax[0]:
                taxableIncome += tax[0]-prevTaxableAmount
                currTax = (tax[0]-prevTaxableAmount) * tax[1]
            else:
                taxableIncome += salary-prevTaxableAmount
                currTax= (salary-prevTaxableAmount) * tax[1]

            print "currTax=", currTax, "taxableIncome=", taxableIncome
            totalTax += currTax
            prevTaxableAmount = tax[0]

            if taxableIncome >= salary:
                break

        return totalTax

    def _init (self):
        self.taxBracket = sorted(self.taxBracket)
        highestBracket = self.taxBracket.pop(0)
        highestBracket[0] = float('inf')
        self.taxBracket.append(highestBracket)




taxBracket = [[38700, .12], [9525, .10], [82500, .22], [157500, .24],[None, .32]]
taxCalculator = TaxCalculator(taxBracket)

print(taxCalculator().computeTax(38699))
print(taxCalculator().computeTax(38700))
print(taxCalculator().computeTax(38701))
