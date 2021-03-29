import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

countryCode=0
phoneNum=0

def ccode():
    global countryCode
    countryCode = input("Enter Country Code: ")

    if len(countryCode) > 3 or len(countryCode) < 3:
        print("Incorrect length!! TRY AGAIN")
        ccode()
    else:
        return countryCode


def pnum():
    global phoneNum
    phoneNum=input("Enter Phone Number: ")
    if len(phoneNum) > 10 or len(phoneNum) < 10:
        print("Incorrect length!! TRY AGAIN")
        pnum()
    else:
        return phoneNum


ccode()
pnum()
number=countryCode+phoneNum
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))