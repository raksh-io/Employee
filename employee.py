# employee.py
# Program to accept employee information and return a formatted string (with default values)

import sys

def get_employee_details(
        name="John Doe",
        emp_id="E1001",
        department="IT",
        salary="50000"):
    """Return a formatted employee details string with defaults."""
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


if __name__ == "__main__":
    print("=== Employee Information Formatter (with Default Values) ===")

    try:
        if len(sys.argv) == 5:
            # Inputs from CLI
            emp_name = sys.argv[1]
            emp_id = sys.argv[2]
            emp_dept = sys.argv[3]
            emp_salary = sys.argv[4]
        else:
            # Use default values
            emp_name = "John Doe"
            emp_id = "E1001"
            emp_dept = "IT"
            emp_salary = "50000"

        print("\n=== Program Parameters ===")
        print("Name:", emp_name)
        print("Employee ID:", emp_id)
        print("Department:", emp_dept)
        print("Salary:", emp_salary)

        # Generate formatted output
        result = get_employee_details(emp_name, emp_id, emp_dept, emp_salary)

        print("\n=== Formatted Output ===")
        print(result)

    except Exception as e:
        print("An error occurred:", e)
