# IronFlex Gym - Management System

A modern, responsive gym management website built with Flask and HTML/CSS. The platform provides a comprehensive digital presence for fitness centers with user authentication, service browsing, and contact management features.

## 🎯 Features

### Pages & Functionality

#### 1. **Home Page** (`/`)
- Eye-catching hero section with call-to-action button
- Feature cards showcasing gym benefits:
  - Modern Equipment
  - Expert Trainers
  - Flexible Timings
  - Nutrition Plans
- Responsive navigation bar with links to all pages
- Professional footer with quick links

#### 2. **About Page** (`/about`)
- Company story and background information
- Mission, Vision, and Core Values sections
- Reasons to choose IronFlex Gym with visual cards
- High-quality images and professional layout
- Call-to-action to join

#### 3. **Services Page** (`/services`)
- 8 comprehensive service cards in grid layout:
  - 💪 Strength Training
  - 🏃 Cardio Fitness
  - 🧘 Yoga & Flexibility
  - 👨‍🏫 Personal Training
  - 🥗 Nutrition Counseling
  - 👥 Group Classes
  - 📊 Progress Tracking
  - 🏊 Swimming Pool
- Detailed descriptions for each service
- Call-to-action button

#### 4. **Gallery Page** (`/gallery`)
- 12-image responsive grid gallery
- Hover effects with zoom animation
- Professional fitness-related images
- Mobile-friendly responsive design
- Smooth transitions and animations

#### 5. **Contact Page** (`/contact`)
- Contact form with validation:
  - Name field (required)
  - Email field (required, validated)
  - Phone field (optional)
  - Subject field (required)
  - Message textarea (required)
- **Client-side validation** with error messages
- Success/error notifications
- Contact information section:
  - Physical location
  - Phone hours
  - Email support details
- Backend form submission handling

#### 6. **Login Page** (`/login`)
- Username/Email input field
- Password input field
- Remember me checkbox
- Forgot Password link
- Link to registration page
- Professional form styling
- Terms & conditions footer

#### 7. **Registration Page** (`/register`)
- Full Name input
- Email Address input
- Username input (3-20 characters)
- Password field with real-time strength indicator
- Confirm Password field
- Terms & Conditions checkbox
- **Advanced password strength visualization** (4-bar indicator)
- Comprehensive form validation:
  - Username length validation
  - Email format validation
  - Password strength requirements (8+ chars, uppercase, lowercase, numbers)
  - Password matching validation
- Link to login page

## 🛠️ Technologies Used

- **Backend**: Python Flask 3.1.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design**: Responsive, Mobile-first approach
- **Features**: Form validation, animations, gradient backgrounds

## 📁 Project Structure

```
gym-management-system/
├── app.py                    # Flask application with all routes
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── static/
│   └── style.css            # Comprehensive CSS styling
└── templates/
    ├── index.html           # Home page
    ├── about.html           # About page
    ├── services.html        # Services page
    ├── gallery.html         # Gallery page
    ├── contact.html         # Contact page with validation
    ├── login.html           # Login page
    ├── register.html        # Registration page
    └── membership.html      # Membership page (existing)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Clone/Download the Repository
```bash
cd gym-management-system
```

### Step 2: Install Dependencies
```bash
pip install flask
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Website
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📋 Routes

| Route | Page | Method |
|-------|------|--------|
| `/` | Home | GET |
| `/about` | About Us | GET |
| `/services` | Services | GET |
| `/gallery` | Gallery | GET |
| `/contact` | Contact | GET, POST |
| `/login` | Login | GET |
| `/register` | Registration | GET |
| `/membership` | Membership | GET |

## 🎨 Design Features

### Visual Design
- **Color Scheme**: Dark theme with rose-red accents (#e11d48)
- **Typography**: Oswald font for modern, bold appearance
- **Layout**: Responsive grid layouts for all pages
- **Animations**: Smooth hover effects, transitions, and transforms

### User Experience
- Sticky navigation bar for easy access
- Consistent card-based design system
- Clear call-to-action buttons throughout
- Intuitive form layouts with validation feedback
- Mobile-responsive design (tested on various screen sizes)

### Form Validation
- **Contact Form**:
  - Real-time validation
  - Email format verification
  - Success/error message display
  - 5-second auto-dismiss success messages

- **Registration Form**:
  - Password strength indicator with visual bars
  - Real-time password validation
  - Username length validation (3-20 characters)
  - Email format validation
  - Password confirmation matching
  - Terms acceptance requirement

## 🔒 Security Notes

- All form inputs are validated on the client-side
- For production, implement server-side validation and database storage
- Add CSRF protection for form submissions
- Implement proper authentication and password hashing (use libraries like `werkzeug.security`)

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: Below 768px

## ✨ Future Enhancements

- [ ] Database integration for user accounts and contact submissions
- [ ] Email notification system for contact form submissions
- [ ] User dashboard with membership management
- [ ] Payment gateway integration
- [ ] Trainer appointment booking system
- [ ] Class scheduling and enrollment
- [ ] Member progress tracking and analytics
- [ ] Social media integration
- [ ] Blog/News section
- [ ] Mobile app version

## 📄 License

This project is available for educational and commercial use.

## 📧 Support

For questions or support, contact: info@ironflex.com

---

**Built with ❤️ for fitness enthusiasts everywhere**
