# Taking input for first Product ...
first_id, first_quantity, first_price = input().split(" ")
# Taking input for second Product...
second_id, second_quantity, second_price = input().split(" ")
total = ((int(first_quantity) * float(first_price)) +
         (int(second_quantity) * float(second_price)))
# Printing Result...
print('VALOR A PAGAR: R$ {0:.2f}'.format(total))
