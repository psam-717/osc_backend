DROP TABLE IF EXISTS books_read;
DROP TABLE IF EXISTS members;
CREATE TABLE IF NOT EXISTS members(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);
INSERT INTO members(username,full_name,is_active) VALUES

    ('Muna','Memunatu Lukman',True),
    ('AstroLab', 'Joseph Ayebia',True),
    ('Mauve', 'Mauvis Tetteh',True),
    ('Ram', 'Ramla Abubakr',False),
    ('Bint','Bintu Abdul',True);

--SELECT * FROM members;

CREATE TABLE IF NOT EXISTS books_read(
    id SERIAL PRIMARY KEY,
    member_id INTEGER,
       CONSTRAINT kmembers
        FOREIGN KEY(member_id)
        REFERENCES members(id),
    title VARCHAR(50),
    author VARCHAR(100),
    read_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating FLOAT

);
INSERT INTO books_read(member_id,title,author,rating) VALUES
(2,'The Devil son','Kofi Aidoo',5.0),
(4,'Unity','Conti',4.0),
(1,'The Generous hunter','Yaa Asantewaa',3.0),
(3,'Atomic habits','Lukman Abdul-somed',2.0),
(5,'How to train your dragon', 'Bintu Abdullah',1.0);

SELECT * FROM books_read; 