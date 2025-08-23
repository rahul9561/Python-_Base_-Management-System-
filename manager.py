from db import get_connection
from employee import Employee

class EmployeeManager:
    def add_employee(self, emp: Employee):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", emp.to_tuple())
        conn.commit()
        conn.close()
        print("✅ Employee added successfully.")

    def view_employees(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def update_employee(self, emp_id, field, new_value):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE employees SET {field}=? WHERE id=?", (new_value, emp_id))
        conn.commit()
        conn.close()
        print("✅ Employee updated successfully.")

    def delete_employee(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
        conn.commit()
        conn.close()
        print("✅ Employee deleted successfully.")
