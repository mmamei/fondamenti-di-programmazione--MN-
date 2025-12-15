# List of users, a simple list of dict with username, role and password as key

users = [
    {"username": "admin", "role": "administrator", "password": "admin"},
    {"username": "alice", "role": "user", "password": "alice"},
    {"username": "bob", "role": "user", "password": "bob"}
]

documents = [
    {"id": 1, "title": "Company Strategy", "content": "Secret business plans...", "owner": "admin", "visibility": "private"},
    {"id": 2, "title": "Project Report", "content": "Q1 project results...", "owner": "alice", "visibility": "private"},
    {"id": 3, "title": "Personal Notes", "content": "My private thoughts...", "owner": "alice", "visibility": "private"},
    {"id": 4, "title": "Public Info", "content": "Company public information...", "owner": "admin", "visibility": "public"}
]

def user_login(username, prompted_password):
    """
    Authenticate a user by username and password.
    
    Parameters
    ----------
    username : str
        The username to authenticate
    prompted_password : str
        The password provided by the user during login attempt
    
    Returns
    -------
    user_dict : dict or None
        User dictionary if username exists, None otherwise
    authenticated : bool
        True if authentication successful, False otherwise
    
    Notes
    -----
    Return scenarios:
    - (user_dict, True): Successful authentication
    - (user_dict, False): User exists but wrong password  
    - (None, False): User doesn't exist
    """
    for user in users:
        if user['username'] == username:
            if user['password'] == prompted_password:
                return user, True
            else:
                return user, False
    return None, False


def retrive_document(document_title, connected_user):
    """
    Retrieve a document by title if the user has permission to view it.
    
    Parameters
    ----------
    document_title : str
        The exact title of the document to retrieve
    connected_user : dict
        User dictionary containing 'role' and 'username' keys
    
    Returns
    -------
    document : dict or None
        Document dictionary if found and user has permission, None otherwise
    
    Notes
    -----
    Permission hierarchy:
    1. Administrators: access to all documents
    2. Document owners: access to their own documents regardless of visibility
    3. All users: access to public documents
    4. Otherwise: access denied
    """
    for doc in documents:
        if doc['title'] == document_title:
            break
    else:
        return None

    # check if user is authorized to see the document before returning it
    if connected_user['role'] == 'administrator' or doc['visibility'] == 'public':
        return doc
    if doc['owner'] == connected_user['username']:
        return doc
    return None


def change_document_visibility(document_title, connected_user, new_visibility):
    """
    Change the visibility of a document if the user has permission.
    
    Parameters
    ----------
    document_title : str
        The exact title of the document to modify
    connected_user : dict
        User dictionary containing 'role' and 'username' keys
    new_visibility : str
        The new visibility setting for the document
    
    Returns
    -------
    success : bool
        True if visibility was successfully changed, False otherwise
    
    Notes
    -----
    Permission rules:
    - Document owners can always change visibility of their documents
    - Administrators can change visibility of any document
    - Other users cannot change document visibility
    """
    for doc in documents:
        if doc['title'] == document_title:
            break
    else:
        return False
    
    # check if user is authorized to see the document before returning it
    has_right = False
    if connected_user['role'] == 'administrator' or doc['visibility'] == 'public':
        has_right = True
    if doc['owner'] == connected_user['username']:
        has_right = True

    if not has_right:
        return False

    for doc in documents:
        if doc['title'] == document_title:
            doc['visibility'] = new_visibility
            return True

user, success = user_login('bob', 'bob')

print(f"Login attempt for 'bob' with correct password: {success}, User: {user}")

doc = retrive_document("Public Insfo", user)
print(f"Document retrieval attempt for 'Public Info' by 'bob': {doc}")