# create_database.py
import sqlite3
from werkzeug.security import generate_password_hash

def create_database():
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    
    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(80) UNIQUE NOT NULL,
            email VARCHAR(120) UNIQUE NOT NULL,
            password_hash VARCHAR(120) NOT NULL,
            is_admin BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) UNIQUE NOT NULL,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tag (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) UNIQUE NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS post (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200) NOT NULL,
            slug VARCHAR(200) UNIQUE NOT NULL,
            content TEXT NOT NULL,
            excerpt TEXT,
            featured_image VARCHAR(200),
            is_published BOOLEAN DEFAULT 1,
            is_featured BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER NOT NULL,
            category_id INTEGER,
            views INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (category_id) REFERENCES category (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            is_approved BOOLEAN DEFAULT 0,
            user_id INTEGER NOT NULL,
            post_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id),
            FOREIGN KEY (post_id) REFERENCES post (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS newsletter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(120) UNIQUE NOT NULL,
            subscribed_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS post_tags (
            post_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            PRIMARY KEY (post_id, tag_id),
            FOREIGN KEY (post_id) REFERENCES post (id),
            FOREIGN KEY (tag_id) REFERENCES tag (id)
        )
    ''')
    
    # Create indexes for better performance
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_post_user_id ON post(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_post_category_id ON post(category_id)",
        "CREATE INDEX IF NOT EXISTS idx_post_slug ON post(slug)",
        "CREATE INDEX IF NOT EXISTS idx_post_published ON post(is_published)",
        "CREATE INDEX IF NOT EXISTS idx_post_featured ON post(is_featured)",
        "CREATE INDEX IF NOT EXISTS idx_post_created_at ON post(created_at)",
        "CREATE INDEX IF NOT EXISTS idx_comment_post_id ON comment(post_id)",
        "CREATE INDEX IF NOT EXISTS idx_comment_user_id ON comment(user_id)",
        "CREATE INDEX IF NOT EXISTS idx_comment_approved ON comment(is_approved)",
        "CREATE INDEX IF NOT EXISTS idx_post_tags_post_id ON post_tags(post_id)",
        "CREATE INDEX IF NOT EXISTS idx_post_tags_tag_id ON post_tags(tag_id)"
    ]
    
    for index in indexes:
        cursor.execute(index)
    
    # Insert default admin user
    admin_password_hash = generate_password_hash('admin123')
    cursor.execute('''
        INSERT OR IGNORE INTO user (username, email, password_hash, is_admin) 
        VALUES (?, ?, ?, ?)
    ''', ('admin', 'admin@blog.com', admin_password_hash, True))
    
    # Insert default categories
    categories = [
        ('Technology', 'Tech-related posts'),
        ('Lifestyle', 'Lifestyle and personal posts'),
        ('Travel', 'Travel experiences and tips'),
        ('Food', 'Food and cooking posts'),
        ('Business', 'Business and entrepreneurship posts')
    ]
    
    for category in categories:
        cursor.execute('''
            INSERT OR IGNORE INTO category (name, description) 
            VALUES (?, ?)
        ''', category)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database 'blog.db' created successfully!")
    print("Default admin user: admin / admin123")

if __name__ == "__main__":
    create_database()
