-- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

select e.company_code, c.founder, 
        count(distinct e.lead_manager_code), 
        count(distinct e.senior_manager_code), 
        count(distinct e.manager_code), 
        count(distinct e.employee_code) 
from Employee e 
inner join Company c on e.company_code=c.company_code
group by e.company_code, c.founder
order by e.company_code;
