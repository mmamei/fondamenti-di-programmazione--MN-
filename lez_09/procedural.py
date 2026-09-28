print("=== DOCUMENT MANAGEMENT SYSTEM ===")
print("=== PROCEDURAL APPROACH ===\n")

# Global data structures - this becomes messy quickly!
documents = [
    {"id": 1, "title": "Company Strategy", "content": "Secret business plans...", "owner": "admin", "visibility": "confidential"},
    {"id": 2, "title": "Project Report", "content": "Q1 project results...", "owner": "alice", "visibility": "team"},
    {"id": 3, "title": "Personal Notes", "content": "My private thoughts...", "owner": "alice", "visibility": "private"},
    {"id": 4, "title": "Public Info", "content": "Company public information...", "owner": "admin", "visibility": "public"}
]

users = [
    {"username": "admin", "role": "administrator", "department": "management"},
    {"username": "alice", "role": "user", "department": "engineering"},
    {"username": "bob", "role": "user", "department": "marketing"}
]

# Helper functions that work on global data
def find_user(username):
    """Find user by username"""
    for user in users:
        if user["username"] == username:
            return user
    return None


def find_document(doc_id):
    """Find document by ID"""
    for doc in documents:
        if doc["id"] == doc_id:
            return doc
    return None

def can_user_view_document(username, doc_id):
    """Check if user can view a specific document"""
    user = find_user(username)
    document = find_document(doc_id)
    
    if not user or not document:
        return False
    
    # Complex permission logic mixed with data access
    if user["role"] == "administrator":
        return True
    
    if document["visibility"] == "public":
        return True
    
    if document["owner"] == username:
        return True
    
    if document["visibility"] == "team" and user["department"] == "engineering":
        return True
    
    return False

def get_user_documents(username):
    """Get all documents a user can access"""
    user_documents = []
    for doc in documents:
        if can_user_view_document(username, doc["id"]):
            user_documents.append(doc)
    return user_documents

# Test the procedural system
print("Testing procedural document access:")
print("----------------------------------")

# Test different user scenarios
test_cases = [
    ("admin", 1, "Admin accessing confidential doc"),
    ("alice", 2, "Owner accessing their own doc"),
    ("alice", 1, "Regular user accessing confidential doc"),
    ("bob", 2, "Different department accessing team doc"),
    ("alice", 4, "Any user accessing public doc")
]

for username, doc_id, description in test_cases:
    can_view = can_user_view_document(username, doc_id)
    document = find_document(doc_id)
    print(f"{description}: {can_view}")
    if can_view:
        print(f"  Document: {document['title']}")

print("\nAlice's accessible documents:")
alice_docs = get_user_documents("alice")
for doc in alice_docs:
    print(f"  - {doc['title']} (Owner: {doc['owner']})")