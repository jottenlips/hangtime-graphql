from aws_resources.dynamo import table
from aws_resources.dynamo import build_update_expression, build_update_attributes_dictionary

def test_table():
    db = table()
    assert db != None

# def test_build_update_expression():
#     update_exp = build_update_expression(mock_hang)
#     assert update_exp == 'set name=:name'

# def build_update_attributes_dictionary():
#     update_attr = pdate_attributes_dictionary(mock_hang)
#     assert update_attr == {
#         ':name': 'hang name',
#     }

