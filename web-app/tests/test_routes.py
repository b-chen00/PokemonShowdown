def test_login_page(flask_app):
    url='/login'
    response = flask_app.get(url)
    assert response.status_code == 200

def test_register_page(flask_app):
    url='/register'
    response = flask_app.get(url)
    assert response.status_code == 200

# def test_login(app_with_data):
#     url='/'
#     response = app_with_data.get(url, query_string={'username': 'test', 'password':'test'}, follow_redirects=True)
#     assert response.status_code == 200
#     assert response.request.path=='/home'
#
# def test_history_page(app_with_data):
#     url='/history'
#     response = app_with_data.get(url)
#     assert response.status_code == 200
#
# def test_advise_page(app_with_database):
#     url='/advice'
#     response = app_with_database.get(url)
#     assert response.request.path == '/advice'
#     assert response.status_code == 200
#
# def test_poem_page(app_with_database):
#     url='/poem'
#     response = app_with_database.get(url)
#     assert response.request.path == '/poem'
#     assert response.status_code == 200
#
# def test_joke_page(app_with_database):
#     url='/joke'
#     response = app_with_database.get(url)
#     assert response.request.path == '/joke'
#     assert response.status_code == 200
#
# def test_weekly_page(app_with_database):
#     url='/historyWeekly'
#     response = app_with_database.get(url)
#     assert response.request.path == '/historyWeekly'
#     assert response.status_code == 200
#
# def test_logout(app_with_data):
#     url='/logout'
#     response = app_with_data.get(url, follow_redirects=True)
#     assert response.status_code == 200
#     assert response.request.path == '/'
#     response = app_with_data.get('/register')
#     assert response.status_code == 200
#     assert response.request.path == '/register'
#
# def test_register_page(app_with_database):
#     url='/register'
#     response = app_with_database.get(url)
#     assert response.request.path == '/register'
#     assert response.status_code == 200
#
# def test_register(app_with_database):
#     url='/register'
#     response = app_with_database.post(url, data={'username': 'Santa Claus', 'firstName': 'Santa', 'lastName': 'Claus', 'password':'Christmas'},follow_redirects=True)
#     assert response.status_code == 200
#     assert response.request.path=='/'
#     response = app_with_database.get(response.request.path, query_string={'username': 'Santa Claus', 'password': 'Christmas'}, follow_redirects = True)
#     assert response.status_code == 200
#     assert response.request.path == '/home'
