import argparse
from src.repository.file import read_file_lines
from src.domain.employee import Employee
from src.service.input_parsing import get_employee_name, get_employee_working_schedule


def main():

    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('Required arguments')
    optional = parser.add_argument_group('Optional arguments')
    required.add_argument("--input", "-i", help="Input file name containing the employees' information", required=True)
    optional.add_argument('-o', '--output', help='Output file name to store the results')
    args = parser.parse_args()

    employees_salary = []
    # Check for --input
    if args.input:
        input_file_name = args.input
        input_lines = read_file_lines(input_file_name)
        for line in input_lines:
            name = get_employee_name(line)
            working_schedule = get_employee_working_schedule(line)
            employee = Employee(name,working_schedule)
            employee.calculate_salary()
            print(employee)
            employees_salary.append(employee.__str__())
    if args.output:
        output_file_name = args.output
        with open(output_file_name, "w") as text_file:
            for employee in employees_salary:
                text_file.write(f'{employee}\n')        


if __name__ == "__main__":
    main()
