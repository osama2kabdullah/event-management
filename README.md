# Event Management System

A fully functional Event Management System built with Django and Tailwind CSS, demonstrating advanced Django ORM techniques, optimized queries, and responsive front-end design.

## 📋 Features

### Core Functionality
- **Event Management**: Create, read, update, and delete events with detailed information
- **Participant Management**: Manage event participants with email tracking
- **Category System**: Organize events by categories
- **Search & Filter**: Find events by name, location, category, or date range
- **Organizer Dashboard**: Real-time overview of events and participants

### Advanced Features
- **Optimized Database Queries**: Uses `select_related()` and `prefetch_related()` for efficient data retrieval
- **Aggregate Queries**: Calculate total participants across all events
- **Date Range Filtering**: Filter events by custom date ranges
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS
- **Interactive Dashboard**: Click stats to dynamically filter event views

## 🎯 Project Structure

```
event-management/
├── event_management/          # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── events/                    # Main app
│   ├── models.py             # Data models (Event, Category, Participant)
│   ├── views.py              # View logic with optimized queries
│   ├── forms.py              # Django forms with Tailwind styling
│   ├── urls.py               # App-level URL routing
│   ├── admin.py              # Django admin configuration
│   └── migrations/           # Database migrations
├── templates/                # HTML templates
│   ├── base.html             # Base template with navigation
│   ├── dashboard.html        # Organizer dashboard
│   ├── event_list.html       # Events listing page
│   ├── event_detail.html     # Event details page
│   ├── event_form.html       # Event create/edit form
│   ├── category_list.html    # Categories listing
│   ├── category_form.html    # Category create/edit form
│   ├── participant_list.html # Participants listing
│   ├── participant_form.html # Participant create/edit form
│   ├── search_results.html   # Search results page
│   └── home.html             # Home page
├── static/                   # Static files
│   ├── css/                  # Stylesheets (Tailwind CSS)
│   ├── js/                   # JavaScript files
│   └── images/               # Image assets
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database
├── package.json              # Node.js dependencies
├── tailwind.config.js        # Tailwind CSS configuration
└── postcss.config.js         # PostCSS configuration
```

## 📊 Data Models

### Event
- **name**: Event title
- **description**: Detailed event description
- **date**: Event date
- **time**: Event time
- **location**: Event venue/location
- **category**: Foreign key to Category

### Participant
- **name**: Participant name
- **email**: Participant email
- **events**: Many-to-many relationship with Event

### Category
- **name**: Category name
- **description**: Category description

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+ (for Tailwind CSS)
- pip (Python package manager)
- npm (Node package manager)

### Installation

1. **Clone the repository**
   ```bash
   cd event-management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .\.venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install django
   ```

4. **Install Node dependencies**
   ```bash
   npm install
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Build Tailwind CSS**
   ```bash
   npm run build:tailwind
   # Or for development with watch mode
   npm run watch:tailwind
   ```

7. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Access the application at: `http://127.0.0.1:8000/`

## 🔧 Available Commands

### Django Commands
```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access admin panel
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

### Tailwind CSS Commands
```bash
# Build Tailwind CSS (one-time)
npm run build:tailwind

# Watch for changes (development mode)
npm run watch:tailwind
```

## 📱 Key Features & Usage

### Dashboard
- View overall statistics (total events, upcoming events, past events, total participants)
- Click on stat cards to filter events dynamically
- See today's scheduled events
- Quick overview of event details and participant counts

**Access**: Navigate to `/dashboard/`

### Events Management
- **List Events**: View all events with filtering options
- **Create Event**: Add new events via form
- **View Details**: See full event information and participant list
- **Edit Event**: Update event details
- **Delete Event**: Remove events from the system

**Access**: Navigate to `/events/`

### Participants Management
- **List Participants**: View all registered participants
- **Create Participant**: Register new participants
- **Assign Events**: Link participants to multiple events
- **Edit Participant**: Update participant information
- **Delete Participant**: Remove participants

**Access**: Navigate to `/participants/`

### Categories Management
- **List Categories**: View all event categories
- **Create Category**: Add new categories
- **Edit Category**: Update category details
- **Delete Category**: Remove categories

**Access**: Navigate to `/categories/`

### Search & Filter
- **Search**: Find events by name or location
- **Category Filter**: Filter events by category
- **Date Range**: Filter events by start and end dates
- **Combined Filters**: Use multiple filters simultaneously

**Access**: Use search bar in navigation or visit `/events/`

## 🎨 UI/UX Design

### Tailwind CSS Integration
- Responsive grid layouts (mobile, tablet, desktop)
- Consistent color scheme and typography
- Interactive hover effects and transitions
- Mobile-first design approach
- Accessible form elements with proper focus states

### Navigation
- Top navigation bar with links to all sections
- Search functionality in header
- Breadcrumb-like navigation through detail pages
- "Add New" buttons for creating entities

### Dashboard Features
- Stats grid with key metrics
- Interactive stat cards that filter data
- Today's events highlighted section
- Event cards with participant count and category display

## 🔐 Security Features

- CSRF protection on all forms
- Secure form validation
- SQL injection prevention (via Django ORM)
- Django security middleware enabled
- Input sanitization via form validation

## 📝 Form Validation

All forms include:
- Required field validation
- Email format validation for participant emails
- Date/time validation
- Custom Tailwind CSS styling for form inputs
- Real-time visual feedback on focus/input

## 🧪 Testing the Application

### Test Checklist
1. **Create an Event**: Add a new event with all details
2. **Add Participants**: Create participants and assign to events
3. **Update Data**: Edit existing events and participants
4. **Delete Operations**: Remove events/participants with confirmation
5. **Search**: Test search with various keywords
6. **Filters**: Test category and date range filters
7. **Dashboard**: Verify statistics and interactive filtering
8. **Responsiveness**: Test on mobile, tablet, and desktop viewports

## 📚 Technologies Used

- **Backend**: Django 6.0
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3
- **Styling**: Tailwind CSS 3.4
- **JavaScript**: Vanilla JavaScript
- **Build Tools**: Node.js, npm, PostCSS

## 📄 License

This project is part of an educational assignment.

## 👨‍💻 Author

Created as an Event Management System assignment demonstrating Django ORM and Tailwind CSS expertise.

---

**Last Updated**: December 2025
