CREATE DATABASE book_club;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
)

CREATE TABLE books_read (
    id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    author VARCHAR(60) NOT NULL,
    rating INTEGER DEFAULT 1 CHECK (rating BETWEEN 1 AND 5),
    read_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_member
        FOREIGN KEY (member_id)
        REFERENCES members(id)
        ON DELETE CASCADE
);

INSERT INTO members (username, full_name, join_date, is_active)
VALUES
    ('Astro', 'Astro Lab', '2022-01-05 09:15:00', TRUE),
    ('Bondly', 'James Bond', '2023-11-12 14:30:00', FALSE),
    ('Millman', 'Chase Miller', '2023-01-05 08:45:00', TRUE),
    ('Jessy', 'Jessy Walker', '2024-04-08 16:10:00', FALSE),
    ('Vicky', 'Veronica Mensah', '2024-04-05 11:20:00', TRUE),
    ('Code_crafter', 'John Mensah', '2025-06-22 19:05:00', FALSE),
    ('Ice reader', 'Prince Agyemang', '2026-01-05 07:50:00', TRUE)

INSERT INTO books_read (member_id, title, author, rating, read_date)
VALUES
    (3, 'Atomic Habits', 'James Clear', 4, '2023-11-05 10:20:00'),
    (2, 'Clean Code', 'Robert C. Martin', 3, '2024-03-15 14:05:00'),
    (1, 'The Pragmatic Programmer', 'Andrew Hunt', 4, '2023-07-10 09:30:00'),
    (4, 'Dracula', 'Bram Stoker', 5, '2024-08-02 18:15:00'),
    (6, 'Introduction to Algorithms', 'Thomas H. Cormen', 2, '2025-07-05 11:45:00'),
    (4, 'Black Beauty', 'Anna Sewell', 4, '2024-11-25 16:10:00'),
    (7, 'The Stranger', 'Albert Camus', 3, '2026-01-10 08:50:00'),
    (5, 'Mockingjay', 'Suzanne Collins', 4, '2025-09-15 13:25:00'),
    (4, 'The Secret Agent', 'Joseph Conrad', 5, '2025-01-08 17:40:00'),
    (7, 'The Client', 'John Grisham', 2, '2026-01-20 07:55:00');

SELECT * FROM members 
SELECT * FROM books_read 

DROP TABLE IF EXISTS members CASCADE
DROP TABLE IF EXISTS books_read 

