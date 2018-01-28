#! python3
# This is a program for ATBS making a list organized into string right aligned


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def table_printer(tab_data):
    col_widths = [0] * len(tab_data)  # creates 3 lists based on the list length
    for j in range(len(tab_data[0])):  # finds a length of 4 items (aka rows)
        for i in range(len(tab_data)):  # finds a length of 3 items (aka columns)
            col_widths[i] = len((max(tab_data[i], key=len)))  # sets the column width to the maximum length of an item in the list
            a = tab_data[i][j]
            print(a.rjust(col_widths[i]), end=" ")  #  every time we print a column, we rjust it to the max width.
        print("\n")


table_printer(tableData)
