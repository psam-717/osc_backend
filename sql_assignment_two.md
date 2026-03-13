# PostgreSQL Assignment – Session 2  
**Working with Data in the Book Club Database**

**Goal**  
Practice reading, filtering, sorting, updating and deleting data using the `book_club` database you created in Session 1.

You will use **only** the two tables you already created:

- `members`  
- `books_read`

**Instructions**

1. **Basic retrieval & filtering** (4 points)

   Write SELECT queries that return:

   a. All columns and all rows from the `members` table  
   b. All columns and all rows from the `books_read` table  
   c. Only the books that have a rating of 4 or higher  
      Show: `title`, `author`, `rating`, `read_date`  
   d. All members who joined **before January 1, 2024**  
      Show: `username`, `full_name`, `join_date`

2. **Sorting & limiting** (4 points)

   Write SELECT queries that:

   a. Show the 5 highest-rated books (highest rating first)  
      Include: `title`, `author`, `rating`, `member_id`  
      If two books have the same rating, sort by `read_date` descending

   b. Show the **3 most recently joined active members**  
      Show: `username`, `full_name`, `join_date`  
      Only include members where `is_active = true` (or equivalent)

3. **Subquery practice** (5 points)

   Write a SELECT query using a subquery that returns:

   - The `title`, `author`, `rating` and `read_date` of every book  
   - **only** for members whose `username` is `'sarahreads'` or `'bookworm_kofi'`  
   (use the actual usernames that exist in your `members` table — if you don’t have these exact usernames, choose two real ones from your data)

4. **UPDATE operations** (6 points)

   Perform the following updates and use `RETURNING *` in each case:

   a. Change the `rating` to 5 for **one specific book** (choose any book by its `id`)  
   b. Mark one member as inactive (`is_active = false`) using their `username`  
   c. Increase the rating by 1 for **all books** read by a specific member  
      (choose one member and use a subquery to find their `member_id`)

5. **DELETE operation** (3 points)

   a. Delete **one book entry** that has the lowest rating in your table  
      (you can hardcode the `id` after finding it, but show the SELECT you used to find the lowest-rated book)  
   b. Run `SELECT * FROM books_read` after the deletion to show the table state

**Important rules**

- Do **not** drop or recreate the tables or database  
- All queries must work on the data you inserted in Session 1  
- Use `RETURNING *` whenever you perform UPDATE or DELETE (unless the question says otherwise)  
- Write clean, readable SQL (good indentation, consistent keywords casing)

**What to submit**

Create a file named `book_club_session2_yourname.sql` (or `.md` if you prefer) containing:

1. All your SELECT, UPDATE and DELETE queries clearly numbered / labelled (1a, 1b, 2a, …)
2. After each query that returns data, include a comment block with the result you got, e.g.:

```sql
-- Result:
-- title             | author          | rating | read_date
-- ------------------+-----------------+--------+------------
-- Project Hail Mary | Andy Weir       | 5      | 2025-02-10
-- ...

Submit by: Sunday, 15/03/26
Good luck — take your time and test each query!