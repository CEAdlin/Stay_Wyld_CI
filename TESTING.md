
# 🧪 Testing

Testing was carried out throughout development to ensure that the application was functional, responsive, accessible and secure.

Testing included:

- User story testing
- Feature testing
- Form validation
- Booking validation
- Authentication testing
- Authorisation testing
- Responsive testing
- Browser compatibility testing
- HTML validation
- CSS validation
- JavaScript validation
- Python/Django checks
- Lighthouse testing
- Manual bug testing

---
# Automated Testing

The Django system check completed successfully with no configuration issues.
![Django system check passed](documentation/automated_testing/manage.py_check.png)

The test suite completed successfully with all tests passing.
![Django Automated Tests](documentation/automated_testing/manage.py_test.png)

Python Syntax was checked, no syntax errors were found:
![Python Syntax Test](documentation/automated_testing/python_syntax_validation.png)

# Manual Testing – User Stories

Each user story was manually tested to confirm that the implemented functionality meets the acceptance criteria and provides the intended experience for visitors, customers and administrators.

## Visitor User Stories

| ID | User Type | User Story | Test | Expected Result | Screenshot |
|---|---|---|---|---|---|
| US01 | Visitor | As a visitor, I want to view the homepage so that I can understand what the glampsite offers. | Navigate to the website homepage. | The homepage loads successfully and clearly presents the glampsite, accommodation and key information. | ![US01 Homepage Test](documentation/features/index_navbarsandhero.png) |
| US02 | Visitor | As a visitor, I want to view the three accommodation units so that I can decide which accommodation is suitable for me. | Navigate to the accommodation section and view each unit. | All three accommodation units are displayed with relevant information. | ![US02 Accommodation Test](documentation/features/index_staywithus.png) |
| US03 | Visitor | As a visitor, I want to submit an enquiry so that I can ask questions before booking. | Complete and submit the enquiry form using valid information. | The enquiry is submitted successfully and confirmation is provided to the visitor. | N/A - feature not implemented |
| US04 | Visitor | As a visitor, I want to see a calendar showing availability and nightly prices. | Open the availability calendar and select different dates. | The calendar displays available and unavailable dates and the correct nightly prices. | ![US04 Availability Test](documentation/features/unit_detail_c.png) |
| US05 | Visitor | As a visitor, I want to view accommodation photographs so that I can understand what the units and site look like. | Open the accommodation photographs/gallery. | Relevant photographs are displayed correctly and can be viewed clearly. | ![US05 Photograph Test](documentation/features/customer_unit_detail_facilities_and_gallery.png) |

## Customer User Stories

| ID | User Type | User Story | Test | Expected Result | Screenshot |
|---|---|---|---|---|---|
| US06 | Customer | As a customer, I want to register for an account so that I can book online. | Complete the registration form using valid customer details. | A customer account is created successfully and the customer can access the booking functionality. | ![US06 Registration Test](documentation/features/register_validation.png) |
| US07 | Customer | As a registered customer, I want to log in securely so that I can access my account and see my booking/s. | Enter valid login credentials and submit the login form. | The customer is securely logged in and can access their account and bookings. | ![US07 Login Test](documentation/features/my_bookings.png) |
| US08 | Customer | As a customer, I want to book an available unit so that I can arrange my stay. | Select an available unit and valid dates and complete the booking process. | The booking is successfully created and stored against the customer's account. | ![US08 Booking Test](documentation/features/customer_booking_submitted.png) |
| US09 | Customer | As a customer, I want to see live prices for my selected dates. | Select different accommodation and booking dates. | The total price updates correctly according to the selected dates and nightly prices. | ![US09 Pricing Test](documentation/features/customer_create_booking_arrival_time_validation.png) |
| US10 | Customer | As a customer, I want to view my bookings so that I can check my upcoming stays along with balances paid and outstanding. | Log in and open the customer's bookings/account page. | The customer's bookings are displayed with relevant stay dates, accommodation and payment balance information. | ![US10 Booking History Test](documentation/features/customer_my_bookings.png) |
| US11 | Customer | As a customer, I want to be able to request to modify a booking online. | Open an existing booking and submit a modification  request. | The request is submitted successfully and the customer receives confirmation. | ![US11 Booking Request Test](documentation/features/booking_create_update_request.png) ![US11 Modification Feedback Test](documentation/features/booking_update_status_feedback.png) |
| US12 | Customer | As a customer, I would like to post a review of my glamping unit along with pictures. | Submit a review with text and an image after a stay. | The review and photograph are submitted successfully and displayed appropriately. | N/A - feature not implemented |
| US13 | Customer | As a customer, I want to be able to edit my profile details so that my information remains up to date. | Log in and edit the customer's profile information. | The updated profile information is saved successfully and displayed correctly. | N/A - feature not implemented |
| US14 | Customer | As a customer, I would like to receive reminder emails before my stay with any helpful information. | Create an upcoming booking and trigger/test the booking reminder process. | A reminder email is sent to the customer before their stay containing relevant information. | N/A - feature not implemented |

## Administrator User Stories

| ID | User Type | User Story | Test | Expected Result | Screenshot |
|---|---|---|---|---|---|
| US15 | Administrator | As an administrator, I want to securely log in so that I can manage the website. | Access the administrator login and enter valid administrator credentials. | The administrator is securely logged in and can access the administration functionality. | ![US15 Admin Login Test](documentation/features/login.png) |
| US16 | Administrator | As an administrator, I want to edit accommodation units so that the website information remains up to date. | Edit an existing unit; description, occupancy, dog-friendly & images. | Accommodation information is successfully created and updated, and changes appear on the website. | ![US16 Accommodation Management Test](documentation/features/admin_unit_detail.png) |![US16 Accommodation Management Test](documentation/features/admin_unit_detail_gallery.png)
| US17 | Administrator | As an administrator, I want to view and modify bookings so that I can manage reservations. | Log in as an administrator and view/edit an existing booking. | The administrator can view and successfully modify booking information. | ![US17 Booking Management Test](documentation/features/admin_booking_modify.png) |
| US18 | Administrator | As an administrator, I want to create a booking on behalf of a customer so that I can handle bookings made by phone or in person. | Create a booking through the administration area. | A booking is successfully created and linked to the correct customer and accommodation. | ![US18 Admin Booking Test](documentation/features/admin_create_customer_booking.png) |
| US19 | Administrator | As an administrator, I want to set a minimum stay for bookings. | Bookings below the set minimum stay are blocked and the customer is prompted. | Bookings below the minimum stay are prevented and valid bookings are accepted. | ![US19 Minimum Stay Test](documentation/features/create_booking_2nightmin.png) |
| US20 | Administrator | As an administrator, I want to manage accommodation images so that website photographs can be updated without changing the code. | Add, edit or remove an accommodation image through the administration area. | Images can be successfully managed and changes are reflected on the website. | ![US20 Image Management Test](documentation/features/admin_unit_detail_gallery.png) |
| US21 | Administrator | As an administrator, I want to view customer enquiries so that I can respond to potential customers. | Log in to the administration area and open the enquiries section. | Customer enquiries are displayed with the relevant customer and enquiry information. | N/A - feature not implemented |
| US22 | Administrator | As an administrator, I want to view a list of all bookings so that I can monitor current, upcoming and previous stays. | Open the bookings section within the administration area. | All relevant bookings are displayed with accommodation, customer and date information. | ![US22 Booking List Test](documentation/features/admin_bookings_list_2.png) |
| US23 | Administrator | As an administrator, I want to access a dashboard showing units, upcoming bookings, registered customers and bookings per unit this month so that I can quickly monitor the glampsite. | Log in to the administration area and open the dashboard. | The dashboard displays accurate information for units, upcoming bookings, registered customers, unread enquiries, unavailable units and bookings per unit for the current month. | ![US23 Dashboard Test](documentation/features/admin_dashboard.png) ![US23 Dashboard Test](documentation/features/admin_bookings_list_2.png)|
| US24 | Administrator | As an administrator, I want to be able to search customers by name so that I can quickly find customer information. | Enter a customer's name into the customer search function. | Customers matching the search criteria are displayed. | ![US24 Customer Search Test](documentation/features/admin_customer_list_filter_name.png) |
| US25 | Administrator | As an administrator, I want each booking to automatically be assigned a unique booking reference number so that bookings can be easily identified. | Create a new booking and view the booking details. | A unique booking reference number is automatically generated and assigned to the booking in the form of an ID. | ![US25 Booking Reference Test](documentation/features/admin_booking_detail.png) |
| US26 | Administrator | As an administrator, I want to be able to search bookings by booking ID so that I can quickly find a specific reservation. | Enter a valid booking reference ID into the booking search function. | The booking matching the reference ID number is displayed. | ![US26 Booking Search Test](documentation/features/admin_booking_filter_id.png) |
| US27 | Administrator | As an administrator, I want to be able to see booking statistics by unit so that I can understand booking trends. | Open the booking statistics section and The number of bookings is displayed. | A list of bookings per unit is displayed: past, present and future. | ![US27 Booking Search By Unit Test](documentation/features/admin_booking_filter_unit.png) |
| US28 | Administrator | As an administrator, I want to be able to temporarily block out dates by unit for maintenance or private use so that unavailable dates cannot be booked. | Block selected dates for a specific accommodation unit and attempt to make a booking for those dates. | The selected dates are shown as unavailable and customers cannot book the unit during the blocked period. | ![US28 Blocked Dates Test](documentation/features/admin_unit_availability.png) |
| US29 | Administrator | As an administrator, I want to manage unit pricing so that accommodation prices remain accurate throughout the year. | Configure different prices for units and date periods. | The correct price is displayed for the selected unit and dates. | ![US29 Modify Unit Pricing](documentation/features/admin_unit_detail_cont..png) |
| US30 | Administrator | As an administrator, I want to view registered customers so that I can access and manage customer accounts and contact information. | Open the customer management section. | A list of registered customers is displayed with relevant account and contact information. | ![US30 Customer Management Test](documentation/features/admin_customers_list_2.png) |
| US31 | Administrator | As an administrator, I want to filter bookings by date, accommodation and status so that I can quickly find specific bookings. | Apply different booking filters. | The booking list updates to display only bookings matching the selected filters. | ![US31 Booking Filtering Test](documentation/features/admin_booking_filter_unit.png) ![US31 Booking Filtering Status Test](documentation/features/admin_booking_filter_past.png) ![US31 Booking Filtering Status Test](documentation/features/admin_booking_filter_id.png)|

# Manual Testing – Features

Each major feature was manually tested to ensure that it works as intended across different user roles, devices and scenarios.

| Feature | Test | Expected Result | Actual Result | Screenshot | Pass/Fail |
|---|---|---|---|---|---|
| Navigation | Click each navigation link from the homepage. | Each link directs the user to the correct page or section. | Each navigation link directed to the correct page or section. | ![Navigation Test](documentation/features/index_navbarsandhero.png) | Pass |
| Homepage | Load the homepage. | Homepage loads successfully with all content, images and navigation displayed correctly. | The homepage loaded successfully with its content, images and navigation displayed correctly. | ![Homepage Test](documentation/features/index_navbarsandhero.png) | Pass |
| Accommodation Listings | Open the accommodation section. | All three accommodation units are displayed with correct information. | All three accommodation units were displayed with the correct information. | ![Accommodation Listings Test](documentation/features/index_staywithus.png) | Pass |
| Accommodation Details | Select an individual accommodation unit. | The correct accommodation details, facilities, pricing and photographs are displayed. | The selected unit displayed the correct details, facilities, pricing and photographs. | ![Accommodation Details Test](documentation/features/unit_detail_b.png) | Pass |
| Accommodation Images | Open accommodation photographs/gallery. | Images load correctly and are displayed clearly. | The accommodation images loaded correctly and were displayed clearly. | ![Accommodation Images Test](documentation/features/unit_detail_a.png) | Pass |
| Availability Calendar | Open the availability calendar. | Calendar displays available and unavailable dates correctly. | The calendar displayed available and unavailable dates correctly. | ![Availability Calendar Test](documentation/features/unit_detail_c.png) | Pass |
| Availability Calendar | Select dates containing an existing booking. | Dates that are already booked are shown as unavailable. | Existing booking dates were shown as unavailable. | ![Booked Dates Test](documentation/features/booking_dates_taken.png) | Pass |
| Availability Calendar | Select dates outside existing bookings. | Available dates can be selected for booking. | Dates outside existing bookings could be selected for booking. | ![Available Dates Test](documentation/features/customer_create_booking_arrival_time_validation.png) | Pass |
| Live Pricing | Select different accommodation and dates. | The displayed price updates correctly according to the selected accommodation and dates. | The displayed price updated correctly for the selected accommodation and dates. | ![Live Pricing Test](documentation/features/booking_price_update_live.png) | Pass |
| Minimum Stay | Attempt to book fewer nights than the configured minimum stay. | The system prevents the booking and displays an appropriate message. | The system prevented the booking and displayed the minimum-stay message. | ![Minimum Stay Error Test](documentation/features/create_booking_2nightmin.png) | Pass |
| Minimum Stay | Attempt to book the minimum number of nights. | The booking can proceed successfully. | A booking meeting the minimum stay could proceed successfully. | ![Minimum Stay Success Test](documentation/features/minimum_2nightstay.png) | Pass |
| Booking Validation | Select a departure date before the arrival date. | The system prevents an invalid booking and displays an appropriate error message. | The system prevented the invalid date selection and displayed an appropriate message. | ![Date Validation Test](documentation/features/booking_price_update_live.png) | Pass |
| Booking Validation | Attempt to book dates that overlap an existing booking. | The system prevents the overlapping booking. | The system prevented the overlapping booking. | ![Booking Overlap Test](documentation/features/booking_dates_taken.png) | Pass |
| Customer Registration | Register using valid customer information. | A new customer account is successfully created. | A new customer account was created successfully. | ![Registration Test](documentation/features/register_validation.png) | Pass |
| Customer Registration | Attempt to register with invalid or incomplete information. | Validation messages are displayed and the account is not created until valid information is provided. | Validation messages were displayed and the account was not created until valid information was provided. | ![Registration Validation Test](documentation/features/register_validation.png) | Pass |
| Customer Login | Log in using valid customer credentials. | Customer is successfully authenticated and redirected to the appropriate page. | The customer was authenticated successfully and redirected to the appropriate page. | ![Customer Login Test](documentation/features/login.png) | Pass |
| Customer Login | Attempt to log in using incorrect credentials. | Login fails and an appropriate error message is displayed. | Login failed and an appropriate error message was displayed. | ![Invalid Login Test](documentation/features/login_incorrect.png) | Pass |
| Customer Logout | Select the logout option while logged in. | Customer is securely logged out and redirected appropriately. | The customer was logged out securely and redirected to index.html. | ![Logout Test](documentation/features/index_loggedout.png) | Pass |
| Customer Bookings | Log in and open the customer's bookings. | Only the logged-in customer's bookings are displayed. | Only the logged-in customer's bookings were displayed. | ![Customer Bookings Test](documentation/features/my_bookings.png) | Pass |
| Booking Reference | Create a new booking. | A unique booking reference ID is automatically generated and displayed. | A unique booking reference was generated and displayed. | ![Booking Reference Test](documentation/features/booking_detail.png) | Pass |
| Booking Confirmation | Complete a booking successfully. | Confirmation is displayed with booking details, dates, accommodation and booking reference. | Confirmation displayed the booking details, dates, accommodation and booking reference. | ![Booking Confirmation Test](documentation/features/booking_status_confirmed.png) | Pass |
| Profile Editing | Edit customer profile information. | Updated information is saved and displayed correctly. | Updated customer information was saved and displayed correctly. | ![Profile Editing Test](documentation/features/admin_customer_update_feedback.png) | Pass |
| Booking Modification Request | Submit a request to modify an existing booking. | The modification request is submitted successfully and confirmation is provided. | The modification request was submitted successfully and confirmation was provided. | ![Booking Modification Test](documentation/features/customer_update_feedback.png) | Pass |
| Customer Booking Cancellation | Cancel a booking with clear feedback. | The cancellation is confirmed, the booking is cancelled and the booking status reflects this. | The cancellation request was submitted successfully and confirmation was provided. | ![Booking Cancellation Test](documentation/features/customer_booking_detail_cancellation_request_accepted.png) ![Booking Cancel Status](documentation/features/customer_booking_detail_cancel_request.png)| Pass |
| Admin Login | Log in using valid administrator credentials. | Administrator is authenticated and can access administrative functionality. | The administrator was authenticated and could access the administrative functionality. | ![Admin Login Test](documentation/features/login.png) | Pass |
| Admin Access Control | Attempt to access administrator functionality as a normal customer or visitor. | Unauthorised users are prevented from accessing restricted functionality and are re-directed to index.html. | Unauthorised users were prevented from accessing restricted functionality. | ![Admin Access Test](documentation/features/index_loggedout.png) | Pass |
| Admin Dashboard | Open the administrator dashboard. | Dashboard displays units, upcoming bookings, registered customers, unread enquiries, unavailable units and bookings per unit this month. | The dashboard displayed the unit, booking, customer and availability information. | ![Admin Dashboard Test](documentation/features/admin_dashboard.png) | Pass |
| Edit Accommodation | Edit an existing accommodation unit. | Changes are saved and displayed correctly on the website. | Accommodation changes were saved and displayed correctly on the website. | ![Edit Accommodation Test](documentation/features/admin_unit_detail.png) | Pass |
| Manage Images | Add, edit or remove accommodation images through the administration area. | Images are successfully managed and website content updates accordingly. | Accommodation images were managed successfully and the website content updated accordingly. | ![Manage Images Test](documentation/features/admin_unit_detail_gallery.png) | Pass |
| View Bookings | Open the administrator booking list. | Administrator can view relevant customer, accommodation, date and booking information. | The administrator could view the relevant booking information. | ![View Bookings Test](documentation/features/admin_bookings_list_2.png) | Pass |
| Modify Bookings | Edit an existing booking as an administrator. | Booking information is successfully updated. | Booking information was updated successfully. | ![Modify Booking Test](documentation/features/admin_booking_modify.png) | Pass |
| Create Admin Booking | Create a booking on behalf of a customer. | Booking is successfully created and linked to the correct customer and accommodation. | The booking was created successfully and linked to the correct customer and accommodation. | ![Admin Booking Test](documentation/features/admin_create_customer_booking.png) | Pass |
| Customer Search | Search for a customer using their name. | Matching customers are displayed. | Customers matching the searched name were displayed. | ![Customer Name Search Test](documentation/features/admin_customer_list_filter_name.png) | Pass |
| Booking Search | Search for a booking using its booking reference ID. | The matching booking is displayed. | The booking matching the reference ID was displayed. | ![Booking Search Test](documentation/features/admin_booking_filter_id.png) | Pass |
| Booking Filtering | Filter bookings by date. | Only bookings matching the selected date criteria are displayed. | Only bookings matching the selected date criteria were displayed. | ![Booking Date Filter Test](documentation/features/admin_booking_filter_date.png) | Pass |
| Booking Filtering | Filter bookings by accommodation. | Only bookings for the selected accommodation are displayed. | Only bookings for the selected accommodation were displayed. | ![Booking Accommodation Filter Test](documentation/features/admin_booking_filter_unit.png) | Pass |
| Blocked Dates | Block dates for a specific accommodation for maintenance or private use. | Selected dates become unavailable for customer bookings. | Selected dates became unavailable for customer bookings. | ![Blocked Dates Test](documentation/features/admin_unit_availability.png) | Pass |
| Error Handling | Trigger common validation and booking errors. | User receives clear and understandable error messages. | Clear and understandable error messages were displayed. | ![Error Handling Test](documentation/features/customer_create_booking_name_validation.png) | Pass |
| 404 Error Page | Navigate to a non-existent page. | A custom 404 page is displayed instead of an unhandled server error. | The custom 404 page was displayed instead of an unhandled server error. | ![404 Error Test](documentation/features/404_page.png) | Pass |

---

# 🔦 Lighthouse

Lighthouse was used to audit the deployed site across Performance,
Accessibility, Best Practices and SEO. The evidence below includes a mobile
homepage audit and a desktop unit-page audit. Scores can vary depending on
network conditions, device emulation and the page being tested.

Testing was carried out on the deployed website.

### Lighthouse Results

![Lighthouse Results Desktop](documentation/lighthouse_unitpage_desktop.png)
![Lighthouse Results Mobile](documentation/lighthouse_homepage_mobile.png)

| Lighthouse category | Score | Notes and improvements |
| --- | --- | --- |
| Performance | 78 | The site contains image-rich accommodation content. Images were compressed and converted to WebP to reduce transfer size. Remaining opportunities include reducing render-blocking CSS and external font requests. |
| Accessibility | 97 | The remaining deduction is related to colour contrast in the availability calendar, where blocked dates use a muted grey treatment. This is documented as a future improvement while preserving the visual distinction between available, booked and blocked dates. |
| Best Practices | 100 | No Lighthouse best-practice failures were reported in the tested audit. Production settings were checked separately to ensure `DEBUG` is disabled and secrets are stored as environment variables. |
| SEO | 100 | The audit found no SEO issues in the tested pages. Page titles and meta descriptions are present. |

### Lighthouse Improvements

Any issues identified through Lighthouse testing were reviewed and improvements were made where appropriate.

Examples include:

- Converting images from .png to .webp.
- Adding in a missing alt text.
- Improving colour contrast, especially on the calendars.
- Improving heading hierarchy.

# 🌐 Browser Compatibility

The website was tested using multiple modern browsers to ensure consistent functionality.

### Browser Testing Evidence

| Browser | Desktop | Mobile | Result |
|---|---|---|---|
| Google Chrome | ![Chrome Desktop](documentation/features/browser_chrome.png) | ![Chrome Mobile](documentation/features/browser_chrome_mobile.png) | Passed |
| Microsoft Edge | ![Edge Desktop](documentation/features/browser_edge.png) | ![Edge Mobile](documentation/features/index_mobile.png) | Passed |
| Mozilla Firefox | ![Firefox Desktop](documentation/features/browser_firefox.png) | ![Firefox Mobile](documentation/features/browser_firefox_mobile.png) | passed |


# 📱 Responsiveness

The website was designed using a responsive, mobile-first approach.

Testing was carried out at different screen sizes to ensure:

- Content remains readable.
- Navigation remains usable.
- Images scale correctly.
- Forms remain accessible.
- Buttons remain usable.
- No horizontal scrolling occurs.
- Layouts adapt appropriately.

My features & user stories testing screenshots comprehensively cover desktop devices, to save redant images  only tablet and mobile device screenshots are listed below.

### Tablet Devices

| Page | Screenshot | 
|---|---|
| index.html | <img src="documentation/devices_tablet/tablet_index_1.png" alt="Tablet Index 1" width="150"> <img src="documentation/devices_tablet/tablet_index_2.png" alt="Tablet Index 2" width="150"> <img src="documentation/devices_tablet/tablet_index_3.png" alt="Tablet Index 3" width="150"> |
| register.html | <img src="documentation/devices_tablet/tablet-register.png" alt="Tablet Register" width="150"> |
| booking_create.html | <img src="documentation/devices_tablet/tablet_create_booking.png" alt="Tablet Create Booking" width="150"> <img src="documentation/devices_tablet/tablet_create_booking_feedback.png" alt="Tablet Create Booking Feedback" width="150"> |
| booking_delete.html | <img src="documentation/devices_tablet/tablet_cancel_confirmation.png" alt="Tablet Cancel Confirmation" width="150"> |
| 404.html | <img src="documentation/devices_tablet/tablet_404.png" alt="Tablet 404" width="150"> |
| login.html | <img src="documentation/devices_tablet/tablet_login.png" alt="Tablet Login" width="150"> |
| booking_detail.html | <img src="documentation/devices_tablet/tablet_booking_detail.png" alt="Tablet Booking Detail" width="150"> |
| booking_update.html | <img src="documentation/devices_tablet/tablet_booking_update.png" alt="Tablet Booking Update" width="150"> <img src="documentation/devices_tablet/tablet_update_feedback.png" alt="Tablet Update Feedback" width="150"> |
| my_bookings.html | <img src="documentation/devices_tablet/tablet_my_bookings.png" alt="Tablet My Bookings" width="150"> |
| unit_detail.html | <img src="documentation/devices_tablet/tablet_unit_detail_1.png" alt="Tablet Unit Detail 1" width="150"> <img src="documentation/devices_tablet/tablet_unit_detail_2.png" alt="Tablet Unit Detail 2" width="150"> <img src="documentation/devices_tablet/tablet_unit_detail_3.png" alt="Tablet Unit Detail 3" width="150"> |
| admin_dashboard.html | <img src="documentation/devices_tablet/tablet_admin_dashboard.png" alt="Tablet Admin Dashboard" width="150"> |
| admin_booking_list.html | <img src="documentation/devices_tablet/tablet_admin_booking_list.png" alt="Tablet Admin Booking List" width="150"> |
| admin_booking_detail.html | <img src="documentation/devices_tablet/tablet_admin_booking_detail.png" alt="Tablet Admin Booking Detail" width="150"> |
| admin_customers_list.html | <img src="documentation/devices_tablet/tablet_admin_customers_list.png" alt="Tablet Admin Customers List" width="150"> |
| admin_customer_detail.html | <img src="documentation/devices_tablet/tablet_admin_customer_detail.png" alt="Tablet Admin Customer Detail" width="150"> |
| admin_units_list.html | <img src="documentation/devices_tablet/tablet_admin_unit_list.png" alt="Tablet Admin Unit List" width="150"> |
| admin_unit_detail.html | <img src="documentation/devices_tablet/tablet_admin_unit_detail.png" alt="Tablet Admin Unit Detail 1" width="150"> <img src="documentation/devices_tablet/tablet_admin_unit_detail_2.png" alt="Tablet Admin Unit Detail 2" width="150"> <img src="documentation/devices_tablet/tablet_admin_unit_detail_3.png" alt="Tablet Admin Unit Detail 3" width="150"> |

### Mobile Devices

| Page | Screenshot | 
|---|---|
| index.html | <img src="documentation/devices_mobile/mobile_index.html.png" alt="Mobile Index" width="150"> <img src="documentation/devices_mobile/mobile_index.html_2.png" alt="Mobile Index 2" width="150"> <img src="documentation/devices_mobile/mobile_index.html_3.png" alt="Mobile Index 3" width="150"> <img src="documentation/devices_mobile/mobile_index.html_4.png" alt="Mobile Index 4" width="150"> |
| register.html | <img src="documentation/devices_mobile/mobile_register.png" alt="Mobile Register" width="150"> |
| booking_create.html | <img src="documentation/devices_mobile/mobile_booking_create.html.png" alt="Mobile Booking Create" width="150"> <img src="documentation/devices_mobile/mobile_booking_create_confirmation.png" alt="Mobile Booking Create Confirmation" width="150"> |
| booking_delete.html | N/A |
| 404.html | <img src="documentation/devices_mobile/mobile_404.png" alt="Mobile 404" width="150"> |
| login.html | <img src="documentation/devices_mobile/mobile_login.png" alt="Mobile Login" width="150"> |
| booking_detail.html | <img src="documentation/devices_mobile/mobile_booking_detail.html.png" alt="Mobile Booking Detail" width="150"> <img src="documentation/devices_mobile/mobile_booking_detail.hml_2.png" alt="Mobile Booking Detail 2" width="150"> |
| booking_update.html | <img src="documentation/devices_mobile/mobile_booking_update_request.html.png" alt="Mobile Booking Update" width="150"> <img src="documentation/devices_mobile/mobile_booking_update_request.html_2.png" alt="Mobile Booking Update 2" width="150"> |
| my_bookings.html | <img src="documentation/devices_mobile/mobile_my_bookings.html.png" alt="Mobile My Bookings" width="150"> |
| unit_detail.html | <img src="documentation/devices_mobile/mobile_unit_detail.html.png" alt="Mobile Unit Detail" width="150"> |
| admin_dashboard.html | <img src="documentation/devices_mobile/mobile_admin_dashboard.html.png" alt="Mobile Admin Dashboard" width="150"> |
| admin_booking_list.html | <img src="documentation/devices_mobile/mobile_admin_booking_list.html.png" alt="Mobile Admin Booking List" width="150"> |
| admin_booking_detail.html | <img src="documentation/devices_mobile/mobile_admin_booking_detail.html.png" alt="Mobile Admin Booking Detail" width="150"> |
| admin_customers_list.html | <img src="documentation/devices_mobile/mobile_admin_customers_list.html.png" alt="Mobile Admin Customers List" width="150"> |
| admin_customer_detail.html | <img src="documentation/devices_mobile/mobile_admin_customer_detail.html.png" alt="Mobile Admin Customer Detail" width="150"> |
| admin_units_list.html | <img src="documentation/devices_mobile/mobile_admin_units_list.html.png" alt="Mobile Admin Units List" width="150"> |
| admin_unit_detail.html | <img src="documentation/devices_mobile/mobile_admin_unit_detail.html.png" alt="Mobile Admin Unit Detail" width="150"> <img src="documentation/devices_mobile/mobile_admin_unit_detail.html_2.png" alt="Mobile Admin Unit Detail 2" width="150"> |

# ✅ Code Validation

## HTML Validation

The website was tested using the W3C HTML Validator.

| page | Screenshot |
|--|--|
| index.html | ![Index HTML validation](documentation/code_html/index.png) |
| register.html | ![Register HTML validation](documentation/code_html/register.png) |
| login.html | ![Login HTML validation](documentation/code_html/login.png) |
| booking_create.html | ![Booking create HTML validation](documentation/code_html/create_booking.png) |
| booking_delete.html | N/A |
| booking_detail.html | ![Booking detail HTML validation](documentation/code_html/booking_detail.png) |
| booking_page.html | N/A |
| booking_update.html | ![Booking update HTML validation](documentation/code_html/booking_update.png) |
| calendar.html | N/A |
| my_bookings.html | ![My bookings HTML validation](documentation/code_html/my_bookings.png) |
| unit_detail.html | ![Unit detail Keepers Cottage HTML validation](documentation/code_html/unit_detail_kc.png) ![Unit detail Shepherds Keep HTML validation](documentation/code_html/unit_detail_sk.png) ![Unit detail Tinkers Lodge HTML validation](documentation/code_html/unit_detail_tl.png) |
| admin_dashboard.html | ![Admin dashboard HTML validation](documentation/code_html/admin_dashboard.png) |
| admin_booking_list.html | ![Admin booking list HTML validation](documentation/code_html/admin_booking_list.png) |
| admin_booking_detail.html | ![Admin booking detail HTML validation](documentation/code_html/admin_booking_detail.png) |
| admin_customers_list.html | ![Admin customers list HTML validation](documentation/code_html/admin_customers_list.png) |
| admin_customer_detail.html | ![Admin customer detail HTML validation](documentation/code_html/admin_customer_detail.png) |
| admin_units_list.html | ![Admin unit list HTML validation](documentation/code_html/admin_unit_list.png) |
| admin_unit_detail.html | ![Admin unit detail HTML validation](documentation/code_html/admin_unit_detail.png) |
| base.html | N/A |
| 404.html | N/A |

### Result

TODO – Add validation result and describe any issues found and resolved.

---

## CSS Validation

The website was tested using the W3C CSS Validator.

![CSS Validation](file)

### Result

TODO – Add validation result and describe any issues found and resolved.

---

## JavaScript Validation

JavaScript was tested using an appropriate JavaScript validation or linting tool.

![JavaScript Validation](file)

### Result

TODO – Add validation result.

---

## Python / Django Validation

Django's built-in project checks were used to identify configuration and code issues.

Example:

python manage.py check

## 🐞 Bugs

Below is a table outlining known and resolved bugs identified during development and testing.

| Bug ID | Bug Description | Cause | Solution | Unresolved Bug Screenshot | Resolved Bug Screenshot | Status |
|--------|------------------|--------|-----------|-----------------------------|----------------------------|---------|
| 001 | Accommodation images occasionally fail to load on mobile | Slow Cloudinary response / missing responsive breakpoints | Added responsive image sizes and lazy loading | *(Insert screenshot)* | *(Insert screenshot)* | Resolved |
| 002 | Booking form allowed stays under two nights | Missing validation logic in booking model | Added server-side validation enforcing minimum stay | *(Insert screenshot)* | *(Insert screenshot)* | Resolved |
| 003 | Navigation links break on small screens | CSS media query conflict | Updated breakpoints and improved mobile nav styling | *(Insert screenshot)* | *(Insert screenshot)* | Resolved |
| 004 | Form validation messages not displaying in Safari | Browser-specific form behaviour | Added custom JS validation messages | *(Insert screenshot)* | *(Insert screenshot)* | Resolved |
| 005 | Occasional slow loading on accommodation list page | Large image payloads | Enabled Cloudinary auto‑compression and caching | *(Insert screenshot)* | *(Insert screenshot)* | Partially Resolved |