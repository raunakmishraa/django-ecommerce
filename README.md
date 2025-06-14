<p align="center"><h1 align="center">DJANGO-ECOMMERCE</h1></p>
<p align="center">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/raunakmishraa/django-ecommerce?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/raunakmishraa/django-ecommerce?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/raunakmishraa/django-ecommerce?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/raunakmishraa/django-ecommerce?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

MyShop is a foundational e-commerce web application built with Django, designed to provide a seamless online shopping experience. This project currently implements core functionalities including user authentication, profile management, static content pages (like legal policies and "About Us"), and basic product listing and detail views. It is set up with a clean, responsive user interface using Tailwind CSS.

---

## 👾 Features

### 1. User Authentication & Management

* **User Registration (Sign Up):** Users can create new accounts.

* **User Login:** Registered users can log in to their accounts.

* **User Logout:** Authenticated users can log out.

* **Custom User Model:** Extends Django's `AbstractUser` to include `phone_number` and `address` fields, providing more detailed user profiles.

* **User Profile Page:** Authenticated users have a dedicated profile page displaying their username, email, first name, last name, phone number, and address.

* **Edit Profile:** Users can update their `username`, `email`, `first_name`, `last_name`, `phone_number`, and `address` from a dedicated edit page.

* **Change Password:** A separate, secure page allows authenticated users to change their password.

* **Message Alerts:** Displays success/error messages for login, signup, profile edits, and password changes.

### 2. Static Pages

* **Home Page (`index.html`):** Features a hero section, a dynamically loaded "featured products" section (with placeholder data and links to product details), and a newsletter signup.

* **About Us Page (`about_us.html`):** Provides information about the store's mission and offerings.

* **Terms of Service Page (`terms_of_service.html`):** Outlines the terms and conditions for using the website.

* **Privacy Policy Page (`privacy_policy.html`):** Details how user data is collected and used.

* **Shipping Information Page (`shipping_information.html`):** Provides details about shipping policies.

* **Refund Policy Page (`refund_policy.html`):** Explains the refund and return guidelines.

* **Consistent Header & Footer:** All pages include a unified navigation header and a detailed footer with quick links. The header adapts based on user authentication status (login/signup buttons vs. profile/cart buttons).

### 3. Product Catalog

* **Product List Page (`product_list.html`):** Displays a grid of products with basic information (name, price, image, short description) and links to individual product detail pages.

* **Product Detail Page (`product_detail.html`):** Shows comprehensive information for a single product, including a larger image, full description, price, and key features/specifications.

* **Product Model (`Product`):** Defines product attributes such as name, description, price, stock, image, and a foreign key to `Category`.

* **Category Model (`Category`):** Allows for organizing products into different categories.

### 4. Admin Interface

* **Django Admin Integration:** `CustomUser`, `Category`, and `Product` models are registered with the Django admin, allowing for easy management of users, product categories, and products directly from the admin panel.

---

## 📁 Project Structure

```sh
└── django-ecommerce/
    ├── db.sqlite3
    ├── frontend
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    └── online_Store
        ├── __init__.py
        ├── __pycache__
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```


### 📂 Project Index

<details open>
	<summary><b><code>DJANGO-ECOMMERCE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/manage.py'>manage.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/db.sqlite3'>db.sqlite3</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- online_Store Submodule -->
		<summary><b>online_Store</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/online_Store/settings.py'>settings.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/online_Store/urls.py'>urls.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/online_Store/asgi.py'>asgi.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/online_Store/wsgi.py'>wsgi.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- frontend Submodule -->
		<summary><b>frontend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/tests.py'>tests.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/forms.py'>forms.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/views.py'>views.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/apps.py'>apps.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/urls.py'>urls.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/admin.py'>admin.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			<tr>
				<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/models.py'>models.py</a></b></td>
<!-- 				<td><code>❯ REPLACE-ME</code></td> -->
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/footer.html'>footer.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/edit_profile.html'>edit_profile.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/about_us.html'>about_us.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/privacy_policy.html'>privacy_policy.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/product_list.html'>product_list.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/terms_of_service.html'>terms_of_service.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/shipping_information.html'>shipping_information.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/password_change.html'>password_change.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/login.html'>login.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/refund_policy.html'>refund_policy.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/index.html'>index.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/profile_page.html'>profile_page.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/signup.html'>signup.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/header.html'>header.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/homepage.html'>homepage.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/contact.html'>contact.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/templates/product_detail.html'>product_detail.html</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/raunakmishraa/django-ecommerce/blob/master/frontend/migrations/0001_initial.py'>0001_initial.py</a></b></td>
<!-- 						<td><code>❯ REPLACE-ME</code></td> -->
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with django-ecommerce, ensure your runtime environment meets the following requirements:

- **Programming Language:** HTML


### ⚙️ Installation

Install django-ecommerce using one of the following methods:

**Build from source:**

1. Clone the django-ecommerce repository:
```sh
❯ git clone https://github.com/raunakmishraa/django-ecommerce/
```

2. Navigate to the project directory:
```sh
❯ cd django-ecommerce
```

3. Install the project dependencies:

echo 'pip install Django Pillow'


### 🤖 Usage
Run django-ecommerce using the following command:
echo 'python manage.py runserver'

### 🧪 Testing
Run the test suite using the following command:
echo 'python manage.py test'

---
## 📌 Project Roadmap

# MyShop E-commerce Application Roadmap

This roadmap outlines the planned development phases for the MyShop E-commerce application, building upon the existing foundational features to create a fully functional and robust online shopping platform.

---

## Phase 1: Core Foundation (Current State)

This phase covers the features already implemented in the project.

* **User Authentication & Management:**
    * [x] User Registration, Login, Logout.
    * [x] Custom User Model with phone number and address.
    * [x] User Profile page with view and edit functionalities.
    * [x] Secure Change Password feature.
    * [x] System message alerts for user actions.

* **Static Pages:**
    * [x] Home Page (Hero, Featured Products preview, Newsletter Signup).
    * [x] "About Us", "Terms of Service", "Privacy Policy", "Shipping Information", "Refund Policy" pages.
    * [x] Consistent header and footer across all pages with responsive navigation.

* **Product Catalog (Basic):**
    * [x] Product List page displaying placeholder products.
    * [x] Product Detail page for individual product information.
    * [x] Django Models for `Product` and `Category`.

* **Admin Interface:**
    * [x] Django Admin integration for `CustomUser`, `Category`, and `Product` models.

---

## Phase 2: E-commerce Core Functionality

Focus on implementing the essential features required for a transactional e-commerce store.

* **Shopping Cart:**
    * [ ] Add products to cart.
    * [ ] View cart contents (quantities, subtotals).
    * [ ] Update product quantities in the cart.
    * [ ] Remove items from the cart.
    * [ ] Persist cart data (e.g., using sessions or database for logged-in users).

* **Order Management:**
    * [ ] Checkout process (collecting shipping/billing info).
    * [ ] Create and store order details (products, quantities, total, status).
    * [ ] User's order history page to view past purchases.

---

## Phase 3: Enhanced Product & User Experience

Adding features to improve usability, discoverability, and engagement.

* **Product Search & Filtering:**
    * [ ] Implement a search bar for products.
    * [ ] Add filters by category, price range, etc., on the product list page.

* **User Reviews & Ratings:**
    * [ ] Allow logged-in users to submit reviews and assign ratings to products.
    * [ ] Display average ratings and individual reviews on product detail pages.

* **Product Image Management:**
    * [ ] Enable actual image uploads for products via the Django admin interface.
    * [ ] Display product images dynamically on product list and detail pages.

* **Improved Error Handling & Feedback:**
    * [ ] Implement custom 404 (Page Not Found) and 500 (Server Error) pages.
    * [ ] More granular user feedback for various interactions.

---

## Phase 4: Advanced Features & Deployment

Preparing the application for real-world usage and scaling.

* **Payment Gateway Integration:**
    * [ ] Integrate with a secure payment gateway (e.g., Stripe, PayPal) for processing transactions.

* **Frontend Framework Integration (Optional):**
    * [ ] Consider integrating a modern JavaScript framework (e.g., React, Vue.js) for a more dynamic and interactive user interface, especially for the cart and checkout processes.

* **Deployment Strategy:**
    * [ ] Prepare the application for deployment to a production server (e.g., Heroku, AWS, DigitalOcean).
    * [ ] Configure production-ready settings, including static file serving, media file storage, and database.

* **Admin Enhancements:**
    * [ ] Implement custom actions or advanced filters in Django admin as needed for business operations.

---

This roadmap is a living document and may be adjusted based on feedback, priorities, and emerging requirements.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/raunakmishraa/django-ecommerce/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/raunakmishraa/django-ecommerce/issues)**: Submit bugs found or log feature requests for the `django-ecommerce` project.
- **💡 [Submit Pull Requests](https://github.com/raunakmishraa/django-ecommerce/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/raunakmishraa/django-ecommerce/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/raunakmishraa/django-ecommerce/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=raunakmishraa/django-ecommerce">
   </a>
</p>
</details>

---
