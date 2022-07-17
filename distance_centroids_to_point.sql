-- how to calculate the distance for polygons (centroid) to one given point?

UPDATE schema_name.table_name
SET column1 = St_Distance(St_Centroid(geometry), St_Transform(ST_SetSRID( ST_Point( 11.575501, 48.137227), 4326), 25832));
