from pypika import Query, Table

table_food = Table('Food')

def AddFood(foodName, food_type):
    q = Query.into(table_food).insert(foodName, food_type)
    return q

def GetFood():
    q = Query.from_(table_food)
    return q

def AddModelResQueryString(key, accuracy, f1_score, date_score, final_score):
    query = f"""
        insert into model_evaluate values ('{key}', '{accuracy}' ,'{f1_score}' ,'{date_score}' ,'{final_score}')
    """
    return query

