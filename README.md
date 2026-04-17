# 🛒 Django Shop

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Azure](https://img.shields.io/badge/Azure-Deployed-blue)
![Tests](https://img.shields.io/badge/Tests-29-success)

A full-stack e-commerce web application built with **Django**, **PostgreSQL**, **Azure App Service**, and **Cloudinary**.

🚀 **Live Demo:** https://djangoshopproject-gpdadncxbdc9cgby.switzerlandnorth-01.azurewebsites.net/

---

# 📌 Project Overview

Django Shop is an online marketplace where users can browse products, register accounts, add items to cart, place orders, leave reviews, and manage their profiles.

The project was created for educational and exam purposes.

---

# ✨ Features

## 🌍 Public Area
- Home page
- Product catalog
- Product details page
- Add products to cart
- About page
- Contact page
- User registration
- User login

## 🔐 Private Area
- User profile page
- Edit / delete profile
- Add products to cart
- Checkout / place order
- Order history
- Order details
- Product reviews

## 👨‍💼 Admin Area
- Django admin dashboard
- Manage products
- Update order statuses

## ⚙️ Production Features
- PostgreSQL database
- Cloudinary image uploads
- WhiteNoise static files
- Mailjet email integration
- Secure `.env` configuration
- Azure deployment
- Automated tests

---

# 🛠️ Tech Stack

| Backend | Frontend | Database | Deployment | Services |
|--------|----------|----------|------------|----------|
| Python | HTML5 | PostgreSQL | Azure App Service | Cloudinary |
| Django | CSS3 / SCSS | | Azure PostgreSQL | Mailjet |
| DRF | Bootstrap / JavaScript | | | |

---

# 🧩 Database Models

- User
- Profile
- Product
- Review
- Cart
- CartItem
- Order
- OrderItem

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YIvanov97/Django-Advanced-Exam-21.04.2026.git
cd Shop
```

## 2️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

## 3️⃣ Apply Migrations
```bash
python manage.py migrate
```

## 4️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

## 5️⃣ Run Server
```bash
python manage.py runserver
```
## Demo Accounts

### Admin Account
- Email: admin@admin.com
- Password: admin

### Test User Account
- Email: test@testov.com
- Password: 12test34
