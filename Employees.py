# import the libraries
import csv
import os

# Define CSV file name
csv_filename = "Employees.csv"

# Define header
header = ["emp_id", "name", "department", "purpose", "email", "phone"]

# Define Data
rows = [
    [101, "Anuj", "Sales", "Client Meeting", "anuj@company.com", "9876543210"],
    [102, "Rashi", "Admin", "Manage Office Systems", "rashi@company.com", "9123456789"],
    [103, "Sneha", "HR", "Interview Candidate", "sneha@company.com", "9988776655"],
    [104, "Tanya", "IT", "Software Update", "tanya@company.com", "7065769445"]
]

# Check if file already exists
file_exists = os.path.isfile(csv_filename)

# Create and write CSV only if it doesn't exist
if not file_exists:
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)
    print("Employee CSV file created successfully")
else:
    print("CSV file already exists. Skipping creation")

# Ask user if they want to add a new employee
choice = input("Do you want to add a new employee? (yes/no): ").strip().lower()

if choice == "yes":
    # Gather new employee data
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    purpose = input("Enter Purpose: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    # Append new data to CSV file
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, department, purpose, email, phone])

    print(f"New employee {name} added successfully")

else:
    print("No new employee added.")



