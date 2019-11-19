class TestClass:
    def instance_method(self):
        # Method of the object.
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        # Method of the class.
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        # regular function that is inside a class.
        print(f"Called static_method.")

# Call a instance method
object = TestClass()
object.instance_method()

# Call a classmethod
TestClass.class_method()

# Call a staticmethod
TestClass.static_method()
