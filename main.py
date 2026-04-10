import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_secure_cards = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()


    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


    def book(self):
        """Book a hotel by changing availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class SpaHotel(Hotel):
    def book_spa(self):
        pass


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
       content = f""""
        Thank you for your spa reservation!
        Here is your spa booking details:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
       """
       return content


class CreditCard:
    def __init__(self,number):
        self.number = number


    def validate(self, exp, holder, cvc):
        card_data = {"number": self.number, "expiration": exp,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        my_pass = df_secure_cards.loc[df_secure_cards["number"] == self.number, "password"].squeeze()
        if my_pass == given_password:
            return True
        else:
            return False


class SpaTicket():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
       content = f""""
        Thank you for your reservation!
        Here is your booking details:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
       """
       return content


print(df)
hotel_id = input("Enter hotel id: ")
hotel = SpaHotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(exp="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation = Reservation(customer_name=name, hotel_object=hotel)
            print(reservation.generate())
            book_spa_hotel = input("Do you want to book a spa?")
            if book_spa_hotel == "yes":
                hotel.book_spa()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                spa_reservation = spa_ticket.generate()
                print(spa_reservation)
            else:
                exit
        else:
            print("Sorry, credit card authentication failed")
    else:
        print("Sorry, there was a problem with your payment.")
else:
    print("Sorry, hotel is not available")