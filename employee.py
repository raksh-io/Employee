import sys

def get_employee_details(name, emp_id, department, salary):
    """Return a formatted employee details string exactly matching the test."""
    return (
        f"Employee Name: {name},"
        f"Employee ID: {emp_id},"
        f"Department : {department},"
        f"Salary : {salary}"
    )

if __name__ == "__main__":
    print(get_employee_details("Alice Smith", "E1234", "HR", "60000.00"))
