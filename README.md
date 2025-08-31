# CoNexus - Modern Blog Platform

A fully interactive and modern blog website built with Flask, featuring a responsive design, user authentication, admin dashboard, and comprehensive content management system.

## 🚀 Features

### Core Features
- **Home Page**: Welcome section, featured posts, recent posts, categories, and tags
- **Blog Page**: List of all posts with search, filtering, and pagination
- **Single Post Page**: Full post view with comments, social sharing, and related posts
- **About Page**: Personal introduction and mission statement
- **Contact Page**: Contact form with social media links
- **User Authentication**: Registration, login, and role-based access control
- **Admin Dashboard**: Complete content management system

### Advanced Features
- **Dark/Light Mode Toggle**: User preference with persistent storage
- **Newsletter Subscription**: Email collection and management
- **SEO Optimization**: Meta tags, OpenGraph, and structured data
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Image Upload**: Featured image support for blog posts
- **Comment System**: User comments with approval workflow
- **Social Media Integration**: Share buttons and social links
- **Analytics Ready**: Google Analytics integration placeholder

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (easily configurable for MySQL/PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Authentication**: Flask-Login
- **Database ORM**: SQLAlchemy
- **File Upload**: Werkzeug
- **Deployment**: Gunicorn (production)

## 📁 Project Structure

```
conexus/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── blog.html         # Blog listing
│   ├── post.html         # Single post
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   ├── admin/            # Admin templates
│   │   ├── dashboard.html
│   │   ├── posts.html
│   │   └── new_post.html
│   └── errors/           # Error pages
│       ├── 404.html
│       └── 500.html
├── static/               # Static files
│   └── uploads/          # Uploaded images
└── blog.db              # SQLite database (created automatically)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd conexus
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Admin credentials: `admin` / `admin123`

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///blog.db
UPLOAD_FOLDER=static/uploads
MAX_CONTENT_LENGTH=16777216
```

### Database Configuration
The application uses SQLite by default. To use MySQL or PostgreSQL:

1. Update the database URL in `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/bloghub'
   # or
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/bloghub'
   ```

2. Install the appropriate database driver:
   ```bash
   pip install mysqlclient  # for MySQL
   pip install psycopg2-binary  # for PostgreSQL
   ```

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password
- `is_admin`: Admin privileges flag
- `created_at`: Account creation timestamp

### Posts Table
- `id`: Primary key
- `title`: Post title
- `slug`: URL-friendly title
- `content`: Post content (HTML)
- `excerpt`: Post summary
- `featured_image`: Image file path
- `is_published`: Publication status
- `is_featured`: Featured post flag
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `user_id`: Author reference
- `category_id`: Category reference
- `views`: View count

### Categories Table
- `id`: Primary key
- `name`: Category name
- `description`: Category description

### Comments Table
- `id`: Primary key
- `content`: Comment text
- `created_at`: Comment timestamp
- `is_approved`: Approval status
- `user_id`: Commenter reference
- `post_id`: Post reference

### Newsletter Table
- `id`: Primary key
- `email`: Subscriber email
- `subscribed_at`: Subscription timestamp

## 🎨 Customization

### Styling
The application uses Tailwind CSS. To customize the design:

1. Modify the Tailwind configuration in `templates/base.html`
2. Update color schemes and components
3. Add custom CSS in the `<style>` sections

### Adding Features
- **New Routes**: Add to `app.py` in the appropriate section
- **New Templates**: Create in the `templates/` directory
- **New Models**: Add to the database models section in `app.py`

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

#### Using Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

Build and run:
```bash
docker build -t bloghub .
docker run -p 8000:8000 bloghub
```

#### Deployment Platforms

**Heroku**
1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```
2. Deploy using Heroku CLI or GitHub integration

**Render**
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`

**DigitalOcean App Platform**
1. Connect your repository
2. Select Python environment
3. Configure environment variables

## 🔒 Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **CSRF Protection**: Built-in Flask-WTF protection
- **File Upload Security**: Secure filename handling and size limits
- **SQL Injection Protection**: SQLAlchemy ORM protection
- **XSS Protection**: HTML escaping in templates

## 📈 Analytics Integration

To add Google Analytics:

1. Get your tracking ID from Google Analytics
2. Add the tracking code to `templates/base.html`:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_TRACKING_ID');
   </script>
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/bloghub/issues) page
2. Create a new issue with detailed information
3. Contact support at support@bloghub.com

## 🎯 Roadmap

- [ ] Email notifications for comments
- [ ] Advanced search with filters
- [ ] User profiles and avatars
- [ ] Social media login integration
- [ ] RSS feed generation
- [ ] API endpoints for mobile apps
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Backup and restore functionality
- [ ] CDN integration for images

## 🙏 Acknowledgments

- Flask team for the amazing web framework
- Tailwind CSS for the utility-first CSS framework
- Font Awesome for the beautiful icons
- The open-source community for inspiration and tools

---

**Happy Blogging! 🚀**
