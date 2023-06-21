# Write your MySQL query statement below
select patient_id, patient_name, conditions
from patients
where conditions like"Diab1%" or conditions like"% Diab1%"