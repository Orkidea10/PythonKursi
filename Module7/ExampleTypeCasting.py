from Module5.Examples import rezultati

age=25
age_As_string=str(age)
print(age_As_string," of type ",type(age_As_string))

print(bool(0))# this is false because 0 is false in boolean
print(bool(42))#this is true bc 42 translates as 1

print(bool(""))
print(bool("Hello"))

#implicit TypeCasting
#x=32
#y=5.3
#rezultati=x+y
#print(rezultati,"of type", type(rezultati))


a=5
b='3'
rezultati1=a*int(b)
print(rezultati1, "of type ",type(rezultati1))


c=4
rezultati2="hello"*c
print(rezultati2, "of type ",type(rezultati2))


#get two numbers from user input then sum them up
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
result=a+b
print(result)