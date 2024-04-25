-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    -- Calculate the weighted sum and sum of weights for all users
    UPDATE users u
    JOIN (
        SELECT c.user_id,
               SUM(c.score * p.weight) AS weighted_sum_score,
               SUM(p.weight) AS sum_weights
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS t ON u.id = t.user_id
    SET u.average_score = IF(t.sum_weights > 0, t.weighted_sum_score / t.sum_weights, 0);
END//

DELIMITER ;
