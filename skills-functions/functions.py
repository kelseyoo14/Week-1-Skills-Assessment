# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def print_name(name):
    print "Hi", name


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiplies(num1, num2):
    print num1 * num2


# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def print_string(string, num):
    print string * integer


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def lower_or_higher(num):
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    elif num == 0:
        print "Zero"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def num_of_space(string):
    count = 0
    for letter in string:
        if letter == " ":
            count +=1
    return count


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_meal_price(meal_price, tip=15):
    total = meal_price + (meal_price * (float(tip)/100))
    return total


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def sign_and_parity(num):
    if num < 0:
        sign = "Negative"
    # It wasn't explicitly said in the directions what should be done with '0'
    # Since the options are "Positive" or "Negative", I'm having '0' come up with "Positive"
    else:
        sign = "Positive"

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return sign, parity


sign, parity = sign_and_parity(-11)

print sign
print parity


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.


# *****The instructions seemed a little confusing to me. First, I wouldn't think I'd need to pass in
# "default tax amount" twice, let alone once, if I don't want the user defining the tax.
# Second, I would assume that a user would pass in the cost of the item being calculated, unless this
# function is specifically for this one specific price (which would defeat the purpose of writing a
# reusable piece of code). Therefore, the parameters should be state abbreviation and item price.

def price_with_tax(state, item_price):
    total_item_cost = 0

    if state.upper() == "CA":
        total_item_cost = item_price + (item_price * .07)
    else:
        total_item_cost = item_price + (item_price * .05)

    return total_item_cost



# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def name_and_title(name, title="Engineer"):
    return title + " " + name


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

def amazing_letter(receiver_name, receiver_title, sender_name):
    receiver = name_and_title(receiver_name, receiver_title)

    print "Dear %s, I think you are amazing! \nSincerely, %s." % (receiver, sender_name)


# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.


# *****I wasn't quite sure from the directions whether I should pass in both a number and the list
# "numbers". Since it said "take a number", I wrote it to only take in a number, and not the list.
# From my understanding, whether or not I pass in the list doesn't matter, as long as I reference
# the correct list in the function. Though writing it this way means this function can only append 
# to the specific list "numbers".

def add_to_numbers_list(num):
    numbers.append(num)




