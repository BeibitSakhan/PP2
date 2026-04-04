CREATE OR REPLACE FUNCTION is_valid_phone(p_phone TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN p_phone ~'\+?[0-9]{10,15}$';
END;
$$ language plpgsql;

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
Language plpgsql as $$
BEGIN
    IF p_name IS NULL OR TRIM (p_name) ='' THEN
        RAISE EXCEPTION 'Esim bos bolmauy qazhet';
    END IF;
    IF NOT is_valid_phone(p_phone) THEN
        RAISE EXCEPTION 'Nomeriniz qate: %', p_phone;
    END IF;
    IF EXISTS(SELECT 1 FROM contacts WHERE name=p_name) THEN
        UPDATE contacts SET phone=p_phone WHERE name=p_name;
        RAISE NOTICE 'Esiminin nomeri zhanardy %', p_name;
    ELSE
        INSERT INTO contacts(name,phone) VALUES (p_name,p_phone);
        RAISE NOTICE 'Zhana contact engizildi %', p_name;
    END IF;
END;
$$;


