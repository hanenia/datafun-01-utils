"""
This is to show the salary of the employees, technicians only at this point, of the fictional Hanna Pharma. 
Last updated January 12, 2024.
"""
import math
import statistics

def main(): 
    print(byline)
    
#defining all variables
Company: str="Hanna Pharma"
Technicians_all_shift: int=8 #total sum of technicians in all shifts
Median_time_at_company_by_role: float=3.8 #This is only for technicians at this point, but could be expanded to more roles as query is built on. 
Role_Blue_badge: bool=True #Defines if role is direct employee or contractor
Shift: list= ["Front_day, Front_night, Back_day, Back_night"] # list of Shifts
Average_salary_for_role_by_shift: list=[26.5,32.2,27.5,35.3]

#strings made from above variables
active_players_string: str=f"There are {Technicians_all_shift} in the job role."
Role_Blue_badge_string: str=f"Is this a blue badge role? {Role_Blue_badge}"
Median_time_at_company_by_role_string: str=f"The median time an employee s role has been in this role is {Median_time_at_company_by_role} years."
Average_salary_for_role_by_shift_string: str = f"The average salary by shift are {Average_salary_for_role_by_shift}"

# Find the statistics for numeric list.
smallest = min(Average_salary_for_role_by_shift)
largest = max(Average_salary_for_role_by_shift)
total = sum((Average_salary_for_role_by_shift))
count = len(Average_salary_for_role_by_shift)
mean = statistics.mean(Average_salary_for_role_by_shift)
mode = statistics.mode(Average_salary_for_role_by_shift)
median = statistics.median(Average_salary_for_role_by_shift)
standard_deviation= statistics.stdev(Average_salary_for_role_by_shift)

#creating a string for all batting stats to be called on in byline
Salary_stats_string: str = f"""
  Descriptive statistics for average salary for role
  smallest: {smallest}
  largest: {largest}
  total: {total}
  count: {count}
  mean: {mean}
  mode: {mode}
  median: {median}
  standard deviation: {standard_deviation}
"""

byline: str=f"""
{Company}
{Role_Blue_badge_string}
{Median_time_at_company_by_role_string}
{Average_salary_for_role_by_shift_string}
{Salary_stats_string}
"""

#code can only run from this script
if __name__ == '__main__':
    main()
