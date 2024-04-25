-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE sum_weights FLOAT;
    DECLARE weighted_sum_score FLOAT;
    DECLARE weighted_average FLOAT;

    -- calculate the weighted sum
    SELECT corrections.user_id, SUM(corrections.score * projects.weight)
    INTO weighted_sum_score
    FROM corrections
    INNER JOIN projects on corrections.project_id = projects.id
    GROUP BY corrections.user_id;

    -- calculate the sum of weights
    SELECT corrections.user_id, SUM(projects.weight)
    INTO sum_weights
    FROM projects
    INNER JOIN corrections on corrections.project_id = projects.id
    GROUP BY corrections.user_id;

    -- Calculate average score for the user and update the users table
    IF sum_weights > 0 THEN
        SET weighted_average = weighted_sum_score / sum_weights;
    ELSE
        SET weighted_average = 0;
    END IF;

    UPDATE users
    SET average_score = weighted_average
    WHERE id = user_id_param;
END//

DELIMITER ;

