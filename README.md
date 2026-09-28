

# Stay Wyld 

## Site & Developer Links:

Deployed Site: [StayWyld](https://staywyld-capstone-b19305edb31c.herokuapp.com/)

[GitHub Project Board](https://github.com/users/CEAdlin/projects/4)

Developer: Corrine Adlington ([CEAdlin](https://www.github.com/CEAdlin))

### SuperUser Login Credentials:
Username: CorrineAd

Password: Test1234

## Project Overview:

A responsive, full-stack Django web application designed to allow visitors to explore three glamping units, make enquiries, register as customers and book available accommodation for a minimum two-night stay. The website will include customer authentication, a database-driven booking and availability system, and a secure admin area where accommodation, customers and bookings can be managed. The project will demonstrate the use of HTML, CSS, JavaScript, Python, Django, Cloudinary and Heroku, following Agile development principles and MoSCoW prioritisation.

![screenshot](documentation\AmIResponsive_Screenshot.png)


## User Stories

User stories organised by 'user'.

### Visitor Stories

| ID | User story | Priority | Board status |
| --- | --- | --- | --- |
| US01 | As a visitor, I want to view the homepage so that I can understand what Stay Wyld offers. | Must | Done |
| US02 | As a visitor, I want to view the accommodation units so that I can choose a suitable stay. | Must | Done |
| US03 | As a visitor, I want to submit an enquiry through my dashboard prior to booking. | Could | Todo |
| US04 | As a visitor, I want to view availability and prices so that I can choose suitable dates. | Must | Done |
| US05 | As a visitor, I want to view accommodation photographs before booking. | Should | Done |

### Customer Stories

| ID | User story | Priority | Board status |
| --- | --- | --- | --- |
| US06 | As a customer, I want to register for an account so that I can manage bookings. | Must | Done |
| US07 | As a customer, I want to log in securely so that I can access my account. | Must | Done |
| US08 | As a customer, I want to book an available unit so that I can reserve my stay. | Must | Done |
| US09 | As a customer, I want to see live prices for selected dates. | Must | Done |
| US10 | As a customer, I want to view my bookings and stay history. | Should | Done |
| US11 | As a customer, I want to request a booking modification or cancellation. | Should | Done |
| US12 | As a customer, I want to post a review. | Could | Won'tHave |
| US13 | As a customer, I want to edit my customer profile. | Could | Todo |
| US14 | As a customer, I want to receive booking reminder emails. | Could | Won'tHave |

### Administrator Stories

| ID | User story | Priority | Board status |
| --- | --- | --- | --- |
| US15 | As an administrator, I want to log in securely so that I can manage the website. | Must | Done |
| US16 | As an administrator, I want to add and edit accommodation units. | Must | Done |
| US17 | As an administrator, I want to view and modify bookings. | Must | Done |
| US18 | As an administrator, I want to create bookings on behalf of customers. | Must | Done |
| US19 | As an administrator, I want to enforce a minimum stay. | Must | Done |
| US20 | As an administrator, I want to manage accommodation images. | Should | Done |
| US21 | As an administrator, I want to view customer enquiries. | Could | Todo |
| US22 | As an administrator, I want to view bookings and previous stays. | Should | Done |
| US23 | As an administrator, I want a dashboard to monitor the glampsite. | Should | Done |
| US24 | As an administrator, I want to search customers by name. | Should | Done |
| US25 | As an administrator, I want each booking to have a unique ID. | Should | Done |
| US26 | As an administrator, I want to search bookings by ID. | Should | Done |
| US27 | As an administrator, I want to view booking information by accommodation unit. | Should | Done |
| US28 | As an administrator, I want to block dates by unit. | Should | Done |
| US29 | As an administrator, I want to manage unit pricing so that accommodation prices. | Should | Done |
| US30 | As an administrator, I want to view and update registered customers. | Could | Done |
| US31 | As an administrator, I want to filter bookings by date, accommodation and 'Active' status. | Could | Done |

## Wireframes

The following full-page wireframes show the planned desktop, tablet and mobile
layouts in the order a visitor, customer or administrator would normally access
the application. Each image includes the complete page flow, including lower
content sections and the footer.

### 1. `index.html`

| Full-page wireframe |
| --- |
| ![Homepage full-page wireframe](documentation/wireframes/index-full.svg) |

### 2. `unit_detail.html`

| Full-page wireframe |
| --- |
| ![Unit detail full-page wireframe](documentation/wireframes/unit_detail-full.svg) |

### 3. `booking_create.html`

| Full-page wireframe |
| --- |
| ![Booking create full-page wireframe](documentation/wireframes/booking_create-full.svg) |

### 4. `my_bookings.html`

| Full-page wireframe |
| --- |
| ![My bookings full-page wireframe](documentation/wireframes/my-bookings-full.svg) |

### 5. `booking_detail.html`

| Full-page wireframe |
| --- |
| ![Booking detail full-page wireframe](documentation/wireframes/booking_detail-full.svg) |

### 6. `booking_update.html`

| Full-page wireframe |
| --- |
| ![Booking update full-page wireframe](documentation/wireframes/booking_update-full.svg) |

### 7. `admin_dashboard.html`

| Full-page wireframe |
| --- |
| ![Admin dashboard full-page wireframe](documentation/wireframes/admin_dashboard-full.svg) |

### 8. `admin_bookings_list.html`

| Full-page wireframe |
| --- |
| ![Admin bookings list full-page wireframe](documentation/wireframes/admin_bookings_list-full.svg) |

### 9. `admin_booking_detail.html`

| Full-page wireframe |
| --- |
| ![Admin booking detail full-page wireframe](documentation/wireframes/admin_booking_detail-full.svg) |

### 10. `admin_customers_list.html`

| Full-page wireframe |
| --- |
| ![Admin customers list full-page wireframe](documentation/wireframes/admin_customers_list-full.svg) |

### 11. `admin_customer_detail.html`

| Full-page wireframe |
| --- |
| ![Admin customer detail full-page wireframe](documentation/wireframes/admin_customer_detail-full.svg) |

### 12. `admin_units_list.html`

| Full-page wireframe |
| --- |
| ![Admin units list full-page wireframe](documentation/wireframes/admin_units_list-full.svg) |

### 13. `admin_unit_detail.html`

| Full-page wireframe |
| --- |
| ![Admin unit detail full-page wireframe](documentation/wireframes/admin_unit_detail-full.svg) |

### Wireframe Summary

The wireframes were an important part of my planning process. They helped me
organise the site's information architecture, map the customer booking journey
and identify the main functions required on each page. Creating desktop, tablet
and mobile layouts also encouraged me to consider responsive behaviour before
implementation, including the way forms, booking calendars, tables and
administration controls would reflow on smaller screens.

During development, I adapted some of the original layouts as the functionality
became clearer and as usability issues were identified through testing. These
changes included refining the booking flow, separating customer and staff
workflows, improving filter controls and restructuring content for mobile
devices. The final design is therefore an informed evolution of the initial
wireframes rather than a direct copy, and better reflects the completed
application and its real user journeys.

## Design and Planning
### Purpose and Target Users

Stay Wyld is designed for visitors and customers who want to explore a small
glamping site, check availability and make a booking. A second user group is
staff, who need a practical administration area for managing units, images,
blocked dates, customers and bookings.

The main user problem is that accommodation information, availability and
booking management need to be available in one clear workflow. The design
therefore separates the public discovery journey from the authenticated
customer journey and the staff management journey.

### Layout and Design Rationale

The visual direction is inspired by woodland accommodation and combines dark
green, dark blue, muted gold and light neutral surfaces. Large accommodation
imagery establishes the setting, while structured sections and clear buttons
make booking actions easy to find.

The main layout decisions were:

- The homepage hero introduces the brand and leads into the accommodation list.
- The three units are displayed as full-width stacked rows so each unit has
	enough space for its image, description, facilities and booking actions.
- Unit detail pages separate information, gallery images and availability.
- Booking pages place date selection beside booking details on larger screens
	and stack them on smaller screens.
- Customer pages prioritise booking status, dates and next actions.
- Staff pages use denser tables, filters and management panels for repeated
	administrative tasks.

### Typography

- **Island Moments** is the primary display font used for branding and large
	headings.
- **Cormorant Garamond** is the secondary font used for body copy, labels and
	interface text.
- **Manrope** is imported as an additional interface font option.

![Fonts Used](documentation\Googlefonts_fontsused.png)

### Colour Palette

The implemented CSS variables are:

| Variable | Value | Use |
| --- | --- | --- |
| `--colour-primary` | `#436043` | Primary green text and accents |
| `--colour-secondary` | `#759075` | Supporting green states |
| `--colour-tertiary` | `#ffffff` | Light text and surfaces |
| `--colour-accent` | `#c1bd88` | Gold borders, buttons and highlights |
| `--colour-blue` | `#28293e` | Dark panels, navigation and footer |

![Stay Wyld colour palette](documentation\staywyld_colourpalette.png)

### UX, Accessibility and Responsive Planning

The templates use semantic headings, labelled form controls, descriptive image
alternative text, native buttons and links, and responsive CSS media queries.
The heading structure was reviewed so pages use a logical `h1`, `h2` and `h3`
sequence. The implementation also includes:

- Clear navigation and booking calls to action.
- Separate customer and staff workflows.
- Clear validation messages and user feedback.
- Keyboard-friendly native controls and visible focus styling.
- Responsive layouts without loss of core functionality.

### Responsive Planning

Responsive behaviour was considered during the planning and wireframing stages.
The layouts were designed for desktop, tablet and mobile screen sizes using CSS
media queries, Flexbox and Grid.

On the homepage, the three accommodation units remain as full-width rows rather
than being forced into narrow columns. On booking pages, the availability
calendar and booking form sit beside each other on larger screens and stack
vertically on smaller screens. Tables and administration filters are allowed to
wrap or scroll where necessary so that functionality remains usable on mobile
devices.

Responsive testing was carried out using browser developer tools and the
deployed site. The main checks included readable text, usable navigation,
accessible form controls, correctly scaled images, no unnecessary horizontal
scrolling and buttons that remain easy to use on touch screens.

### Lighthouse Evidence

Lighthouse was used to audit the deployed site across Performance,
Accessibility, Best Practices and SEO. The evidence below includes a mobile
homepage audit and a desktop unit-page audit. Scores can vary depending on
network conditions, device emulation and the page being tested.

Homepage - Mobile:
![Lighthouse results mobile](documentation\lighthouse_homepage_mobile.png)
Units page - Desktop:
![Lighthouse results desktop](documentation\lighthouse_unitpage_desktop.png)


| Lighthouse category | Score | Notes and improvements |
| --- | --- | --- |
| Performance | 78 | The site contains image-rich accommodation content. Images were compressed and converted to WebP to reduce transfer size. Remaining opportunities include reducing render-blocking CSS and external font requests. |
| Accessibility | 97 | The remaining deduction is related to colour contrast in the availability calendar, where blocked dates use a muted grey treatment. This is documented as a future improvement while preserving the visual distinction between available, booked and blocked dates. |
| Best Practices | 100 | No Lighthouse best-practice failures were reported in the tested audit. Production settings were checked separately to ensure `DEBUG` is disabled and secrets are stored as environment variables. |
| SEO | 100 | The audit found no SEO issues in the tested pages. Page titles and meta descriptions are present. |

## Agile Methodology

Agile methodology was used to develop Stay Wyld in small, manageable feature
slices rather than attempting to build the complete application at once. The
work was planned around the needs of visitors, customers and administrators,
then refined as features were implemented and tested.

### User Stories and Acceptance Criteria

The product backlog was organised into user stories on the GitHub Project Board.
Each story described the user type, desired outcome and reason for the feature.
Acceptance criteria were used to define what successful completion looked like.
For example, the booking story required date selection, availability checking,
price calculation, the two-night minimum and successful database storage.

Stories were broken into practical development tasks, such as creating models,
views, templates, validation, permissions and tests. The full story tables are
documented earlier in this README and the detailed issue-style stories are in
`documentation/github_issues.md`.

### Kanban Board

![Project Board:](documentation\Project_Board.png)

The GitHub Project Board was used as a Kanban board. Cards were organised by
status and moved as work progressed:

Completed features were checked manually and with automated tests before being
treated as Done. The board provided a visible record of planned, active and
completed work.

![User Story:](documentation\user-story.png)

Story points were not used. Work was prioritised using MoSCoW labels and user-story priority.

### MoSCoW Prioritisation

The stories were prioritised using MoSCoW:

- **Must:** Essential booking, account and administration functionality.
- **Should:** Important improvements that support the main workflows.
- **Could:** Useful extensions that are outside the minimum viable product.
- **Won't:** Outside the scope of this project, but could be useful additions further down the line.

This prioritisation kept the core booking and authentication journeys ahead of
optional features such as reviews, reminder emails and online payments.

### Iteration and Review

Development changed in response to testing, browser behaviour and deployment
feedback. Iterative improvements included:

- Refining responsive layouts for mobile, tablet and desktop.
- Correcting booking date validation and allowing check-in on checkout dates.
- Adding blocked-date availability management.
- Adding booking ID, unit, date and status filters.
- Adding customer-name search and reset controls.
- Moving uploaded media to Cloudinary for reliable production storage.
- Improving heading hierarchy, alternative text and meta descriptions.
- Removing invalid CDN references identified through Lighthouse.

### Agile Reflection

The board and user stories helped keep the work visible and prioritised. Testing
each feature as it was completed made it easier to identify issues early and
adapt the design without losing sight of the main booking purpose. Features
that were not required for the first version were kept as future scope rather
than delaying the core release.

# Stay Wyld Database Diagram

```mermaid
erDiagram
    USER ||--o| CUSTOMER_PROFILE : has
    USER ||--o{ BOOKING : makes
    USER ||--o{ BOOKING_CHANGE_REQUEST : submits
    UNIT ||--o{ BOOKING : receives
    UNIT ||--o{ UNIT_GALLERY_IMAGE : contains
    UNIT ||--o{ UNIT_BLOCKED_DATE : blocks
    BOOKING ||--o{ BOOKING_CHANGE_REQUEST : receives

    USER {
        int id PK
        string username
        string email
        boolean is_staff
        boolean is_superuser
    }

    CUSTOMER_PROFILE {
        int id PK
        int user_id FK
        string full_name
        text address
        string phone_number
    }

    UNIT {
        int id PK
        string name
        string slug
        string short_description
        text description
        image main_image
        int max_adults
        int max_children
        decimal price_per_night
        decimal dog_surcharge
        string dog_charge_type
        boolean dogs_allowed
        boolean active
    }

    UNIT_GALLERY_IMAGE {
        int id PK
        int unit_id FK
        image image
        int position
    }

    UNIT_BLOCKED_DATE {
        int id PK
        int unit_id FK
        date date
    }

    BOOKING {
        int id PK
        int customer_id FK
        int unit_id FK
        string customer_name
        email customer_email
        string customer_phone
        date check_in_date
        date check_out_date
        int adults
        int children
        int infants
        int dogs
        decimal dog_surcharge
        decimal nightly_price
        int total_nights
        decimal total_amount
        text special_requests
        boolean agreed_terms
        string status
        datetime created_at
        datetime updated_at
    }

    BOOKING_CHANGE_REQUEST {
        int id PK
        int booking_id FK
        int customer_id FK
        string request_type
        text message
        date requested_check_in
        date requested_check_out
        int requested_adults
        int requested_children
        int requested_dogs
        string status
        datetime created_at
    }
```

## Relationship Notes

 Each registered customer has one `CustomerProfile` linked to exactly one Django `User`, enforced by the one-to-one relationship. 
 Staff and superuser accounts use Django's built-in `User` account for administration and are intentionally exempt from the customer-specific profile. `CustomerProfile.user_id` is therefore unique. 
 `Unit.slug` is also unique in Django, although those uniqueness markers are omitted from the Mermaid field syntax for parser compatibility.
 An authenticated customer can have many bookings. An administrator-created booking may have no linked user because the customer's name, email and phone are stored directly on the booking.
 A unit can have many bookings, gallery images and blocked dates.
 A booking can have multiple modification or cancellation requests, each submitted by a customer user, only one request per unit can be open at any one time.
 The unique unit/date constraint prevents the same date being blocked more than
 once for a particular unit.

## Workflow Notes

A customer booking is initially stored with a `PENDING` status. Staff can review it and change the status to `CONFIRMED`, `CANCELLED` or `COMPLETED`.
Customer modification and cancellation requests are stored separately in `BookingChangeRequest`. Staff approval is represented by the request status changing from `OPEN` to `APPROVED` or the internal `REJECTED` value, which is displayed to users as **Declined**.
A booking is not considered available only because it is pending. The booking availability logic checks date overlap and ignores cancelled bookings.
Staff can create `UnitBlockedDate` records for maintenance or private use. Blocked nights are displayed as unavailable and rejected by the booking validation logic.
A following booking can check in on the previous booking's checkout date,
because the checkout date is treated as the exclusive end of the stay.

## Features

The tables below summarise the main implemented features. Wireframe thumbnails
are clickable and open the full-page design evidence. 

### Navigation (including login and registration)

| Feature | Description | Screenshot |
| --- | --- | --- |
| Public navigation | Main navigation bar with top, user-nav-bar showing login status | ![Index Navigation](documentation\features\index_navbarsandhero.png) |
| Login and registration | Customers can register, log in and log out. Navigation changes according to authentication state and role. | ![Login Page](documentation\features\login.png)![Register Page](documentation\features\register_validation.png) |

### Security

| Feature | Description | Screenshot |
| --- | --- | --- |
| Defensive programming | Forms validate required values, dates, guest numbers, passwords and booking rules. Invalid input receives clear feedback. | ![Register Field Required](documentation\features\register_validation.png) ![Arrival Time Field Required](documentation\features\customer_create_booking_arrival_time_validation.png) ![Date Availability Validation](documentation\features\customer_create_booking_available_date_validation.png) ![Name Field Required](documentation\features\customer_create_booking_name_validation.png) ![Minimum Stay Enforcement](documentation\features\customer-unit_detail_minimum_stay_validation.png) ![Admin Delete Booking Confirmation](documentation\features\admin_bookings_list_delete_prompt.png) |
| Authentication and authorisation | If not logged in - directed to login-page to access user/super-user restricted content. If user is logged in and attempts to access super-user restricted content request will be ignored and they will be re-drected to index.html. | ![Re-direct To Login Page](documentation\features\login.png) |

### Homepage

| Feature | Description | Screenshot |
| --- | --- | --- |
| Brand introduction | Hero content introduces Stay Wyld and provides clear booking calls to action. | ![Homepage Hero](documentation\features\index_navbarsandhero.png)![Homepage Booking Call To Action](documentation\features\index_booknow_cta.png) |
| Unit rows | Three accommodation units are shown as full-width stacked rows with images, descriptions, facilities and booking links. | ![Index Stay With Us Section](documentation\features\index_booknow_cta.png) |
| About and gallery | The homepage continues with the About section, photo gallery and footer contact details. | ![Index Gallery](documentation\features\index_gallery.png) ![Index Gallery & Footer](documentation\features\index_footer.png)|

### Unit Details

| Feature | Description | Screenshot |
| --- | --- | --- |
| Unit information | Displays unit name, description, facilities, capacity, pricing and main image. | ![Customer Unit Detail](documentation\features\customer_unit_detail.png) ![Customer Unit Detail Gallery & Facilities](documentation\features\customer_unit_detail_facilities_and_gallery.png) ![Customer Unit Occupancy etc.](documentation\features\Customer_Unit_Detail_Occupancy.png) ![Customer Unit Detail Availability Calendar](documentation\features\customer-unit_detail_availability_calendar.png) |
| Gallery | Displays additional Cloudinary-backed gallery images. | ![Customer Unit Detail Cloudinary Gallery](documentation\features\customer_unit_detail_booknow_cta.png) |
| Booking call to action | Links the visitor to the booking flow for the selected unit. | ![Customer Unit Book Now Call To Action](documentation\features\customer-unit_detail_availability_calendar.png) |

### Create A Booking

| Feature | Description | Screenshot |
| --- | --- | --- |
| Availability calendar | Shows booked and blocked dates and lets customers select valid dates. | ![Create a Booking Calendar](documentation\features\customer_create_booking_available_date_validation.png)  |
| Booking validation | Enforces the two-night minimum, prevents overlaps and allows check-in on an existing checkout date. | ![Minimum Stay Enforcement](documentation\features\customer-unit_detail_minimum_stay_validation.png)  |
| Pricing and confirmation | Calculates nights, nightly price and dog surcharge before confirmation. | ![Create Booking Total Price Display](documentation\features\customer_create_booking_arrival_time_validation.png) ![Create Booking Feedback](documentation\features\customer_create_booking_feedback.png) |
| My Bookings - View My Bookings | User can log in to view 'My Bookings' section and view all bookings along with status. | ![My Bookings List View](documentation\features\customer_my_bookings.png) ![Customer Booking Detail](documentation\features\customer_booking_detail.png) |

### Update Booking Request

| Feature | Description | Screenshot |
| --- | --- | --- |
| Request form | Customers can submit requested date, guest and dog changes for staff approval. | ![Booking Update Request](documentation\features\customer_booking_detail_update_request.png) |
| Request Submitted | The customer can see that their update request has been submitted and awaiting admin approval. | ![Booking Update Request Feedback](documentation\features\customer_booking_update_request_feedback.png) |

### Delete Booking Request

| Feature | Description | Screenshot |
| --- | --- | --- |
| Cancellation request | Customers submit a cancellation request rather than directly deleting protected booking data. | ![Booking Cancel Request](documentation/features/customer_booking_detail_cancel_request.png) |
| Staff decision | Staff can approve or decline the request, with the user-facing status displayed as Declined when appropriate. | ![Admin Can Accept Or Reject Cancel Request](documentation\features\admin_booking_detail_request_open.png) |
| Customer cancellation request accepted | If the cancellation request was accepted by the admin this is reflected within the customers 'My Bookings' and booking detail. | ![Customer Cancellation Request Accepted](documentation\features\customer_booking_cancel_request_accepted.png) |
| Customer cancellation request rejected | If the cancellation request was rejected by the admin this is reflected within the customers 'My Bookings' and booking detail and the booking stays open. | ![Customer cancellation request rejected](documentation\features\customer_booking_cancel_request_declined.png) |

### Admin Dashboard

| Feature | Description | Screenshot |
| --- | --- | --- |
| Staff overview | Provides navigation and summary access to units, customers, bookings and availability management. | ![Admin dashboard](documentation\features\admin_dashboard.png) |

### Admin Booking List

| Feature | Description | Screenshot |
| --- | --- | --- |
| Booking table | Shows customer, unit, dates, status, request status and actions. | ![Admin bookings list](documentation\features\admin_bookings_list.png) |
| Filters | Filters by current/upcoming, past, current, upcoming, unit, date range and exact booking ID. | ![Admin bookings list filter ID](documentation\features\admin_bookings_list_filter_ID.png) ![Admin bookings list filter by date](documentation\features\admin_bookings_list_filter_date.png) ![Admin bookings list filter by 'past'](documentation\features\admin_bookings_list_filter_past.png) |
| Clear control | Resets all booking filters and returns to the default current/upcoming view. | ![Admin bookings list filter clear button](documentation\features\admin_bookings_list.png) |

### Admin Detail (including requests and modify)

| Feature | Description | Screenshot |
| --- | --- | --- |
| Booking details | Staff can view customer contact details, dates, guests, price and status. | ![Admin booking detail](documentation\features\admin_booking_detail.png) |
| Modify booking | Staff can update booking dates, guests, dogs and status. | ![Admin booking detail modify](documentation\features\admin_booking_modify.png) |
| Change requests | Staff can review open modification or cancellation requests and approve or decline them. | ![Admin accept or decline request](documentation\features\admin_booking_detail_request_open.png) |

### Customer List

| Feature | Description | Screenshot |
| --- | --- | --- |
| Customer records | Superusers can view registered customer names, email, phone, booking count and active-booking state. | ![Admin customers list](documentation\features\admin_customers_list.png) |
| Search and sorting | Customers can be sorted A-Z or by active booking and searched by partial name with reset control. | ![Admin customer list filter by name](documentation\features\admin_customers_list_filter_name.png) ![Admin customer list filter by active](documentation\features\admin_customers_list_filter_active.png) |

### Customer Detail (including modify and delete)

| Feature | Description | Screenshot |
| --- | --- | --- |
| Customer profile | Superusers can view and update customer name, email, address and phone details. | ![Admin customer detail](documentation\features\admin_customer_detail.png) |
| Customer bookings | Displays bookings associated with the selected customer. | ![Admin customer detail bookings](documentation\features\admin_customer_detail_cont..png) |
| Admin customer update feedback | Admin can update the customers profile, feedback is then shown once the changes are saved. | ![Admin customer update feedback](documentation\features\admin_customer_update_feedback.png) |

### Unit List

| Feature | Description | Screenshot |
| --- | --- | --- |
| Unit overview | Staff can view the available unit records and access each unit's management page. | ![Admin units wireframe](documentation\features\admin_units_list.png) |

### Unit Detail (including update)

| Feature | Description | Screenshot |
| --- | --- | --- |
| Unit editing | Staff can update name, descriptions, capacity, pricing, dog settings and active status. | ![Admin unit detail](documentation\features\admin_unit_detail.png) ![Admin unit detail cont.](documentation\features\admin_unit_detail_cont..png) |
| Media management | Staff can upload, order and delete main and gallery images stored through Cloudinary. | ![Admin unit detail wireframe](documentation\features\admin_unit_detail_gallery.png) |
| Blocked availability | Staff can select dates and mark them unavailable or available. Booked dates cannot be changed. | ![Admin unit availability](documentation\features\admin_unit_detail_availability.png) |

## Technologies Used

### Overview

Stay Wyld is a full-stack web application for browsing glamping accommodation, checking availability and managing bookings. It is built with Django and uses Python for booking logic, customer accounts, authentication, database models and staff administration.

Django templates generate the HTML pages. Bootstrap provides responsive components, custom CSS provides the Stay Wyld visual design, and JavaScript adds client-side interaction such as image galleries, booking forms and the availability calendar.

### Frontend

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) for semantic page structure and content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for responsive layouts and custom styling.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for client-side interaction and validation.
- [Bootstrap 5](https://getbootstrap.com/) and [Bootstrap Icons](https://icons.getbootstrap.com/) for responsive components and interface icons.
- [FullCalendar](https://fullcalendar.io/) for displaying accommodation availability.

### Backend

- [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/) for the application, routing, templates, forms, authentication, sessions and administration.
- [Django ORM](https://docs.djangoproject.com/en/stable/topics/db/queries/) for database queries and model relationships.
- [django-admin-sortable2](https://github.com/jrief/django-admin-sortable2) for ordering accommodation gallery images in the admin area.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for loading local settings from `.env`.
- [dj-database-url](https://pypi.org/project/dj-database-url/) for parsing the database connection URL.

### Database

The application uses Django's database abstraction, allowing separate databases for development and deployment:

- [SQLite](https://www.sqlite.org/) is the default local database stored in `db.sqlite3`.
- [PostgreSQL](https://www.postgresql.org/) is used by the deployed Heroku application.
- [psycopg2-binary](https://www.psycopg.org/) provides the PostgreSQL database adapter.

Django migrations manage the schema for customer profiles, accommodation units, gallery images, blocked dates, bookings and booking change requests.

### Media and Static Files

- [Cloudinary](https://cloudinary.com/) and [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) store and deliver accommodation images in production.
- [Pillow](https://python-pillow.org/) provides image processing support for uploaded images.
- [WhiteNoise](https://whitenoise.readthedocs.io/) serves static files through the deployed WSGI application.

## Bugs

| Bug encountered | Fix implemented |
| --- | --- |
| Blocked dates were not consistently shown or enforced in the booking calendar. | Normalised blocked dates to ISO format, passed them safely from Django to JavaScript, displayed them in the calendar and checked them again during booking validation. |
| Data tables disappeared or became unusable on mobile screens, removing access to important information and actions. | Added responsive table wrappers with horizontal scrolling and adjusted mobile table display, sizing and spacing so the content remains available on smaller screens. |
| Administrators could be redirected to the customer `my_bookings.html` page instead of the staff `admin_bookings_list.html` page. | Separated customer and administrator routing and redirects, using the correct destination for each authenticated user role. |
| The accent gold colour had insufficient contrast against white backgrounds across the site. | Reviewed the colour usage across shared components, changed low-contrast text and controls to darker accessible colours, and checked the result with Lighthouse. |
| The accommodation capacity field changed from `max_guests` to separate `max_adults` and `max_children` values, but some forms, views and templates still used the old field. | Updated the model references, migration, admin pages, forms, views and templates so capacity is handled consistently for adults and children. |
| Uploaded accommodation images were being saved in the project root instead of the intended media locations. | Set the correct `upload_to` paths for main and gallery images and configured Django's Cloudinary storage backend for production media. |

## Deployment

This project can be copied from GitHub, run locally with SQLite, and deployed to Heroku with PostgreSQL and Cloudinary-backed media storage.

### Fork the Repository

Forking creates your own GitHub copy of the project, which you can modify and deploy independently.

1. Sign in to [GitHub](https://github.com/).
2. Open the [Stay Wyld repository](https://github.com/CEAdlin/capstone_staywyld) and select **Fork**.
3. Choose your GitHub account as the destination and create the fork.

### Clone the Repository

Clone your fork to your computer after forking it:

```powershell
git clone https://github.com/<your-github-username>/capstone_staywyld.git
cd capstone_staywyld
```

### Run Locally

Create a virtual environment and install the pinned dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the project root. The local configuration can use the included SQLite database:

```env
SECRET_KEY=your-local-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Create the database tables and start the development server:

```powershell
python manage.py migrate
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

### Deploy to Heroku

1. Create a [Heroku](https://www.heroku.com/) account and select **Create new app** from the dashboard.
2. Give the app a unique name and choose a region.
3. In the app's **Settings**, open **Config Vars** and add:
    - `SECRET_KEY`: a secure production secret.
    - `DEBUG`: `False`.
    - `DATABASE_URL`: the PostgreSQL database connection URL.
    - `CLOUDINARY_URL`: the Cloudinary connection URL used for uploaded accommodation images.
4. Open the **Deploy** tab, select GitHub as the deployment method and connect the forked repository.
5. Select the branch to deploy and choose **Deploy Branch**.

Heroku installs the dependencies from `requirements.txt` and uses the `Procfile` command `gunicorn config.wsgi` to serve the Django application. WhiteNoise serves static files, while Cloudinary stores production media. After deployment, run migrations from the Heroku app's terminal or release process if they have not been applied automatically.

### Updating a Deployment

When GitHub integration is connected, push changes to the selected branch and redeploy from Heroku. With manual deployment enabled, select **Deploy Branch** after each push.

## Testing

Please see TESTING.md 

## AI Usage

AI tools, including GitHub Copilot and ChatGPT, were used as development support throughout the project. The following summary focuses on the outcomes of that use.

### Code Creation

Copilot helped generate and refine Django views, URL patterns, templates, CSS rules and JavaScript for the booking flow, availability calendars, customer accounts and administration features. Generated suggestions were adapted to the existing project structure and helped accelerate implementation of features such as date validation, image management and responsive layouts.

### Debugging

AI assistance helped identify and resolve issues including blocked dates not being carried correctly into the calendar, incorrect customer and administrator redirects, the `max_guests` to `max_adults` and `max_children` model change, media files being stored in the wrong location, and tables becoming unusable on mobile screens. It also helped trace deployment and static-file problems by comparing settings, templates and server output.

### Performance and User Experience

AI suggestions supported improvements to responsive layouts, mobile table scrolling, image handling through Cloudinary, accessible colour contrast, heading structure and form feedback. Lighthouse results and browser testing were used to assess these changes, with the final decisions based on observed behaviour rather than generated suggestions alone.

### Automated Unit Tests

GitHub Copilot was used to create Django unit-test structures for booking availability, blocked dates, checkout-date reuse, admin date blocking and booking-list behaviour. The generated tests were reviewed and adjusted so that dates, redirects, database records and availability rules matched the actual application logic. This provided focused coverage for important customer and staff workflows.

### Reflection on the Development Process

AI reduced time spent searching for syntax, alternative implementations and documentation wording, allowing more time for testing and design decisions. It worked best as a review and problem-solving partner rather than an automatic source of final code. Manual testing, Django checks, browser inspection and personal understanding of the generated code remained necessary throughout development.

AI was also used to create original site images inspired by real-world glamping designs and builds. These images were reviewed and edited before being used in the project.

All AI generated content was manually reviewed, edited, and validated to ensure accuracy and alignment with project requirements.  

## Credits

This project was completed as part of the Code Institute four-month bootcamp. I would like to thank Code Institute for providing the course structure, learning resources, project guidance and technical material that supported my development throughout the programme.

Special thanks to the Code Institute mentors for their time, advice and knowledge, and for helping me work through challenges in development, testing and deployment.

### Software and Services Used

- **Visual Studio Code** for writing and organising the project code.
- **Python and Django** for the application backend, booking logic, authentication and database-driven features.
- **Bootstrap and Bootstrap Icons** for responsive layout components and interface icons.
- **JavaScript and FullCalendar** for client-side interaction and the accommodation availability calendar.
- **Adobe Photoshop** for editing images and creating the Stay Wyld logo and favicon.
- **ChatGPT** for generating original image assets and supporting visual content creation.
- **Chrome DevTools** for responsive testing, browser inspection and debugging.
- **Google Lighthouse** for auditing performance, accessibility, best practices and SEO.
- **Git and GitHub** for version control, source-code management and the project board.
- **Cloudinary** for storing and delivering accommodation images in production.
- **Heroku** for hosting and deploying the live application.
- **W3C Markup Validation Service** for checking the validity of the HTML structure.
- **W3C CSS Validation Service** for checking CSS syntax and standards compliance.
- **JSHint** for identifying potential errors and quality issues in JavaScript.
- **PEP 8** for checking Python style and formatting conventions.
- **Chrome DevTools** for browser inspection, responsive layout testing and debugging.
- **Google Lighthouse** for testing performance, accessibility, best practices and SEO.


