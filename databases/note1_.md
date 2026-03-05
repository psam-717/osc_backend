# Database

    A structured collection of data for efficient storage, retrieval and management

## Types of Database

**Relational**: Stores data in structured tables with rows and columns, using a fixed schema. Data is linked across tables via relationships (keys like primary/foreign keys)

### Examples of relational dbs

- PostgreSQL
- Microsoft SQL Server
- My SQL

**Non-relational**: Stores data without a fixed table structure — uses flexible models like documents (JSON-like), key-value pairs, wide columns, or graphs. Schema is dynamic (can change easily).

### Examples of non-relational dbs

- MongoDB
- Redis

## Data types in postgresql and their categories

    * Numeric
        SERIAL: Auto-incrementing (primary key)
        INTEGER/INT: Ages,counts, IDs
        BIGINT: Very large numbers

    * Text
        VARCHAR(n): Names, usernames(limited length)
        TEXT:Descriptions, notes, long strings

    * Boolean
        BOOLEAN: Used for flags (is_active, completed, is_admin)

    * Date/Time
        TIMESTAMP: Created/updated times
        DATE: Birth dates, deadlines

    * JSON
        JSONB: Flexible semi-structured data

### Terminologies

**Table/Relation**: A structured collection of related data organized in rows and columns. In PostgreSQL, this is the main object where data lives

**Row/Tuple/Record**: A single entry/record in a table — one horizontal line representing one instance

**Column**: A vertical field in a table that holds a specific type of data for all rows

**Schema**: A logical namespace/container inside a database that groups related tables, views, etc. (PostgreSQL defaults to public schema)

### Data integrity terminologies

**Primary key**: One or more columns that uniquely identify each row in a table. Cannot be null or duplicated

**Foreign key**: A column (or set of columns) in one table that references the primary key of another table. Enforces relationships and referential integrity

**Candidate Key**: Any column(s) that could serve as a primary key (unique and not null). One is chosen as the actual PK; others become alternate keys


### Query examples

CREATE TABLE users (
    id          SERIAL PRIMARY KEY,               -- auto-incrementing ID
    username    VARCHAR(50) UNIQUE NOT NULL,      -- unique usernames
    full_name   VARCHAR(100) NOT NULL,
    email       TEXT UNIQUE NOT NULL,
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(150) NOT NULL,
    description TEXT,
    priority    INTEGER DEFAULT 1 CHECK (priority BETWEEN 1 AND 5),  -- constraint example
    completed   BOOLEAN DEFAULT FALSE,
    user_id     INTEGER NOT NULL,                  -- foreign key column
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign key constraint (links to users table)
    CONSTRAINT fk_user 
        FOREIGN KEY (user_id) 
        REFERENCES users(id)
        ON DELETE CASCADE     -- optional: delete tasks if user is deleted
);
