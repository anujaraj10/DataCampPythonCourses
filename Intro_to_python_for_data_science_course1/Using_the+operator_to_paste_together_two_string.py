#Using the + operator to paste together two strings can be very useful in building custom messages.

#Suppose, for example, that you've calculated the return of your investment and want to summarize the results in a string. Assuming the floats #savings and result are defined, you can try something like this:

#print("I started with $" + savings + " and now have $" + result + ". Awesome!")
#This will not work, though, as you cannot simply sum strings and floats.

# Definition of savings and result
savings = (100)
result = (100 * 1.10 ** 7)
# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"
pi_float = float("3.1415926")
print (pi_float)
