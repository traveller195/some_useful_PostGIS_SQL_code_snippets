-- create new table, only with ID and modified geometry

CREATE TABLE schema_name.table_name_repair AS SELECT id, ST_MakeValid(geometry) AS geometry FROM schema_name.table_name;

-- join repaired geometry to original table
-- handle unexpected geometry types as a result of repairing

UPDATE schema_name.table_name dest SET geometry = src.geometry
FROM
	(SELECT 
	  g.id,
	  g.geometry 
	FROM 
	  (SELECT 
	   id,
	   ST_Multi((ST_DUMP(ST_MakeValid (geometry))).geom) AS geometry FROM schema_name.table_name_repair
	   ) AS g
	WHERE ST_GeometryType(g.geometry) = 'ST_MultiPolygon' 
	   OR ST_GeometryType(g.geometry) = 'ST_Polygon') AS src
WHERE dest.id=src.id;


-- check number of existing geometry types in the end

SELECT ST_GeometryType(geometry) AS GeometryType, COUNT(*) AS Anzahl 
FROM schema_name.table_name 
GROUP BY ST_GeometryType(geometry) 
ORDER BY Anzahl DESC;
