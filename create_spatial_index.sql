CREATE INDEX idx_name
  ON schema_name.table_name
  USING GIST (geometry_column);
