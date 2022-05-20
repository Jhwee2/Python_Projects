class members:

    def __init__(self):
        self.age = []
        self.name = []

    def read(self, filename):
        file = open(filename, "r")
        for line in file:
            name, age = line.split()
            self.name.append(name)
            self.age.append(age)
        file.close()

    def interface(self):
        print("=============================")
        print("Contact tracing")
        print("=============================")
        print("1 - Search Direct Contacts")
        print("2 - Search User pool")
        print("3 - Display Member Profile")
        print("0 - Exit Program")

    def contact(self):
        user = input("Please enter the name of the person you wish to find!")
        a = []
        for i in range(len(self.name)):
            if user == self.name[i]:
                a.append(i)
        if len(a) == 0:
            print("We cannot find this member in the system!")
        if len(a) != 0:
            print("Direct Contacts")
            print("====================")
            for i in a:
                if 2 <= i < len(self.name) - 2:
                    print(self.name[i - 2])
                    print(self.name[i - 1])
                    print(self.name[i + 1])
                    print(self.name[i + 2])
                elif i == 1:
                    print(self.name[i - 1])
                    print(self.name[i + 1])
                    print(self.name[i + 2])
                elif i == 0:
                    print(self.name[i + 1])
                    print(self.name[i + 2])
                elif i == len(self.name) - 2:
                    print(self.name[i - 2])
                    print(self.name[i - 1])
                    print(self.name[i + 1])
                elif i == len(self.name) - 1:
                    print(self.name[i - 2])
                    print(self.name[i - 1])

    def pool(self):
        name1 = input("Enter name of first member: ")
        name2 = input("Enter name of second member: ")
        name3 = input("Enter name of third member: ")
        a = []
        b = True
        for i in range(len(self.name)):
            if name1 == self.name[i]:
                a.append(i)
            if name2 == self.name[i]:
                a.append(i)
            if name3 == self.name[i]:
                a.append(i)
        for i in range(len(a)):
            if (a[i - 1] - a[i]) == -1:
                if (a[i] - a[i + 1]) == -1:
                    print("Yes these member have been in direct contact")
                    b = False
        if b:
            print("No these members have not been in direct contact")

    def summary(self):
        total = 0
        print("Min Age:", min(self.age))
        print("Max Age:",max(self.age))
        for i in self.age:
            total += int(i)
        print("Avg:", total / len(self.age))


x = members()
x.read("members.txt")
while True:
    x.interface()
    choice = input("Please Select an option 0-3:")
    if choice == "1":
        x.contact()
    if choice == "2":
        x.pool()
    if choice == "3":
        x.summary()
    if choice == "0":
        break
