def parse_query(query):
    query = query.strip().rstrip(";")

    if not query.upper().startswith("SELECT"):
        raise Exception("Only SELECT queries supported")

    select_part, rest = query.split("FROM")
    select_cols = select_part.replace("SELECT", "").strip()

    if "WHERE" in rest:
        from_part, where_part = rest.split("WHERE")
    else:
        from_part = rest
        where_part = None

    table = from_part.strip()

    if select_cols == "*":
        columns = ["*"]
    else:
        columns = [c.strip() for c in select_cols.split(",")]

    where_clause = None
    if where_part:
        ops = ["<=", ">=", "!=", "=", "<", ">"]
        for op in ops:
            if op in where_part:
                col, val = where_part.split(op)
                val = val.strip().strip("'")
                if val.isdigit():
                    val = int(val)
                where_clause = {
                    "column": col.strip(),
                    "operator": op,
                    "value": val
                }
                break

    return {
        "select": columns,
        "from": table,
        "where": where_clause
    }
