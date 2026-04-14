SELECT * FROM users
SELECT * FROM tasks


-- adding a new column to an already existing table
ALTER TABLE users 
ADD COLUMN phone VARCHAR(20)

-- adding a new column and setting them with defaults
ALTER TABLE tasks
ADD COLUMN due_date DATE DEFAULT CURRENT_DATE + INTERVAL '7 days';


-- adding multiple columns
ALTER TABLE users
ADD COLUMN last_login TIMESTAMP DEFAULT NULL,
ADD COLUMN profile_picture_url TEXT,
ADD COLUMN role VARCHAR(10) DEFAULT 'user';



-- filling a newly created column
UPDATE users
SET phone = 'Not provided'
WHERE phone IS NULL;

UPDATE tasks
SET due_date = created_at + INTERVAL '3 days'
WHERE due_date IS NULL;