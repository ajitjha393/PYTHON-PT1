from Employee import *

basic = int(input('Enter the basic salary : '))
grossSalary = basic + calculateDA(basic) + calculateHRA(basic)
netSalary = grossSalary - calculatePF(basic) - calculateITAX(grossSalary)
print('Gross Salary => ', grossSalary)
print('Net Salary => ', netSalary)
