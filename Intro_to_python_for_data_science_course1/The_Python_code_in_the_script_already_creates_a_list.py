#The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first element in the areas_copy #list is changed and the areas list is printed out. If you hit Submit Answer you'll see that, although you've changed areas_copy, the change #also takes effect in the areas list. That's because areas and areas_copy point to the same list.

#If you want to prevent changes in areas_copy to also take effect in areas, you'll have to do a more explicit copy of the areas list. You can do t#his with list() or by using [:].

#Watch out! list() and [:] might not copy properly if you put complex things in your lists.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)