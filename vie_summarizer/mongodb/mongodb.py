from json import dumps

def get_time_interval_query(key: str, start_time: str, end_time: str):
    # RocketChat API sucks. Search for "Query and fields" in https://developer.rocket.chat/apidocs/query-parameters
    # Look at the example for _updatedAt
    query = {
        key: {
            "$gte": {
                "$date": start_time,
            },
            "$lt": {
                "$date": end_time,
            },
        }
    }
    return dumps(query)

def sanity_check():
    # query = {
    #     "ts": {
    #         "$ne": "",
    #         # "$gte": 'ISODate(2024-12-20T00:50:40.637Z)',
    #     }
    # }

    # return dumps(query)

    return '{"ts": {"$gte": "ISODate("2024-12-20T00:50:40.637Z"}}'
    # return '{"ts": {"$ne": ""}}'