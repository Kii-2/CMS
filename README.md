project Overview:
This Django project aims to create a scalable content management system (CMS) designed to support multiple sites on a single backend. 
The system features dynamic webpage management, device catalogs, and lead capture forms for lead generation. 
Additionally, the project will include REST APIs for mobile integration to extend functionality to an Android app.
The CMS will allow site administrators to manage webpages dynamically, associate content sections, and control device visibility for visitors. 
Users can explore devices, fill out forms for more information, and receive personalized responses with tokenized walk-in records. 
The backend will maintain extensive data models to handle city-specific data, vendors, and devices, while the frontend will present a seamless experience through responsive designs.

How to run:
1. Clone the repo in your local system
2. Make migrations using: python manage.py makemigrations
3. Migrate the migrations: python manage.py migrate
4. To run the server: python manage.py runserver


API exposed:
1. Lead capture API: /api/leads/
   Sample Payload:
   {
    "lead_data" : {
    "name": "Kritika Singh",
    "phone_number": "1234567890",
    "email": "kritikasengar56@gmail.com",
    "address": "123 Sector",
    "city": 1,
    "referral_code": "REF123"
    },
    "device_id": 1,
    "vendor_id": 2
  }

    Sample Response:
   {
    "token": 5
   }

2. Devices available: /api/devices/
    GET API to get list of devices

   
