import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


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


class Reservation:
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


class CreditCard:
    def __init__(self,number):
        self.number = number


    def validate(self, exp, holder, cvc):
        card_data = {"number": self.number, "expiration": exp,
                     "holder": holder, "cvc": cvc}
        print(card_data)
        print(df_cards)
        if card_data in df_cards:
            return True
        else:
            return False



print(df)
hotel_id = input("Enter hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(number="1234567890123456")
    if credit_card.validate(exp="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation = Reservation(customer_name=name, hotel_object=hotel)
        print(reservation.generate())
    else:
        print("Sorry, there was a problem with your payment.")
else:
    print("Sorry, hotel is not available")