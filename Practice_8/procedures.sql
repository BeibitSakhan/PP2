CREATE OR REPLACE FUNCTION is_valid_phone(p_phone TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN p_phone ~ '^\+?[0-9]{10,15}$';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name  VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NULL OR TRIM(p_name) = '' THEN
        RAISE EXCEPTION 'Esim bos bolmauy qazhet';
    END IF;
    IF NOT is_valid_phone(p_phone) THEN
        RAISE EXCEPTION 'Nomeriniz qate: %', p_phone;
    END IF;
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
        RAISE NOTICE 'Esiminin nomeri zhanardy %', p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
        RAISE NOTICE 'Zhana contact engizildi %', p_name;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE upsert_data(
    p_names  VARCHAR[],   -- ← must be arrays
    p_phones VARCHAR[],   -- ← was missing the [] and wrong param name used below
    OUT p_invalid TEXT
)
LANGUAGE plpgsql AS $$
DECLARE                   -- ← no parentheses here (this was the crash)
    v_len   INTEGER;
    v_name  VARCHAR;
    v_phone VARCHAR;
    v_i     INTEGER;
    v_bad   TEXT := '';
BEGIN
    v_len := array_length(p_names, 1);
    IF v_len IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Eki olshem birdei boluy qazhet!';
    END IF;
    FOR v_i IN 1..v_len LOOP
        v_name  := p_names[v_i];
        v_phone := p_phones[v_i];

        IF NOT is_valid_phone(v_phone) THEN
            v_bad := v_bad
                  || format('Row %s: %s — bad phone "%s"', v_i, v_name, v_phone)
                  || chr(10);
            CONTINUE;
        END IF;
        IF EXISTS (SELECT 1 FROM phonebook WHERE name = v_name) THEN
            UPDATE phonebook SET phone = v_phone WHERE name = v_name;
        ELSE
            INSERT INTO phonebook(name, phone) VALUES (v_name, v_phone);
        END IF;
    END LOOP;
    p_invalid := COALESCE(NULLIF(TRIM(v_bad), ''), 'All rows valid');
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(
    p_name  VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
DECLARE
    v_deleted INTEGER;
BEGIN
    IF p_name IS NULL AND p_phone IS NULL THEN
        RAISE EXCEPTION 'Provide at least one of: name, phone';
    END IF;

    DELETE FROM phonebook
    WHERE (p_name  IS NULL OR name  = p_name)
      AND (p_phone IS NULL OR phone = p_phone);

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    RAISE NOTICE 'Deleted % row(s)', v_deleted;
END;
$$;