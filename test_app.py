# import json

# def test_api_get_dogs(api):
#     res = api.get('/api/dogs')
#     assert res.json == {'dogs': [{'id': 1, 'name': 'Mochi'}, {'id': 2, 'name': 'Masha'}]}

# def test_api_get_dog(api):
#     res = api.get('/api/dogs/2')
#     assert res.json['dog']['name'] == 'Masha'

# def test_api_post_dogs(api):
#     mock_data = json.dumps({'name': 'Molly'})
#     mock_headers = {'Content-Type': 'application/json'}
#     res = api.post('/api/dogs', data=mock_data, headers=mock_headers)
#     assert res.json['dog']['id'] == 3

# def test_api_not_found(api):
#     res = api.get('/bob')
#     assert res.status == '404 NOT FOUND'
#     assert 'Oops!' in res.json['message']
