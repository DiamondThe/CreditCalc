import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--principal", default=None,
                    help='Loan principal')
parser.add_argument("--payment", default=None,
                    help='Annuity payment')
parser.add_argument("--periods", default=None,
                    help='Number of payments')
parser.add_argument("--interest", default=None,
                    help='Nominal interest')
parser.add_argument("--type", default=None,
                    help='Annuity or differentiated')

args = parser.parse_args()
def interest():
    interest = float(args.interest) / 1200
    return interest

def principal(periods, payment):
    first_stage = (1 + interest()) ** periods - 1
    second_stage = interest() * (1 + interest()) ** periods
    thirst_stage = second_stage / first_stage
    principal = payment / thirst_stage
    return int(principal)

def annuity_payment(principal, periods):
    first_stage = (1 + interest()) ** periods - 1
    second_stage = interest() * (1 + interest()) ** periods
    payment = principal * (second_stage / first_stage)
    return math.ceil(payment)

def number_of_payments(principal, payment):
    first_stage = payment - interest() * principal
    second_stage = payment / first_stage
    log = math.log(second_stage, 1 + interest())
    return log
def differentiate_payment(payment, periods, interest):
    print(interest)
    overpayments = 0
    counter_of_months = periods
    count = 1
    final_payment = 1
    while counter_of_months != 0 and final_payment > 0:
        amount = payment / periods
        amount2 = (payment * (counter_of_months - 1)) / periods
        amount3 = payment - amount2
        amount4 = interest * amount3 + amount
        print(f'Month {count}: payment is {math.ceil(amount4)}')
        final_payment = amount4
        count += 1
        overpayments += math.ceil(amount4)
        counter_of_months -= 1
    overpayment = overpayments - payment
    return '\n' + f'Overpayment = {overpayment}'

def annuity(principal, payment, periods):
    overpayments = 0
    while periods != 0:
        overpayments += payment
        periods -= 1
    overpayment = overpayments - principal
    return f'Overpayment = {overpayment}'

number_of_args = 0
bol = False

if args.principal != None and float(args.principal) >= 0:
    number_of_args += 1
if args.payment != None and float(args.payment) >= 0:
    number_of_args += 1
if args.periods != None and float(args.periods) >= 0:
    number_of_args += 1
if number_of_args < 2 or number_of_args == 3:
    print('Incorrect parameters')
else:
    bol = True

if args.type == None or args.interest == None and bol == True:
    print('Incorrect parameters')
elif args.interest == None or float(args.interest) < 0:
    print('Incorrect parameters')
elif args.type == 'diff' and args.interest != None:
    interest = interest()
    print(differentiate_payment(int(args.principal),
                                int(args.periods),
                                interest))

elif args.type == 'annuity' and args.interest != None and bol == True:
    if args.principal is None:
        args.principal = principal(int(args.periods),
                                   int(args.payment))
        print(f'Your loan principal = {args.principal}!')
        print(annuity(int(args.principal), int(args.payment),
                      int(args.periods)))
    elif args.payment is None:
        args.payment = annuity_payment(int(args.principal),
                                       int(args.periods))
        print(f'Your monthly payment = {args.payment}!')
        print(annuity(int(args.principal), int(args.payment),
                      int(args.periods)))
    elif args.periods is None:
        years = round(number_of_payments(int(args.principal),
                                         int(args.payment))) / 12
        months = round(number_of_payments(int(args.principal),
                                          int(args.payment))) % 12
        per = round(number_of_payments(int(args.principal),
                                       int(args.payment)))
        if months == 12:
            print(f'It will take {years + 1} years to repay this '
                  f'loan!')
            print(annuity(int(args.principal), int(args.payment), per))
        elif years == 1 and months == 0:
            print(f'It will take {years} year to repay this loan!')
            print(annuity(int(args.principal), int(args.payment), per))
        elif years != 0 and years != 1 and months == 0:
            print(f'It will take {years} years to repay this loan!')
            print(annuity(int(args.principal), int(args.payment), per))
        else:
            print(f'It will take {years} years and {months} months to repay'
                  f' this loan!')
            print(annuity(int(args.principal), int(args.payment), per))
else:
    print('Incorrect parameters')