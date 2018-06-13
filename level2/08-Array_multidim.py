__author__ = 'chira'

# Create a list.
elements = []

# Append empty lists in first three indexes.
elements.append([])
elements.append([])
elements.append([])

# Add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)
elements[1].append(5)

elements[2].append(7)
elements[2].append(9)

# Display top-left element.
print(elements[0][0])

# Display entire list.
print(elements)

# Loop over rows.
for i in range(0,len(elements)):
    # Loop over columns.
    for j in range(0,len(elements[i])):
        print("arr[%d][%d] = %d" % (i,j,elements[i][j]))