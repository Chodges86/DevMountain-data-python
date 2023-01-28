
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
# open_file.close()

# Challenge: Do some research and see if you can limit your floats to never exceed to characters after the decimal point.

# PART 3
# Going Further
# Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
print("Printing Totals from Switch:")

total_choc = 0
total_straw = 0
total_van = 0

for line in open_file:
    line = line.split(',')
    match line[2]:
        case "Chocolate":
            total_choc += float(line[3]) * float(line[4])
        case "Strawberry":
            total_straw += float(line[3]) * float(line[4])
        case "Vanilla":
            total_van += float(line[3]) * float(line[4])

flavors = ["Chocolate", "Strawberry", "Vanilla"]
totals = [total_choc, total_straw, total_van]
bar_colors = ["tan", "lightcoral", "cornsilk"]
ax.bar(flavors, totals, label=flavors, color=bar_colors, edgecolor="dimgray")

ax.set_ylabel("Total Sales in USD")
ax.set_xlabel("Flavor")
ax.set_title("Total sales by flavor")
ax.legend()

plt.show()