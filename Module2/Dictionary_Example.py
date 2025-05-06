contact_info = {
    'Alice': {
        'Phone': "049321654",
        "email": "alice@gmail.com",
        "address": "123 rruga kryesore prishtine",
        "birthday": "20/11/1997"
    },
    'Bob': {
        'Phone': "049321654",
        "email": "Bob@gmail.com",
        "address": "123 rruga kryesore prishtine",
        "birthday": "20/08/1997"
    },
    'Eve': {
        'Phone': "049321654",
        "email": "Eve@gmail.com",
        "address": "423 rruga kryesore prishtine",
        "birthday": "20/11/1997"
    },


    #2, create 2 new personas Jane and John
    'Jane':{
        'Phone': "048123432",
        "email": "Jane@gmail.com",
        "address": "743 rruga kryesore prishtine",
        "birthday": "23/05/1997"
    },
    'John':{
        'Phone': "049543267",
        "email": "John@gmail.com",
        "address": "634 rruga kryesore prishtine",
        "birthday": "14/09/1997"
    }
}
print(contact_info)
#1. print out Bob's info
print(contact_info['Bob'])

#3. print Jane's info
print(contact_info['Jane'])

#4. update Jane's phone number and print
print(contact_info['Jane']['Phone'])


