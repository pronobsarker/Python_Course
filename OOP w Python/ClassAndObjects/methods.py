# Creating class
class Phone:
    ''''''

    name = 'Iphone'
    price = 1000000
    brand = 'Apple'
    features = ['camera', 'speaker', 'battery']

    # method

    # The self parameter in Python's Object-Oriented Programming (OOP) is a reference to the instance of the object itself.
    # It is automatically passed as the first argument when you call a method on an instance, allowing you to access the instance's attributes and other methods within that method.
    def call(self):
        print("calling person one")

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text

    # How self Works
    def show_model(self):
        print(f"Showing the phone model: {self.name}")

# Create an instance of the class
my_phone = Phone()  # Note the parentheses here to instantiate the class

my_phone.show_model

# When show_model() is called via the my_phone instance, Python internally converts it to:

# Phone.show_model(my_phone)
# So, self in show_model(self) actually refers to my_phone.



# Now use the instance to call methods and access attributes
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)
