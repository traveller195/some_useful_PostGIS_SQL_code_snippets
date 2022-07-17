CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
uuid_in(md5(random()::text || clock_timestamp()::text)::cstring) AS "id"
