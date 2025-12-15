from parser import parse_query
from engine import load_csv, execute_query

def main():
    print("Simple SQL Engine")
    print("Type 'exit' to quit")

    cache = {}

    while True:
        query = input("sql> ")

        if query.lower() in ("exit", "quit"):
            break

        try:
            parsed = parse_query(query)
            table = parsed["from"]

            if table not in cache:
                cache[table] = load_csv(f"data/{table}.csv")

            result = execute_query(parsed, cache[table])
            print(result)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
