-- Selects
SELECT * from tasks
where description is not NULL

SELECT * FROM tasks
where tasks.priority < 3

-- "order by" and "limit" clause 
SELECT tasks.title, tasks.description, tasks.priority
FROM tasks
ORDER BY tasks.priority DESC
LIMIT 3 

SELECT users.id, users.username, users.email
from users

-- selecting mphil's queries
select tasks.title, tasks.description, tasks.priority
from tasks where tasks.user_id in (select id from users where username = 'luk7654')

-- selection by ordering user_id in ascending order
SELECT * FROM tasks order by user_id asc

select users.id, users.email from users where users.username = 'mphil'
 

-- updates
UPDATE tasks
SET completed = TRUE
where tasks.user_id = 7

-- user wants to update description
UPDATE tasks
set description = 'Wash at the laundromat'
where tasks.title = 'Wash my clothes'

SELECT * FROM users
SELECT * FROM tasks order by user_id asc


-- updating multiple entries in a row simultaneously
UPDATE tasks
    set title = 'Deploy the backend',
    description = 'Deployment should be done via render'
where tasks.id = 5

-- updating and returning updated row
UPDATE tasks
    set priority = 2
where tasks.title = 'Do my assignment'
RETURNING *;

--updating using subquery
update tasks
    set description = 'walk to the next community'
where tasks.user_id in (select id from users where username = 'Mikey')
RETURNING *;


--deletion
Delete from tasks 
where description is NULL

select * from tasks


