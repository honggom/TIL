-- Easy
-- 182. Duplicate Emails

select email from Person group by email having count(email) > 1