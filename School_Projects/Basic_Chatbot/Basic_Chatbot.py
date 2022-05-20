import random


class userinfo:
    def __init__(self):
        self.namelst = []
        self.userlst = []
        self.programlst = []

    def interface(self):
        print(25 * "=")
        print("Chatbot Services!")
        print(25 * "=")
        print("1 - Admin")
        print("2 - Client Therapy")
        print("3 - Quit Program")

    def admin(self):
        password = "admin123"
        holder = input("Please enter the password!")
        while True:
            if password == holder:
                print("Total amount of sessions: ", len(self.namelst))
                print("display client's input")
                print(list(enumerate(self.userlst)))
                print("Average length of client input: ", len(self.userlst) / len(self.namelst))
                lst = []
                for i in self.userlst:
                    for y in i.split(" "):
                        lst.append(y)
                dict = {i: lst.count(i) for i in lst}
                all_values = dict.values()
                for key, value in dict.items():
                    if value == max(all_values):
                        print("The most frequently used word is:", "\"", key, "\" which was used: ", max(all_values),
                              "times")
                dict2 = {i: self.programlst.count(i) for i in self.programlst}
                all_values2 = dict2.values()
                for key, value in dict2.items():
                    if value == max(all_values2):
                        print("The most frequently used program phrase is:", "\"", key, "\" which was used: ",
                              max(all_values2),
                              "times")
                break
            elif holder == "quit":
                break
            else:
                holder = input("Please enter the correct password! or type \"quit\"")

    def cases(self, response, lst, pglist):
        global hold
        elaborate = ["Please elaborate", "Please tell me more", "Go on", "Tell me more about this feeling"]
        ithink = ["Why do you think that way?", "Do you really think so", "I see..."]
        ifeel = ["Why do you feel that way?", "How often do you feel that way?"]
        hold = response.lower().split()

        while hold[-1] != "quit":
            while "you" in hold:
                response = input("We are here to talk about you, not me.\n")
                hold = response.lower().split()
                pglist.append("We are here to talk about you, not me.")
            if "mother" in hold:
                response = input("Tell me more about your mother\n")
                pglist.append("Tell me more about your mother")
            elif "father" in hold:
                response = input("Tell me more about your father\n")
                pglist.append("Tell me more about your father")
            elif "i" and "think" in hold:
                mid = ithink[random.randrange(len(ithink))]
                print(mid)
                pglist.append(mid)
                response = input()
            elif "i" and "feel" in hold:
                mid = ifeel[random.randrange(len(ifeel))]
                print(mid)
                pglist.append(mid)
                response = input()
            elif "i" and "want" and "to" in hold:
                response = input("What would it mean to you if you did that?\n")
                pglist.append("What would it mean to you if you did that?")
            elif "i" and "need" and "to" in hold:
                response = input("What would it mean to you if you did that?\n")
                pglist.append("What would it mean to you if you did that?")
            else:
                mid = elaborate[random.randrange(len(elaborate) - 1)]
                print(mid)
                pglist.append(mid)
                response = input()
                hold = response.split()
            hold = response.split()
            lst.append(response)
            self.programlst = pglist.copy()
            self.userlst = lst.copy()
        return response

    def therapy(self):
        print(
            "Hello, I am Jared! We can talk about anything you want. If you want to stop the conversation type "
            "\"quit\"")
        person = userinfo()
        greetings = ["Hello", "Hi", "Greetings"]
        user = input("What is your name?\n")

        while user != "quit":
            self.userlst.append(user)
            self.namelst.append(user)
            print(greetings[random.randrange(len(greetings) - 1)], self.namelst[-1] + "!",
                  "What would you like to discuss today?")
            user = input()
            if user == "quit":
                break
            else:
                self.userlst.append(user)
                user = person.cases(user, self.userlst, self.programlst)
        print("Okay! Hopefully we can talk again soon!")


x = userinfo()
while True:
    x.interface()
    choice = input("Please Select an option 1-3:\n")
    if choice == "1":
        x.admin()
    if choice == "2":
        x.therapy()
    if choice == "3":
        print("Thank you for using our services")
        break
