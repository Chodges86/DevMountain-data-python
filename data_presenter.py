
# Open the CupcakeInvoices.csv.
open_file = open('CupcakeInvoices.csv')

# Loop through all the data and print each row.
for line in open_file:
    print(line)

open_file.seek(0)

# Loop through all the data and print the type of cupcakes purchased.
for line in open_file:
    line = line.split(',')
    print(line[2])

open_file.seek(0) 

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
total = 0
for line in open_file:
    line = line.split(',')
    qty = float(line[3])
    price = float(line[4])
    total += (qty*price)
    print("%.2f" % (qty*price))

open_file.seek(0)
# Loop through all the data, and print out the total for all invoices combined.
print("%.2f" % total)

# Close your open file.

# Challenge: Do some research and see if you can limit your floats to never exceed to characters after the decimal point.