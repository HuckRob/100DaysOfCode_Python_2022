# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
x_pos = int(position[0])
y_pos = int(position[1])

if y_pos == 1:
    if x_pos == 1:
        row1[0] = "X"
    if x_pos == 2:
        row1[1] = "X"
    if x_pos == 3:
        row1[2] = "X"
if y_pos == 2:
    if x_pos == 1:
        row2[0] = "X"
    if x_pos == 2:
        row2[1] = "X"
    if x_pos == 3:
        row2[2] = "X"
if y_pos == 3:
    if x_pos == 1:
        row3[0] = "X"
    if x_pos == 2:
        row3[1] = "X"
    if x_pos == 3:
        row3[2] = "X"


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
