SELECT MAX(E.Salary) "SecondHighestSalary"
FROM Employee E
WHERE E.Salary < (
    SELECT MAX(Salary)
    FROM Employee
)
LIMIT 1;