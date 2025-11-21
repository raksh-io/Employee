#test_empluyee.py
from employee import get_employee_details

def test_get_employee_details():
    #Sample data
    name = "Alice Smith"
    emp_id = "E1234"
    department = "HR"
    salary = "60000.00"
    #expected output
    excepted_output = (
        "Employee Name: Alice Smith,"
        "Employee ID: E1234,"
        "Department : HR,"
        "Salary : 60000.00"
    )
    #assertion
    assert get_employee_details(name, emp_id, department, salary) == excepted_output