_jwt_token:str|None=None
def get_auth_headers():
    return {'Authorization': f'Bearer {_jwt_token}'}
def set_session_token(token:str):
    global _jwt_token
    _jwt_token=token
