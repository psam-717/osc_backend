-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(50) UNIQUE NOT NULL,
--     full_name VARCHAR(100) NOT NULL,
--     email TEXT UNIQUE NOT NULL,
--     is_active BOOLEAN DEFAULT TRUE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

-- )

-- INSERT INTO users (username, full_name, email)
-- VALUES 
--     ('kweku', 'Sage User', 'kweku@gmail.com')




-- SELECT * FROM tasks

-- CREATE TABLE tasks (
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     description TEXT,
--     priority INTEGER DEFAULT 1 CHECK (priority BETWEEN 1 AND 5),
--     completed BOOLEAN DEFAULT FALSE,
--     user_id INTEGER NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

--     CONSTRAINT fk_user
--         FOREIGN KEY (user_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE
-- );



SELECT * FROM  tasks

INSERT INTO tasks (title, description, user_id, priority)
VALUES
    ('Feed the dog', 'Give it some fried chicken', 5, 5)