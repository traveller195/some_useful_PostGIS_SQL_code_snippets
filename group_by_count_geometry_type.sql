
SELECT ST_GeometryType(geometry) AS GeometryType, COUNT(*) AS Anzahl 
FROM schema_name.table_name 
GROUP BY ST_GeometryType(geometry) 
ORDER BY Anzahl DESC;
