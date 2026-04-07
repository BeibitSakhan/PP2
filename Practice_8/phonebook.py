import psycopg2
from connect import get_connection, get_cursor
 
def create_table(conn):
    """Create the phonebook table if it does not exist."""
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id         SERIAL PRIMARY KEY,
        first_name VARCHAR(50)  NOT NULL,
        last_name  VARCHAR(50)  NOT NULL DEFAULT '',
        phone      VARCHAR(20)  NOT NULL,
        UNIQUE (first_name, last_name)
    );
    """
    with get_cursor(conn) as cur:
        cur.execute(sql)
    conn.commit()
    print("✔  Table 'phonebook' is ready.")
 
 
def load_sql_file(conn, path: str):
    """Execute every statement in a .sql file."""
    with open(path, "r", encoding="utf-8") as fh:
        sql = fh.read()
    with get_cursor(conn) as cur:
        cur.execute(sql)
    conn.commit()
    print(f"✔  Loaded {path}")
 

def search_contacts(conn, pattern: str) -> list:
    """Call the search_contacts(text) SQL function."""
    with get_cursor(conn) as cur:
        cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
        return cur.fetchall()
 
 
def get_page(conn, limit: int = 5, offset: int = 0) -> list:
    """Call the get_contacts_page(limit, offset) SQL function."""
    with get_cursor(conn) as cur:
        cur.execute("SELECT * FROM get_contacts_page(%s, %s);", (limit, offset))
        return cur.fetchall()
 
 
def upsert_contact(conn, first_name: str, last_name: str, phone: str):
    """CALL upsert_contact(…) stored procedure."""
    try:
        with get_cursor(conn) as cur:
            cur.execute(
                "CALL upsert_contact(%s, %s, %s);",
                (first_name, last_name, phone),
            )
        conn.commit()
        print(f"✔  Upserted: {first_name} {last_name} — {phone}")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"✘  Error: {exc.pgerror or exc}")
 
 
def upsert_contacts_bulk(conn, contacts: list[tuple]):
    """
    CALL upsert_contacts_bulk(…) for a list of (first, last, phone) tuples.
    Returns the string of invalid rows from the OUT parameter.
    """
    first_names = [c[0] for c in contacts]
    last_names  = [c[1] for c in contacts]
    phones      = [c[2] for c in contacts]
 
    try:
        with get_cursor(conn) as cur:
            cur.execute(
                "CALL upsert_contacts_bulk(%s::varchar[], %s::varchar[], %s::varchar[], NULL);",
                (first_names, last_names, phones),
            )
            # The OUT param is returned as the first (and only) result column
            row = cur.fetchone()
            invalid_info = row["p_invalid"] if row else "—"
        conn.commit()
        print(f"✔  Bulk upsert done. Invalid rows:\n{invalid_info}")
        return invalid_info
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"✘  Bulk upsert failed: {exc.pgerror or exc}")
        return None
 
 
def delete_contact(conn, first_name=None, last_name=None, phone=None):
    """CALL delete_contact(…) stored procedure."""
    try:
        with get_cursor(conn) as cur:
            cur.execute(
                "CALL delete_contact(%s, %s, %s);",
                (first_name, last_name, phone),
            )
        conn.commit()
        print("✔  Delete executed.")
    except psycopg2.Error as exc:
        conn.rollback()
        print(f"✘  Error: {exc.pgerror or exc}")
 
 

def print_table(rows, title=""):
    if title:
        print(f"\n{'─'*50}\n  {title}\n{'─'*50}")
    if not rows:
        print("  (no rows)")
        return
    print(f"  {'ID':<5} {'First':<15} {'Last':<15} {'Phone':<20}")
    print(f"  {'─'*4} {'─'*14} {'─'*14} {'─'*19}")
    for r in rows:
        print(f"  {r['id']:<5} {r['first_name']:<15} {r['last_name']:<15} {r['phone']:<20}")
 

MENU = """
╔══════════════════════════════════════╗
║     PhoneBook  —  Practice 8        ║
╠══════════════════════════════════════╣
║  1. Search contacts (by pattern)    ║
║  2. Show page of contacts           ║
║  3. Add / update one contact        ║
║  4. Bulk add / update contacts      ║
║  5. Delete contact                  ║
║  0. Exit                            ║
╚══════════════════════════════════════╝
"""
 
 
def menu_search(conn):
    pattern = input("  Enter search pattern: ").strip()
    rows = search_contacts(conn, pattern)
    print_table(rows, f"Results for '{pattern}'")
 
 
def menu_page(conn):
    try:
        limit  = int(input("  Rows per page [5]: ").strip() or 5)
        offset = int(input("  Offset (0-based) [0]: ").strip() or 0)
    except ValueError:
        print("  ✘  Please enter integers.")
        return
    rows = get_page(conn, limit, offset)
    print_table(rows, f"Page (limit={limit}, offset={offset})")
 
 
def menu_upsert(conn):
    first = input("  First name: ").strip()
    last  = input("  Last name : ").strip()
    phone = input("  Phone     : ").strip()
    upsert_contact(conn, first, last, phone)
 
 
def menu_bulk(conn):
    print("  Enter contacts one per line as: FirstName LastName Phone")
    print("  Leave a blank line when done.")
    contacts = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        parts = line.split()
        if len(parts) != 3:
            print("  ⚠  Expected exactly 3 fields; skipping this line.")
            continue
        contacts.append(tuple(parts))
    if contacts:
        upsert_contacts_bulk(conn, contacts)
    else:
        print("  No contacts entered.")
 
 
def menu_delete(conn):
    print("  Fill in at least one field (leave blank to skip):")
    first = input("  First name: ").strip() or None
    last  = input("  Last name : ").strip() or None
    phone = input("  Phone     : ").strip() or None
    delete_contact(conn, first, last, phone)
 
 
# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────
 
def main():
    conn = get_connection()
    print("✔  Connected to PostgreSQL.")
 
   
    create_table(conn)
    load_sql_file(conn, r"C:\Users\Beibit\Desktop\pp2\Practice_8\functions.sql")
    load_sql_file(conn, r"C:\Users\Beibit\Desktop\pp2\Practice_8\procedures.sql")
 
    handlers = {
        "1": menu_search,
        "2": menu_page,
        "3": menu_upsert,
        "4": menu_bulk,
        "5": menu_delete,
    }
 
    while True:
        print(MENU)
        choice = input("  Your choice: ").strip()
        if choice == "0":
            print("  Bye!")
            break
        handler = handlers.get(choice)
        if handler:
            handler(conn)
        else:
            print("  ⚠  Unknown option; try again.")
 
    conn.close()
 
 
if __name__ == "__main__":
    main()