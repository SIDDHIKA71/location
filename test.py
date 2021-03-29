import streamlit as st
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def main():
    st.title("Phone Number Location Tracker and Service Operator")
    st.subheader("Build with Python and StreamLit")
    countryCode = st.text_input("Enter Country Code: ")
    if len(countryCode) > 3 or (len(countryCode) < 3 and len(countryCode)>0):
        st.text("Incorrect lenght!! TRY AGAIN")
    phoneNum = st.text_input("Enter Phone Number: ", type="password")
    if len(phoneNum) > 10 or (len(phoneNum) < 10 and len(phoneNum)>0):
        st.text("Incorrect lenght!! TRY AGAIN")
    number = countryCode + phoneNum
    if st.button("Track"):
        if(len(number)<1):
            st.text("Can't be Null")
        elif len(number)<13  or len(number)>13:
            st.text("enter Correct Input")
        else:
            ch_number = phonenumbers.parse(number, "CH")
            st.success("Country Name: {}".format(geocoder.description_for_number(ch_number, "en")))
            service_operator = phonenumbers.parse(number, "RO")
            st.success("Service Operator Name: {}".format(carrier.name_for_number(service_operator, "en")))
if __name__=="__main__":
    main()