import random


class BSTNode:
    def init(self, passn_no, name):
        self.passn_no = passn_no
        self.name = name
        self.left = None
        self.right = None


class BusTicketManagementSystem:
    def init(self):
        self.root = None
        self.bus_seat = [[0] * 33 for _ in range(10)]

    def green_color(self):
        print("\033[1;32m", end="")

    def reset_color(self):
        print("\033[0m", end="")

    def insert(self, root, cust_id, name):
        if root is None:
            return BSTNode(cust_id, name)
        elif cust_id < root.passn_no:
            root.left = self.insert(root.left, cust_id, name)
        else:
            root.right = self.insert(root.right, cust_id, name)
        return root

    def reservation_info(self, root, s):
        if root is None:
            return None

        if root.passn_no == s:
            self.green_color()
            print("\n-----------------------------------------------------------------")
            print(f"              NAME: {root.name:10}                                           ")
            print(f"              CUSTOMER ID: {root.passn_no: <10}                              ")
            print(f"              BUS NUMBER: {root.passn_no // 1000: <10}                       ")
            print(f"              SEAT NUMBER: {root.passn_no % 100: <10}                        ")
            print(f"              TICKET COST: Tk.{self.cost(root): <10}                         ")
            print("-----------------------------------------------------------------")
            self.reset_color()
            input("Press any key to continue...")
            return root
        elif root.passn_no > s:
            return self.reservation_info(root.left, s)
        else:
            return self.reservation_info(root.right, s)

    def display_seat(self, bus):
        for i in range(1, 33):
            self.green_color()
            print(f"{i:02d}. ", end="")
            self.reset_color()
            if bus[i] == 0:
                print("EMPTY", end=" ")
            else:
                print("BOOKED", end=" ")
            print("         ", end="")
            if i % 4 == 0:
                print()
        print()

    def login(self):
        username = "user"
        password = "Avisheikh001"

        print("\n\n=========================================================================================")
        print("\n\t\t\t\tWELCOME TO OUR BUS TERMINAL\n\n\t\t\t\t   'Have a safe Journey'")
        print("\n\n=========================================================================================\n\n")

        while True:
            match_user = input("\n\nUserName: ")
            match_pass = input("\nPassWord: ")

            if match_user == username and match_pass == password:
                print("\nLOGGED IN SUCCESSFULLY...\n")
                break
            else:
                self.green_color()
                print("\nINVALID DETAILS TRY AGAIN...\n")
                self.reset_color()

    def cost(self, node):
        bus_cost = node.passn_no // 1000
        if bus_cost % 3 == 1:
            return 2000
        elif bus_cost % 3 == 2:
            return 1000
        elif bus_cost % 3 == 0:
            return 1500
        return 0

    def status(self):
        self.bus_lists()
        while True:
            try:
                bus_num = int(input("\n\nENTER YOUR BUS NUMBER : "))
                if bus_num <= 0 or bus_num >= 10:
                    self.green_color()
                    print("\n  PLEASE ENTER CORRECT BUS NUMBER !!\n")
                    self.reset_color()
                else:
                    break
            except ValueError:
                self.green_color()
                print("\n  PLEASE ENTER A VALID NUMBER !!\n")
                self.reset_color()

        print()
        self.display_seat(self.bus_seat[bus_num])