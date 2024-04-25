-- SQL script that creates an index idx_name_first on the table names and the first letter of name.
-- SQL script
ALTER TABLE names
ADD COLUMN first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;
CREATE INDEX idx_name_first on names (first_letter);
