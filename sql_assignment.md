# PostgreSQL Assignment – Session 1

**Goal**  
Create a small database for a simple online book club to practice:

- Creating a database
- Creating tables with appropriate columns
- Choosing data types and constraints
- Using primary keys and foreign keys
- Inserting multiple rows

**Task**

1. Create a new database named `book_club`

2. Create **two tables** inside the `book_club` database:

   - **members** table  
     Must have at least these attributes (columns):  
     - id  
     - username  
     - full_name  
     - join_date  
     - is_active  

   - **books_read** table  
     Must have at least these attributes (columns):  
     - id  
     - member_id  
     - title  
     - author  
     - read_date  
     - rating  

   You decide:  
   - Which columns should be the primary key  
   - Which column should connect the two tables (foreign key)  
   - What data types to use for each column  
   - Which columns should be required  
   - Which columns should be unique  
   - Any default values  
   - Any reasonable checks (e.g. valid range for rating)

3. Insert at least **4 members** into the `members` table using **one multi-row INSERT statement**.  
   Make up realistic usernames, names, and join dates.

4. Insert at least **5 records** into the `books_read` table using **at least one multi-row INSERT statement**.  
   Make sure every `member_id` actually exists in the `members` table.


**What to submit**

- All your `CREATE DATABASE`, `CREATE TABLE`, and `INSERT` statements  
- The output (result rows) of each of those four SELECT queries


Good luck!
Submit by: Sunday, 08/03/26