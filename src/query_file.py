
def generate_query(filters,size,offset,table_name):
    query= f"SELECT * FROM {table_name}"
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += f" LIMIT {size} OFFSET {offset}"
    return query
    
