CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT,
    is_complete BOOLEAN DEFAULT FALSE
);

CREATE TABLE tokens (
    token_id SERIAL PRIMARY KEY,
    user_id INT,
    token TEXT,
    created_at TIMESTAMP,
    expires_at TIMESTAMP
);


CREATE OR REPLACE FUNCTION count_incomplete()
RETURNS INT AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM tasks WHERE is_complete = FALSE);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE toggle_task(p_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE tasks SET is_complete = NOT is_complete WHERE id = p_id;
END;
$$;


CREATE OR REPLACE FUNCTION prevent_delete()
RETURNS trigger AS $$
BEGIN
    IF OLD.is_complete = FALSE THEN
        RAISE EXCEPTION 'Cannot delete incomplete task';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_delete
BEFORE DELETE ON tasks
FOR EACH ROW
EXECUTE FUNCTION prevent_delete();