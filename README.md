# Django CRM (Customer Relationship Management)

A lightweight **CRM system** built with **Django** and **MySQL**.  
This project allows users to **register, log in, and manage customer records** with full **CRUD (Create, Read, Update, Delete)** functionality.  

---

## ✨ Features

### 🔐 Authentication
- User registration  
- Secure login & logout  

### 📂 Customer Records
- Add new customers  
- View details of individual records  
- Update existing records  
- Delete records  

### 🗄 Database
- Uses **MySQL** as the backend database  

### 🎨 UI/UX
- Responsive **Bootstrap** styling  
- Reusable navigation bar  

---

## ⚙️ Installation

### 📋 Prerequisites
- **Python** 3.10+  
- **Django** 5.2+  
- **MySQL Server**  
- **pymysql** library  

---

### 🚀 Setup Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-crm.git
   cd django-crm
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Linux/Mac
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MySQL Database**  
   Update your `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'firstcrm',
           'USER': 'root',
           'PASSWORD': 'kryouliaris20',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
   Or run `mydb.py` to create the database automatically.

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the app**  
   Open your browser at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

---

## 🎯 Usage
- **Login/Register** to start using the CRM  
- Add, update, delete, and view customer records  
- Access Django Admin Panel at: `/admin/`  

---
