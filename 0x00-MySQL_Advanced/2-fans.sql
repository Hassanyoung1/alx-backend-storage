--  a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- import table from metal_band.sql
SELECT origin, COUNT(fans) AS nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
