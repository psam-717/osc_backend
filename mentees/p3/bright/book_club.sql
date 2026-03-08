DROP TABLE IF EXISTS books_read;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE books_read (
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL REFERENCES members(id),
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    read_date DATE NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5)
);

INSERT INTO members (username, full_name, join_date, is_active)
VALUES
    ('kofi_reads', 'Kofi Mensah', '2024-01-10', TRUE),
    ('ama_bookworm', 'Ama Owusu', '2024-02-15', TRUE),
    ('kwame23', 'Kwame Asante', '2024-03-05', TRUE),
    ('abena_lit', 'Abena Darko', '2024-04-20', FALSE);

INSERT INTO books_read (member_id, title, author, read_date, rating)
VALUES
    (1, 'Things Fall Apart', 'Chinua Achebe', '2024-02-01', 5),
    (1, 'Purple Hibiscus', 'Chimamanda Adichie', '2024-03-10', 4),
    (2, 'Half of a Yellow Sun', 'Chimamanda Adichie', '2024-03-20', 5),
    (3, 'The Alchemist', 'Paulo Coelho', '2024-04-01', 4),
    (4, 'Americanah', 'Chimamanda Adichie', '2024-05-15', 3);

SELECT * FROM members;

SELECT * FROM books_read;

SELECT members.full_name, books_read.title, books_read.rating
FROM members
JOIN books_read ON members.id = books_read.member_id;

SELECT * FROM members WHERE is_active = TRUE;
