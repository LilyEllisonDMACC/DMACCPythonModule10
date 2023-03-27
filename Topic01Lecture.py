class MyFirstClass:
    PI = 3.1415926535
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def hello_world(self):
        print("Hello, World!")

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


if __name__ == "__main__":
    my_obj = MyFirstClass("john", "smith")
    my_obj.hello_world()
    print(str(my_obj))
    print(str(my_obj.PI))