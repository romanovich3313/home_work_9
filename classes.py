from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone, new_phone):
        old_index = self.phones.index(old_phone)
        self.phones[old_index] = new_phone           


class Field:
    pass


class Name:
    def __init__(self, name):
        self.name = name
        


class Phone:
    pass



