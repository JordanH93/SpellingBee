BANNER = """
███████╗██████╗ ███████╗██╗     ██╗     ██╗███╗   ██╗ ██████╗     ██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██║     ██║     ██║████╗  ██║██╔════╝     ██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  ██║     ██║     ██║██╔██╗ ██║██║  ███╗    ██████╔╝█████╗  █████╗  
╚════██║██╔═══╝ ██╔══╝  ██║     ██║     ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══╝  ██╔══╝  
███████║██║     ███████╗███████╗███████╗██║██║ ╚████║╚██████╔╝    ██████╔╝███████╗███████╗
╚══════╝╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝
"""
WELCOME = """
Welcome to Spelling Bee!
        Please choose a difficulty to begin playing:
        .1) Easy
        .2) Moderate
        .3) Difficult
"""


#class Validate:
"""
    def select_difficulty(self):
        while True:
            try:
                self.clear()
                print(BANNER)
                choice = int(input(WELCOME))
                if choice == 1:
                    return "Easy"
                elif choice == 2:
                    return "Moderate"
                elif choice == 3:
                    return "Difficult"
                else:
                    print("Please choose a valid difficulty")
            except:
                print("Please enter a valid option.")

    # Using 150 line breaks instead of clear because cls does not work on some IDEs
    # - Can turn off if too annoying
    @staticmethod
    def clear():
        clr = True
        if clr:
            print('\n' * 150)
"""