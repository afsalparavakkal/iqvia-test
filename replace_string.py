"""
Write a function replace_latest_slice() which takes a string query, and changes all
occurrences of latest_slice::<table> to (SELECT * FROM <table> WHERE ds =
'LATEST').
"""


PLACE_HOLDER = 'latest_slice::'
TABLE_SEPERATOR = '::'
SELECT_QUERY_YEMPLATE = "(SELECT * FROM {} WHERE ds = 'LATEST')"

def replace_latest_slice(query):
    if not query:
        raise ValueError

    query_list = query.split()

    final_query = ''

    for item in query_list:

        if item.startswith(PLACE_HOLDER):
            table = item.split(TABLE_SEPERATOR)[1]
            item = SELECT_QUERY_YEMPLATE.format(table)

        final_query += ' ' + item

    return final_query 


expected_result = """SELECT * FROM (SELECT * FROM sale_order WHERE ds = 'LATEST') so INNER JOIN (SELECT * FROM res_partner WHERE ds = 'LATEST') rp ON so.id = rp.id"""

actual_result = replace_latest_slice(query="""SELECT * FROM latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON so.id = rp.id""")
assert actual_result.strip() == expected_result




