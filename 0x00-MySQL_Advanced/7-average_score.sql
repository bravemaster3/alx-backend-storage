-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- SQL Stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user_id;

    IF average_score IS NULL THEN
        SET average_score = 0;
    END IF;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //

DELIMITER ;
