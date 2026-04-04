CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(
    id    INTEGER,
    name  VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        WHERE c.name  ILIKE '%' || p_pattern || '%'
           OR c.phone ILIKE '%' || p_pattern || '%'
        ORDER BY c.name;
END;
$$ language plpgsql;

CREATE OR REPLACE FUNCTION get_contacts(
    p_limit INTEGER DEFAULT 10,
    p_offset INTEGER DEFAULT 0
)
RETURNS TABLE(
    id  INTEGER,
    name VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        ORDER BY c.id
        LIMIT  p_limit
        OFFSET p_offset;
END;
$$ language plpgsql;
