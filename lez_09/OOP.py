from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Dict, Any
from enum import Enum
import hashlib
import secrets

class VisibilityLevel(Enum):
    """Enumeration for document visibility levels"""
    PUBLIC = "public"
    PRIVATE = "private" 
    TEAM = "team"
    CONFIDENTIAL = "confidential"

class UserRole(Enum):
    """Enumeration for user roles"""
    ADMINISTRATOR = "administrator"
    USER = "user"
    MANAGER = "manager"

class PermissionProtocol(ABC):
    """Abstract base class defining the permission protocol (duck typing)"""
    
    @abstractmethod
    def can_view(self, document: 'Document') -> bool:
        pass
    
    @abstractmethod
    def can_modify(self, document: 'Document') -> bool:
        pass

class User(PermissionProtocol):
    """
    Base User class demonstrating encapsulation and abstraction.
    
    Attributes
    ----------
    _username : str
        Unique identifier for the user (protected)
    _role : UserRole
        User's role in the system (protected)
    _password_hash : str
        Hashed password (private)
    _is_active : bool
        Whether the user account is active
    
    Examples
    --------
    >>> user = User("alice", UserRole.USER, "password123")
    >>> user.authenticate("password123")
    True
    """
    
    def __init__(self, username: str, role: UserRole, password: str):
        self._username = username
        self._role = role
        self._password_hash = self._hash_password(password)
        self._is_active = True
        self._login_attempts = 0
    
    # =========================================================================
    # PROPERTIES - Controlled access with validation
    # =========================================================================
    
    @property
    def username(self) -> str:
        """Get username (read-only)"""
        return self._username
    
    @property
    def role(self) -> UserRole:
        """Get user role (read-only)"""
        return self._role
    
    @property
    def is_active(self) -> bool:
        """Check if user account is active (read-only)"""
        return self._is_active
    
    @property
    def login_attempts(self) -> int:
        """Get number of failed login attempts (read-only)"""
        return self._login_attempts
    
    # =========================================================================
    # PRIVATE METHODS - Implementation details
    # =========================================================================
    
    def _hash_password(self, password: str) -> str:
        """Hash password with salt for security"""
        salt = secrets.token_hex(16)
        return hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode('utf-8'), 
            salt.encode('utf-8'), 
            100000
        ).hex() + ':' + salt
    
    def _verify_password(self, password: str) -> bool:
        """Verify password against stored hash"""
        try:
            hashed, salt = self._password_hash.split(':')
            new_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt.encode('utf-8'), 
                100000
            ).hex()
            return hashed == new_hash
        except ValueError:
            return False
    
    # =========================================================================
    # PUBLIC METHODS - User interface
    # =========================================================================
    
    def authenticate(self, password: str) -> bool:
        """
        Authenticate user with password.
        
        Returns
        -------
        bool
            True if authentication successful, False otherwise
        """
        if not self._is_active:
            return False
        
        if self._login_attempts >= 5:
            self.deactivate()
            return False
        
        if self._verify_password(password):
            self._login_attempts = 0
            return True
        else:
            self._login_attempts += 1
            return False
    
    def deactivate(self) -> None:
        """Deactivate user account"""
        self._is_active = False
    
    def activate(self) -> None:
        """Activate user account and reset login attempts"""
        self._is_active = True
        self._login_attempts = 0
    
    def change_password(self, old_password: str, new_password: str) -> bool:
        """
        Change user password with validation.
        
        Parameters
        ----------
        old_password : str
            Current password for verification
        new_password : str
            New password to set
            
        Returns
        -------
        bool
            True if password changed successfully, False otherwise
        """
        if not self._verify_password(old_password):
            return False
        
        if len(new_password) < 6:
            return False
        
        self._password_hash = self._hash_password(new_password)
        return True
    
    # =========================================================================
    # PERMISSION PROTOCOL IMPLEMENTATION (Duck Typing)
    # =========================================================================
    
    def can_view(self, document: 'Document') -> bool:
        """Check if user can view a document"""
        if not self._is_active:
            return False
        
        # Administrators can view everything
        if self._role == UserRole.ADMINISTRATOR:
            return True
        
        # Users can view public documents
        if document.visibility == VisibilityLevel.PUBLIC:
            return True
        
        # Users can view their own documents
        if document.owner == self:
            return True
        
        return False
    
    def can_modify(self, document: 'Document') -> bool:
        """Check if user can modify a document"""
        if not self._is_active:
            return False
        
        # Administrators can modify everything
        if self._role == UserRole.ADMINISTRATOR:
            return True
        
        # Users can modify their own documents
        if document.owner == self:
            return True
        
        return False
    
    # =========================================================================
    # SPECIAL METHODS
    # =========================================================================
    
    def __str__(self) -> str:
        return f"User(username='{self._username}', role={self._role.value})"
    
    def __repr__(self) -> str:
        return f"User('{self._username}', {self._role}, '***')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self._username == other._username

class Administrator(User):
    """
    Administrator user with elevated privileges.
    Demonstrates inheritance and method overriding.
    """
    
    def __init__(self, username: str, password: str):
        super().__init__(username, UserRole.ADMINISTRATOR, password)
    
    def can_view(self, document: 'Document') -> bool:
        """Administrators can view all active documents"""
        return self._is_active
    
    def can_modify(self, document: 'Document') -> bool:
        """Administrators can modify all active documents"""
        return self._is_active
    
    def deactivate_user(self, user: User) -> bool:
        """Administrator-only method to deactivate users"""
        if not isinstance(user, User):
            return False
        user.deactivate()
        return True
    
    def activate_user(self, user: User) -> bool:
        """Administrator-only method to activate users"""
        if not isinstance(user, User):
            return False
        user.activate()
        return True

class Document:
    """
    Document class representing a document in the system.
    Demonstrates encapsulation and composition.
    
    Attributes
    ----------
    _id : int
        Unique document identifier
    _title : str
        Document title
    _content : str
        Document content
    _owner : User
        User who owns the document
    _visibility : VisibilityLevel
        Document visibility setting
    
    Examples
    --------
    >>> user = User("alice", UserRole.USER, "pass")
    >>> doc = Document(1, "My Doc", "Content", user, VisibilityLevel.PRIVATE)
    >>> doc.title
    'My Doc'
    """
    
    # Class attribute - shared by all documents
    next_id = 1
    
    def __init__(self, title: str, content: str, owner: User, 
                 visibility: VisibilityLevel = VisibilityLevel.PRIVATE):
        self._id = Document.next_id
        self._title = title
        self._content = content
        self._owner = owner
        self._visibility = visibility
        
        # Increment class attribute
        Document.next_id += 1
    
    # =========================================================================
    # PROPERTIES - Controlled access with validation
    # =========================================================================
    
    @property
    def id(self) -> int:
        """Get document ID (read-only)"""
        return self._id
    
    @property
    def title(self) -> str:
        """Get document title (read-only)"""
        return self._title
    
    @property
    def content(self) -> str:
        """Get document content (read-only)"""
        return self._content
    
    @property
    def owner(self) -> User:
        """Get document owner (read-only)"""
        return self._owner
    
    @property
    def visibility(self) -> VisibilityLevel:
        """Get document visibility"""
        return self._visibility
    
    @visibility.setter
    def visibility(self, value: VisibilityLevel) -> None:
        """Set document visibility with type validation"""
        if not isinstance(value, VisibilityLevel):
            raise ValueError("Visibility must be a VisibilityLevel enum")
        self._visibility = value
    
    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================
    
    def update_content(self, new_content: str, user: User) -> bool:
        """
        Update document content if user has permission.
        
        Parameters
        ----------
        new_content : str
            New content for the document
        user : User
            User attempting the update
            
        Returns
        -------
        bool
            True if update successful, False otherwise
        """
        if user.can_modify(self):
            self._content = new_content
            return True
        return False
    
    def change_visibility(self, new_visibility: VisibilityLevel, user: User) -> bool:
        """
        Change document visibility if user has permission.
        
        Parameters
        ----------
        new_visibility : VisibilityLevel
            New visibility setting
        user : User
            User attempting the change
            
        Returns
        -------
        bool
            True if change successful, False otherwise
        """
        if user.can_modify(self):
            self.visibility = new_visibility
            return True
        return False
    
    def get_summary(self) -> str:
        """Get document summary"""
        return f"Document {self._id}: '{self._title}' ({self._visibility.value})"
    
    # =========================================================================
    # SPECIAL METHODS
    # =========================================================================
    
    def __str__(self) -> str:
        return f"Document(id={self._id}, title='{self._title}', visibility={self._visibility.value})"
    
    def __repr__(self) -> str:
        return f"Document('{self._title}', '{self._content}', {self._owner}, {self._visibility})"

class DocumentManager:
    """
    Document management system that coordinates users and documents.
    Demonstrates composition and the facade pattern.
    
    Attributes
    ----------
    _users : List[User]
        List of registered users
    _documents : List[Document]
        List of documents in the system
    _current_user : Optional[User]
        Currently logged-in user
    
    Examples
    --------
    >>> manager = DocumentManager()
    >>> admin = Administrator("admin", "admin123")
    >>> manager.add_user(admin)
    >>> manager.login("admin", "admin123")
    True
    """
    
    def __init__(self):
        self._users: List[User] = []
        self._documents: List[Document] = []
        self._current_user: Optional[User] = None
    
    # =========================================================================
    # USER MANAGEMENT
    # =========================================================================
    
    def add_user(self, user: User) -> bool:
        """
        Add a user to the system.
        
        Parameters
        ----------
        user : User
            User to add
            
        Returns
        -------
        bool
            True if user added successfully, False otherwise
        """
        if not isinstance(user, User):
            return False
        
        # Check if username already exists
        if any(u.username == user.username for u in self._users):
            return False
        
        self._users.append(user)
        return True
    
    def find_user(self, username: str) -> Optional[User]:
        """
        Find user by username.
        
        Parameters
        ----------
        username : str
            Username to search for
            
        Returns
        -------
        User or None
            User object if found, None otherwise
        """
        return next((u for u in self._users if u.username == username), None)
    
    def login(self, username: str, password: str) -> Tuple[Optional[User], bool]:
        """
        Authenticate and log in a user.
        
        Parameters
        ----------
        username : str
            Username to authenticate
        password : str
            Password for authentication
            
        Returns
        -------
        tuple (User or None, bool)
            User object (or None) and authentication status
            
        Notes
        -----
        Return scenarios:
        - (User, True): Successful authentication
        - (User, False): User exists but wrong password  
        - (None, False): User doesn't exist
        """
        user = self.find_user(username)
        if user is None:
            return None, False
        
        authenticated = user.authenticate(password)
        if authenticated:
            self._current_user = user
        
        return user, authenticated
    
    def logout(self) -> None:
        """Log out current user"""
        self._current_user = None
    
    @property
    def current_user(self) -> Optional[User]:
        """Get current logged-in user (read-only)"""
        return self._current_user
    
    # =========================================================================
    # DOCUMENT MANAGEMENT
    # =========================================================================
    
    def add_document(self, title: str, content: str, 
                    visibility: VisibilityLevel = VisibilityLevel.PRIVATE) -> Optional[Document]:
        """
        Create and add a new document.
        
        Parameters
        ----------
        title : str
            Document title
        content : str
            Document content
        visibility : VisibilityLevel
            Document visibility setting
            
        Returns
        -------
        Document or None
            Created document if successful, None otherwise
        """
        if self._current_user is None:
            return None
        
        # Check if title already exists
        if any(doc.title == title for doc in self._documents):
            return None
        
        document = Document(title, content, self._current_user, visibility)
        self._documents.append(document)
        return document
    
    def find_document(self, title: str) -> Optional[Document]:
        """
        Find document by exact title match.
        
        Parameters
        ----------
        title : str
            Document title to search for
            
        Returns
        -------
        Document or None
            Document if found, None otherwise
        """
        return next((doc for doc in self._documents if doc.title == title), None)
    
    def retrieve_document(self, title: str) -> Optional[Document]:
        """
        Retrieve a document if current user has permission to view it.
        
        Parameters
        ----------
        title : str
            Document title to retrieve
            
        Returns
        -------
        Document or None
            Document if found and user has permission, None otherwise
            
        Notes
        -----
        This method demonstrates duck typing - it works with any User
        that implements the PermissionProtocol (can_view method)
        """
        if self._current_user is None:
            return None
        
        document = self.find_document(title)
        if document is None:
            return None
        
        # Duck typing in action: we only care that current_user has can_view method
        if self._current_user.can_view(document):
            return document
        
        return None
    
    def change_document_visibility(self, title: str, new_visibility: VisibilityLevel) -> bool:
        """
        Change document visibility if current user has permission.
        
        Parameters
        ----------
        title : str
            Document title
        new_visibility : VisibilityLevel
            New visibility setting
            
        Returns
        -------
        bool
            True if visibility changed successfully, False otherwise
        """
        if self._current_user is None:
            return False
        
        document = self.find_document(title)
        if document is None:
            return False
        
        # Use the document's method which checks permissions
        return document.change_visibility(new_visibility, self._current_user)
    
    def get_accessible_documents(self) -> List[Document]:
        """
        Get all documents accessible to current user.
        
        Returns
        -------
        List[Document]
            List of documents the user can view
        """
        if self._current_user is None:
            return []
        
        return [doc for doc in self._documents if self._current_user.can_view(doc)]
    
    # =========================================================================
    # ADMINISTRATIVE METHODS
    # =========================================================================
    
    def get_system_stats(self) -> Dict[str, Any]:
        """
        Get system statistics (admin only).
        
        Returns
        -------
        dict
            System statistics
        """
        if self._current_user is None or self._current_user.role != UserRole.ADMINISTRATOR:
            return {}
        
        return {
            "total_users": len(self._users),
            "total_documents": len(self._documents),
            "active_users": sum(1 for u in self._users if u.is_active),
            "visibility_breakdown": {
                visibility.value: sum(1 for d in self._documents if d.visibility == visibility)
                for visibility in VisibilityLevel
            }
        }
    
    def list_all_documents(self) -> List[Document]:
        """
        List all documents (admin only).
        
        Returns
        -------
        List[Document]
            All documents in the system
        """
        if self._current_user is None or self._current_user.role != UserRole.ADMINISTRATOR:
            return []
        
        return self._documents.copy()

# =============================================================================
# DEMONSTRATION AND TESTING
# =============================================================================

def demonstrate_oop_system():
    """Demonstrate the OOP system in action"""
    print("=" * 70)
    print("OBJECT-ORIENTED DOCUMENT MANAGEMENT SYSTEM DEMONSTRATION")
    print("=" * 70)
    
    # Create the system
    manager = DocumentManager()
    
    # Create users
    admin = Administrator("admin", "admin123")
    alice = User("alice", UserRole.USER, "alice123")
    bob = User("bob", UserRole.USER, "bob123")
    
    # Add users to system
    manager.add_user(admin)
    manager.add_user(alice)
    manager.add_user(bob)
    
    print("1. USER AUTHENTICATION")
    print("-" * 40)
    
    # Test login
    user, status = manager.login("alice", "alice123")
    print(f"Alice login: {'SUCCESS' if status else 'FAILED'}")
    
    if status:
        # Alice creates documents
        doc1 = manager.add_document("Alice Private Doc", "Private content", VisibilityLevel.PRIVATE)
        doc2 = manager.add_document("Alice Public Doc", "Public content", VisibilityLevel.PUBLIC)
        print(f"Alice created: {doc1.title}, {doc2.title}")
    
    manager.logout()
    
    # Admin login
    user, status = manager.login("admin", "admin123")
    print(f"Admin login: {'SUCCESS' if status else 'FAILED'}")
    
    # Admin creates documents
    doc3 = manager.add_document("Admin Confidential", "Confidential content", VisibilityLevel.CONFIDENTIAL)
    print(f"Admin created: {doc3.title}")
    
    print("\n2. DOCUMENT ACCESS CONTROL")
    print("-" * 40)
    
    # Test document retrieval with different users
    manager.logout()
    manager.login("bob", "bob123")
    
    # Bob tries to access various documents
    documents_to_try = ["Alice Private Doc", "Alice Public Doc", "Admin Confidential"]
    
    for doc_title in documents_to_try:
        doc = manager.retrieve_document(doc_title)
        status = "ACCESS GRANTED" if doc else "ACCESS DENIED"
        print(f"Bob accessing '{doc_title}': {status}")
    
    print("\n3. VISIBILITY MANAGEMENT")
    print("-" * 40)
    
    # Alice changes her document visibility
    manager.logout()
    manager.login("alice", "alice123")
    
    success = manager.change_document_visibility("Alice Private Doc", VisibilityLevel.PUBLIC)
    print(f"Alice changing her private doc to public: {'SUCCESS' if success else 'FAILED'}")
    
    # Bob tries again (should work now)
    manager.logout()
    manager.login("bob", "bob123")
    doc = manager.retrieve_document("Alice Private Doc")
    print(f"Bob accessing formerly private doc: {'SUCCESS' if doc else 'FAILED'}")
    
    print("\n4. ADMINISTRATOR PRIVILEGES")
    print("-" * 40)
    
    manager.logout()
    manager.login("admin", "admin123")
    
    # Admin can see all documents
    accessible = manager.get_accessible_documents()
    print(f"Admin can access {len(accessible)} documents")
    
    stats = manager.get_system_stats()
    print(f"System stats: {stats}")
    
    print("\n5. DUCK TYPING DEMONSTRATION")
    print("-" * 40)
    
    # Create a custom user class that implements PermissionProtocol
    class GuestUser:
        """A guest user that implements the permission protocol"""
        def can_view(self, document):
            return document.visibility == VisibilityLevel.PUBLIC
        
        def can_modify(self, document):
            return False
    
    # This works due to duck typing - GuestUser isn't a User subclass
    # but it implements the required methods
    guest = GuestUser()
    public_doc = manager.find_document("Alice Public Doc")
    if public_doc:
        can_view = guest.can_view(public_doc)
        print(f"Guest user can view public doc: {can_view}")

if __name__ == "__main__":
    demonstrate_oop_system()