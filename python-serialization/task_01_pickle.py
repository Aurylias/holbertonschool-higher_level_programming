"""Module to serialize/deserialize a Python dictionary in JSON"""
from pickle import dump, load

class CustomObject:
    """Constructor"""
    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = student

    @property
    def name(self):
        """Getter for name"""
        return self.__age

    @name.setter
    def name(self, name):
        """Setter for name"""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name

    @property
    def age(self):
        """Getter for age"""
        return self.__age

    @age.setter
    def age(self, age):
        """Setter for age"""
        if not isinstance(age, int):
            raise TypeError("age must be an int")
        self.__age = age

    @property
    def is_student(self):
        """Getter for is_student"""
        return self.__is_student

    @is_student.setter
    def is_student(self, is_student):
        """Setter for is_student"""
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a bool")


    def display(self):
        """Display all attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs student: \
              {self.is_student}")

    def serialize(self, filename):
        """Serialize the instance of this objet as a pickle"""
        try:
            with open(filename, wb) as pick:
                dump(self, pick)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a pickle file to load an instance of this class"""
        try:
            with open(filename, "rb") as pick:
                instance = load(pick)
            return instance
        except Exception:
            return None
