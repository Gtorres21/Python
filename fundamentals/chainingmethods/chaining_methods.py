class User:
    # all_users = []
    def __init__(self, first_name, last_name, email, age):
        # pass
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # Below are default Attributes
        self.rewards_member = False
        self.gold_card_points = 0
        # user.all_users.append(self)

    #  Have this method print all of the users' details on separate lines.

    def display_info(self):
        # print(f"{self.first_name} {self.last_name} {self.email} {self.age}")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        if self.gold_card_points == 0:
            self.gold_card_points = 200
            # print(self.gold_card_points)
        if self.rewards_member == False:
            self.rewards_member = True
            # print(self.rewards_member)

        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        print(self.gold_card_points)

        return self



user1=User("Giovanni","Torres","email.com",30)



user1.display_info().enroll().spend_points(100)

