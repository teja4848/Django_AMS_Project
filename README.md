# 🚗 Automobile Management System (AMS)

## 📜 Introduction to AMS:
The **Automobile Management System (AMS)** is a comprehensive solution for managing various aspects of an automobile business. From managing vehicles, handling fleet operations, tracking expenses, to handling customer feedback, AMS offers an all-in-one platform for administrators, mechanics, and customers.

Automobiles consist of numerous systems—engine, transmission, cooling, exhaust, suspension—that ensure a vehicle's operation. The AMS ensures that these systems are tracked and managed efficiently, contributing to smoother fleet operations and better service quality.

## ✨ Features of AMS:
AMS provides 9 core modules:

- 🔑 **Login/Registration:** Secure access for all users.
- 👤 **Profiles:** Manage and update user profiles.
- 🚗 **Vehicles:** Add, view, and manage vehicle listings.
- 🛠️ **Fleet Management:** Efficiently manage fleet operations.
- 🗓️ **Booking Charts:** Track and schedule vehicle bookings.
- 💸 **Expenses:** Record and manage expenses associated with vehicles.
- 💳 **Payment and Invoices:** Manage payments from generated invoices.
- 📊 **Reports:** Generate reports for analysis.
- 💬 **Feedback:** Collect feedback from users for continuous improvement.

The **Vehicles Module** is central to the system and interacts with all other modules. It allows users to list vehicles, and view all available listings in the system.

## 🧑‍💻 User Roles:

### Admin:
- Add, update, delete, and manage customer and mechanic information.
- Approve or reject mechanic requests based on skills.
- Add customer invoices, mechanic salaries, attendance, and view feedbacks.
- Generate vehicle reports and manage service costs.

### Mechanic:
- Apply for jobs and update their skills.
- View and update the status of assigned work.
- Track salary, attendance, and repair history.
- Provide feedback to the admin.

### Customer:
- Request services and view the status of approved or pending requests.
- View invoices for vehicle repairs and services and make payments.
- Leave feedback for the admin.

## 🛠️ Technologies Used:
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL 
- **Deployment:** PythonAnywhere
- **Version Control:** Git & GitHub


### 🔧 Installation Instructions:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/teja4848/Django_AMS_Project.git
   cd Django_AMS_Project
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the App:**  
   Open the following URL in your browser:
   ```bash
   http://127.0.0.1:8000/
   ```

### 📊 Live Demo: 
👉 Experience the live demo here: [Live Demo](https://saiananya.pythonanywhere.com/)  
Explore the features of the Automobile Management System and see how it can streamline your vehicle management tasks. 

### 🔐 License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### 📝 Feedback & Contributions:
- **Feedback:** I would love to hear from you! Feel free to open issues or submit feedback directly in the repository.
- **Contributions:** Fork the repository, create a new branch, and submit a pull request.
