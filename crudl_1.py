from prettytable import PrettyTable

class Person:
    def __init__(self, name, person_id, gender, year_level, course):
        self.name = name
        self.id = person_id
        self.gender = gender
        self.yearlevel = year_level
        self.course = course


class PeopleList:
    def __init__(self):
        self.people = []

    def create_person(self, name, person_id, gender, year_level, course):
        person = Person(name, person_id, gender, year_level, course)
        self.people.append(person)
        print(f"Person '{name}' added successfully!")

    def read_people(self):
        if not self.people:
            print("No people available!")
        else:
            table = PrettyTable(["Student Name", "ID Number", "Gender", "Course", "Year Level"])
            for person in self.people:
                table.add_row([person.name, person.id, person.gender, person.yearlevel, person.course])
            print(table)

    def update_person(self, person_id, name=None, gender=None, course=None, year_level=None):
        for person in self.people:
            if person.id == person_id:
                if name:
                    person.name = name
                if gender:
                    person.gender = gender
                if course:
                    person.course = course
                if year_level:
                    person.year_level = year_level
                print(f"Person with ID {person_id} updated successfully!")
                return
        print(f"Person with ID {person_id} not found!")

    def delete_person(self, person_id):
        for person in self.people:
            if person.id == person_id:
                self.people.remove(person)
                print(f"Person with ID {person_id} deleted successfully!")
                return
        print(f"Person with ID {person_id} not found!")

    def clear_people(self):
        self.people.clear()
        print("All people cleared successfully!")


def main():
    people_list = PeopleList()

    while True:
        print("\n===== STUDENT INFORMATION SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Clear All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Student Name: ")
            person_id = input("Enter  ID Number: ")
            gender = input("Enter  Gender: ")
            course = input("Enter  Course: ")
            year_level = input("Enter  Year level: ")
            people_list.create_person(name, person_id, gender, course, year_level)
        elif choice == "2":
            people_list.read_people()
        elif choice == "3":
            person_id = input("Enter person's ID to update: ")
            name = input("Enter new name (press enter to keep the current name): ")
            gender = input("Enter new gender (press enter to keep the current gender): ")
            people_list.update_person(person_id, name, gender)
        elif choice == "4":
            person_id = input("Enter person's ID to delete: ")
            people_list.delete_person(person_id)
        elif choice == "5":
            confirm = input("Are you sure you want to clear all people? (y/n): ").lower()
            if confirm == "y":
                people_list.clear_people()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
