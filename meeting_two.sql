SELECT * FROM users
SELECT * FROM tasks

-- selection based on conditions
select * from tasks
where tasks.priority < 4

select * from tasks
order by tasks.priority ASC

select * from tasks
order by tasks.priority DESC

--first four queries (pagination)
select * from tasks
ORDER BY tasks.priority ASC
LIMIT 5

--using subqueries
select tasks.title, tasks.description, tasks.priority, tasks.user_id, tasks.completed
from tasks
where tasks.user_id in (select id from users where users.username = 'mphil')


--updates
UPDATE tasks
set completed = TRUE
where tasks.id = 4
RETURNING *;

UPDATE users
set username = 'luk'
where users.email = 'luk@gmail.com'
RETURNING *;

update tasks
    set title = 'Eat pizza',
    description = 'pizza from chicken man'
where tasks.id = 1
RETURNING *;

select * from tasks
select * from users

--updating using a subquery
update tasks
    set title = 'Play video games', 
    description = 'on the ps5'
where tasks.user_id in (select id from users where username = 'Mikey')
RETURNING *;

INSERT INTO users(username, full_name, email)
VALUES ('astro_boy', 'Dunc Oswald', 'astro@gmail.com')

-- deletion
DELETE FROM users
where username = 'kweku'



