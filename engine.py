import csv


def load_csv(file_path):
    try:
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        raise Exception("CSV file not found")


def apply_where(rows, where):
    if not where:
        return rows

    col = where["column"]
    op = where["operator"]
    value = where["value"]

    if not rows:
        return []

    if col not in rows[0]:
        raise Exception(f"Column '{col}' does not exist")

    result = []

    for row in rows:
        cell = row[col]

        # Convert to int if needed
        if isinstance(value, int):
            try:
                cell = int(cell)
            except ValueError:
                raise Exception(f"Column '{col}' is not numeric")

        if op == "=" and cell == value:
            result.append(row)
        elif op == "!=" and cell != value:
            result.append(row)
        elif op == ">" and cell > value:
            result.append(row)
        elif op == "<" and cell < value:
            result.append(row)
        elif op == ">=" and cell >= value:
            result.append(row)
        elif op == "<=" and cell <= value:
            result.append(row)

    return result


def apply_select(rows, columns):
    if columns == ["*"]:
        return rows

    if not rows:
        return []

    for col in columns:
        if col not in rows[0]:
            raise Exception(f"Column '{col}' does not exist")

    result = []
    for row in rows:
        new_row = {}
        for col in columns:
            new_row[col] = row[col]
        result.append(new_row)

    return result


def apply_count(rows, columns):
    if not columns[0].startswith("COUNT"):
        return None

    inside = columns[0][6:-1]

    if inside == "*":
        return len(rows)

    if rows and inside not in rows[0]:
        raise Exception(f"Column '{inside}' does not exist")

    return sum(1 for r in rows if r.get(inside))


def execute_query(parsed, data):
    rows = apply_where(data, parsed["where"])

    count_result = apply_count(rows, parsed["select"])
    if count_result is not None:
        return count_result

    return apply_select(rows, parsed["select"])
