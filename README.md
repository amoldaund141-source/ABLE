# ABLE: Accessibility & Inclusion Platform

ABLE is a comprehensive, full-stack accessibility platform designed to connect citizens who need physical assistance with verified volunteers (such as NSS students), while also tracking and reporting physical accessibility barriers across the city.

## 🌟 Key Features

### 🏢 Citizen Portal
- **Request Assistance:** Users can drop a pin and request immediate on-ground physical assistance (e.g., wheelchair navigation).
- **Report Barriers:** Citizens can log physical barriers (e.g., broken ramps, blocked tactile paths) directly to a central database.
- **My Dashboard:** Track the live status of your requests (Pending -> Dispatched -> Resolved).

### 🤝 Volunteer Dashboard
- **Live Interactive Maps:** An integrated Leaflet.js map pings the database and drops geographic markers for nearby urgent requests.
- **Real-Time Dispatch:** Volunteers can instantly accept a job and navigate to the citizen.
- **Verified Accounts:** Secure NSS ID Document upload and Admin verification workflow.
- **Certificates:** Automated PDF generation for volunteer appreciation.

### 🛡️ Admin Dashboard
- **System Overview:** Monitor total users, active volunteers, and pending requests.
- **Identity Verification Portal:** Admins can view uploaded ID cards and securely approve/reject new volunteer applications.
- **Directory Management:** Manage the city-wide directory of verified accessible locations.

### ♿ Accessibility First
- Integrated high-contrast Dark Mode.
- Live English-to-Marathi language toggling.
- Built-in text-enlargement tools.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla Javascript, Leaflet.js (Maps)
- **Backend:** Python (Flask)
- **Database:** SQLite3

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/amoldaund141-source/ABLE.git
   cd ABLE
   ```

2. **Install dependencies**
   Ensure you have Python installed. Install the Flask framework:
   ```bash
   pip install flask
   ```

3. **Start the Backend Server**
   ```bash
   python app.py
   ```

4. **Access the Application**
   Open your browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```
   *(The SQLite database `database.db` will be automatically generated upon first run.)*

---

## 🔑 Default Test Credentials

Use these credentials on the `/login.html` page to explore the different dashboards:

| Role | Email | Password |
|------|-------|----------|
| **Admin** | `admin@able.org` | `admin123` |
| **Volunteer** | `volunteer@nss.org` | `vol123` |
| **Citizen** | `user@citizen.org` | `user123` |

---
*Built with precision and care to make the world a more accessible place.*
