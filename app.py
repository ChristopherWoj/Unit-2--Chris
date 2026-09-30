bill = input("How much was the bill")
service = input("how was the service")
float (bill)
if service == "okay":
    print (bill  * 1.15)
    print ("The service was okay. Heres a 15% tip")

elif service == "bad":
    print (bill + 0)
    print ("The service is terrible! No tip for you")

elif service == "good":
    print (bill * 1.20)
    print ("The service was pretty good. Heres a 20% tip")

elif service == "great":
    print (bill  * 1.25)
    print ("The service was great! Heres a 25% tip")