# coding=utf-8

########################################   1

print(type(42))

## type() prints the actual type of the argument passed, type("test") prints String (str) because "test" is a string
print(type("test"))
## type(42) types Int because 42 is a whole number (integer)
## type(0.5) would print float because it is not a whole number
print(type(0.5))

print(type(True))

## empty print is just to create a new line in console, for readability. not for the assignment
print()
######################################## 2

print("puppa"[3:])

# prints "pa", 3 is index position and : means print all following chars

###
print()


################################### 3

def monthOutput(month):
    ## dict is "dictonary" it has a name for a variable stored.
    ## return dict.get(number, "non valid input") would return '1' if you passed the number variable one. dictionary would look like this in that case  =         "one" : 1

    ## look at this : https://www.pydanny.com/why-doesnt-python-have-switch-case.html

    dict = {
        "Januari": "Vinter",
        "Februari": "Vinter",
        "Mars": "Vår",
        "April": "Vår",
        "Maj": "Vår",
        "Juni": "Sommar",
        "Juli": "Sommar",
        "Augusti": "Sommar",
        "September": "Höst",
        "Oktober": "Höst",
        "November": "Höst",
        "December": "Vinter",

    }

    return dict.get(month, "non valid input")


##month = input("Skriv en månad ")
##print(monthOutput(month))


##################################4

testar = "hejhejhej"

testar.capitalize()

testar = testar.capitalize()

print(testar)

int = 10000


def testFunc(int):
    if int == 5:
        print("the number is 5")
    else:
        print("the number is not 5")


def rensa(s):
    ## all numbers 0 1 2 3 4 5 6 7 8 9

    for i in range(10):
        ##if it finds one of the numbers, replace it with nothing ''

        s = s.replace(str(i), '')

    return s


stringtwo = "twothree"

#### vilkenstringduvilländra på = stringduvilländrapå.replace("vad du vill ersätta", "vad du vill ska stå istället")

## du kommer alltså åt stringens metoder genom att skriva . efter variabelnamnet
## samma för ints, bools osv osv

stringtwo = stringtwo.replace("t", "bajs")

print(stringtwo)

string = "ran53dom w94o8r92839ds"

print("String before cleaning : " + string)

print()

print("string after cleaning : " + rensa(string))

rensa("hej")

numbersBase = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##
print()

########################################### 5

# S är ett parameternamn, inte själva bokstaven s
# res har inte initierats

## alltså du måste skriva res = 0 någonstans i metoden innan du använder res som variabel


#räkna("bajs", "bajskslrjla")


##kommer kolla hur många gånger "bajs" finns med (alltså inte bokstaven s som i exemplet


## res += 1 samma sak som
## res = res +1

########################################## 6

def fakultet(n):
    res = 1

    ## we go from 1 to n instead of 0 to n. thats why we need 1 to n+1 to make up for the shift
    for i in range(1, n + 1):
        ## *= means res = res * i but shorter
        res *= i
        print(res)
    return res


print("Fakultet 4 : " + str(fakultet(4)))

##
print()


########################################### 7

## Basically #3, use a dictionary

def getPerson(personnummer):

    personMax = {'Name': 'Max',
                 'Age': 21,
                 'School': 'Chalmers'}

    personRandom = {'Name': 'Snurrr',
                    'Age': 99,
                    'School': 'Livets hårda skola'}

    persons = {
        960602: personMax,
        900101: personRandom

    }

    ##om det inte är ett giltigt personnummer så skickas "non valid input" tillbaks som string
    return persons.get(personnummer, "non valid input")


print(getPerson(960602))
##
print()


############################################# 8

## 3d objects consists of layers



class Layer():
    x = 0
    y = 0
    z = 0



        ##denna behöver du inte tänka på
    def __init__(self, x):
        self.__x = x


## multiple layers create a shape
class Shape:
    shape = {Layer, Layer, Layer, Layer}


#testlager = Layer

#testlager.setX(Layer, 4)

############################################## 9



##Denna funnkar inte just nu, ska kolla på den sen
def dubbelt(string):
    amount = 0  ##initiating amount variable
    for i in range(0, len(string)):
        # here we select a char in the string, starting from index 0
        char = string[i]
        for i in range(0, len(string)):
            ##iterate over the string to see how many times the selected chars exists
            if string[i] == char:
                ##if it finds it, add 1 to amount
                amount += 1

    ## you can also use "if amount:", amount is "True" if it is 1 or over
    if amount > 1:
        return True
    else:
        return False


print(dubbelt("c occurs 3 times"))

print(dubbelt("abc"))
##
print()
############################################ 10


## it "zips" the file together like a zipper, creating "tuples" (tuples == pair of variables or types)

print(list(zip([2015, 2016, 2017], [30, 33, 35])))

numberDigits = [1, 2, 3]



def fleraVariabler(x, y, z):
    print(x)
    print(y)
    print(z)

numberWords = ["One", "Two", "Three"]

##
print()
##
## now it prints (1, one) because it pairs them together. it works the same way if you have even more lists, creating 3-tuples
print(list(zip(numberDigits, numberWords)))
