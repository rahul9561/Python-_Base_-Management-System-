from db import setup_database
from employee import Employee
from manager import EmployeeManager
from visualize import visualize_data
from automation import export_to_csv

def menu():
    setup_database()
    manager = EmployeeManager()

    while True:
        print("\n📌 Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Visualize Data")
        print("6. Export Data to CSV")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(name, age, dept, salary)
            manager.add_employee(emp)

        elif choice == "2":
            employees = manager.view_employees()
            for row in employees:
                print(row)

        elif choice == "3":
            emp_id = int(input("Enter Employee ID: "))
            field = input("Enter field to update (name, age, department, salary): ")
            value = input("Enter new value: ")
            if field in ["age", "salary"]:
                value = float(value) if field == "salary" else int(value)
            manager.update_employee(emp_id, field, value)

        elif choice == "4":
            emp_id = int(input("Enter Employee ID: "))
            manager.delete_employee(emp_id)

        elif choice == "5":
            visualize_data()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
