fire_cells = input().split("#")
total_water = int(input())
effort_made = 0
total_fire = 0
cleared_cells = []
for current_cell in fire_cells:
    current_cell = current_cell.split(" = ")
    current_fire = current_cell[0]
    current_index = int(current_cell[1])
    if current_fire == "High" and 81<=current_index<=125 and total_water >= current_index:
        cleared_cells.append(current_index)
        total_water -= current_index
        total_fire += current_index
        effort_made += current_index * 0.25
    elif current_fire == "Medium" and 51<=current_index<=80 and total_water >= current_index:
        cleared_cells.append(current_index)
        total_water -= current_index
        total_fire += current_index
        effort_made += current_index * 0.25
    elif current_fire == "Low" and 1<=current_index<=50 and total_water >= current_index:
        cleared_cells.append(current_index)
        total_water -= current_index
        total_fire += current_index
        effort_made += current_index * 0.25
print("Cells:")
for cell in cleared_cells:
    print(f" - {cell}")
print(f"Effort: {effort_made:.2f}")
print(f"Total Fire: {total_fire}" )