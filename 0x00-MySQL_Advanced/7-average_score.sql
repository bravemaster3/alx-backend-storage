-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- SQL Stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(CAST(score AS FLOAT)) INTO average_score
    FROM corrections c
    WHERE c.user_id = user_id;

    -- Debugging: Print average score
    -- SELECT * FROM corrections WHERE user_id = (SELECT id FROM users WHERE name = 'Jeanne');

    IF average_score IS NULL THEN
        SET average_score = 0;
    END IF;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //

DELIMITER ;
