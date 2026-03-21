SELECT * FROM users

-- dropping one column from a table
ALTER TABLE users
DROP COLUMN phone;

-- dropping multiple columns
ALTER TABLE users
DROP COLumN last_login,
DROP COLumN profile_picture_url,
DROP COLumN role


-- adding a single column
ALTER TABLE users
ADD COLUMN phone VARCHAR(20);

-- adding a single column with a default value
ALTER TABLE users
ADD COLUMN due_date DATE DEFAULT CURRENT_DATE + INTERVAL '7 days';

-- adding multiple columns 
ALTER TABLE users
ADD COLUMN last_login TIMESTAMP DEFAULT NULL,
ADD COLUMN profile_pic_url TEXT

-- updating the entries for an exiting column
UPDATE users
SET phone = 'Not provided'
WHERE phone IS NULL

UPDATE users
set last_login = created_at + INTERVAL '3 days'
where last_login is NULL

UPDATE users
SET email = 'marv@gmail.com'
where email = 'mphil@gmail.com'



