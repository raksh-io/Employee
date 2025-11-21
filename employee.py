import sys

def get_employee_details(
        name,
        emp_id,
        department,
        salary):
    """Return a formatted employee details string with defaults."""
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

print(get_employee_details("Rakshat", 12, "MCA", 100000))