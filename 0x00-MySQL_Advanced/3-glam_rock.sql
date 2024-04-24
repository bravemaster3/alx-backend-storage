-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- SCRIPT
SELECT band_name, IFNULL(split, 2022)-formed as lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
