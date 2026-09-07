
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

# Manual Testing – User Stories

Each user story was manually tested to confirm that the implemented functionality meets the acceptance criteria and provides the intended experience for visitors, customers and administrators.

## Visitor User Stories

| ID | User Type | User Story | Test | Expected Result | Actual Result | Screenshot | Pass/Fail |
|---|---|---|---|---|---|---|---|
| US01 | Visitor | As a visitor, I want to view the homepage so that I can understand what the glampsite offers. | Navigate to the website homepage. | The homepage loads successfully and clearly presents the glampsite, accommodation and key information. | TODO | ![US01 Homepage Test](file) | TODO |
| US02 | Visitor | As a visitor, I want to view the three accommodation units so that I can decide which accommodation is suitable for me. | Navigate to the accommodation section and view each unit. | All three accommodation units are displayed with relevant information. | TODO | ![US02 Accommodation Test](file) | TODO |
| US03 | Visitor | As a visitor, I want to submit an enquiry so that I can ask questions before booking. | Complete and submit the enquiry form using valid information. | The enquiry is submitted successfully and confirmation is provided to the visitor. | TODO | ![US03 Enquiry Test](file) | TODO |
| US04 | Visitor | As a visitor, I want to see a calendar showing availability and nightly prices. | Open the availability calendar and select different dates. | The calendar displays available and unavailable dates and the correct nightly prices. | TODO | ![US04 Availability Test](file) | TODO |
| US05 | Visitor | As a visitor, I want to view accommodation photographs so that I can understand what the units and site look like. | Open the accommodation photographs/gallery. | Relevant photographs are displayed correctly and can be viewed clearly. | TODO | ![US05 Photograph Test](file) | TODO |

## Customer User Stories

| ID | User Type | User Story | Test | Expected Result | Actual Result | Screenshot | Pass/Fail |
|---|---|---|---|---|---|---|---|
| US06 | Customer | As a customer, I want to register for an account so that I can book online. | Complete the registration form using valid customer details. | A customer account is created successfully and the customer can access the booking functionality. | TODO | ![US06 Registration Test](file) | TODO |
| US07 | Customer | As a registered customer, I want to log in securely so that I can access my account and see my booking/s. | Enter valid login credentials and submit the login form. | The customer is securely logged in and can access their account and bookings. | TODO | ![US07 Login Test](file) | TODO |
| US08 | Customer | As a customer, I want to book an available unit so that I can arrange my stay. | Select an available unit and valid dates and complete the booking process. | The booking is successfully created and stored against the customer's account. | TODO | ![US08 Booking Test](file) | TODO |
| US09 | Customer | As a customer, I want to see live prices for my selected dates. | Select different accommodation and booking dates. | The total price updates correctly according to the selected dates and nightly prices. | TODO | ![US09 Pricing Test](file) | TODO |
| US10 | Customer | As a customer, I want to view my bookings so that I can check my upcoming stays along with balances paid and outstanding. | Log in and open the customer's bookings/account page. | The customer's bookings are displayed with relevant stay dates, accommodation and payment balance information. | TODO | ![US10 Booking History Test](file) | TODO |
| US11 | Customer | As a customer, I want to be able to request to modify or cancel a booking online. | Open an existing booking and submit a modification or cancellation request. | The request is submitted successfully and the customer receives confirmation. | TODO | ![US11 Booking Request Test](file) | TODO |
| US12 | Customer | As a customer, I would like to post a review of my glamping unit along with pictures. | Submit a review with text and an image after a stay. | The review and photograph are submitted successfully and displayed appropriately. | TODO | ![US12 Review Test](file) | TODO |
| US13 | Customer | As a customer, I want to be able to edit my profile details so that my information remains up to date. | Log in and edit the customer's profile information. | The updated profile information is saved successfully and displayed correctly. | TODO | ![US13 Profile Test](file) | TODO |
| US14 | Customer | As a customer, I would like to receive reminder emails before my stay with any helpful information. | Create an upcoming booking and trigger/test the booking reminder process. | A reminder email is sent to the customer before their stay containing relevant information. | TODO | ![US14 Reminder Email Test](file) | TODO |

## Administrator User Stories

| ID | User Type | User Story | Test | Expected Result | Actual Result | Screenshot | Pass/Fail |
|---|---|---|---|---|---|---|---|
| US15 | Administrator | As an administrator, I want to securely log in so that I can manage the website. | Access the administrator login and enter valid administrator credentials. | The administrator is securely logged in and can access the administration functionality. | TODO | ![US15 Admin Login Test](file) | TODO |
| US16 | Administrator | As an administrator, I want to add and edit accommodation units so that the website information remains up to date. | Add a new accommodation unit and edit an existing unit. | Accommodation information is successfully created and updated, and changes appear on the website. | TODO | ![US16 Accommodation Management Test](file) | TODO |
| US17 | Administrator | As an administrator, I want to view and modify bookings so that I can manage reservations. | Log in as an administrator and view/edit an existing booking. | The administrator can view and successfully modify booking information. | TODO | ![US17 Booking Management Test](file) | TODO |
| US18 | Administrator | As an administrator, I want to create a booking on behalf of a customer so that I can handle bookings made by phone or in person. | Create a booking through the administration area using a customer account. | A booking is successfully created and linked to the correct customer and accommodation. | TODO | ![US18 Admin Booking Test](file) | TODO |
| US19 | Administrator | As an administrator, I want to set a minimum stay for bookings. | Configure the minimum stay and attempt bookings below and above the minimum. | Bookings below the minimum stay are prevented and valid bookings are accepted. | TODO | ![US19 Minimum Stay Test](file) | TODO |
| US20 | Administrator | As an administrator, I want to manage accommodation images so that website photographs can be updated without changing the code. | Add, edit or remove an accommodation image through the administration area. | Images can be successfully managed and changes are reflected on the website. | TODO | ![US20 Image Management Test](file) | TODO |
| US21 | Administrator | As an administrator, I want to view customer enquiries so that I can respond to potential customers. | Log in to the administration area and open the enquiries section. | Customer enquiries are displayed with the relevant customer and enquiry information. | TODO | ![US21 Enquiry Management Test](file) | TODO |
| US22 | Administrator | As an administrator, I want to view a list of all bookings so that I can monitor upcoming and previous stays. | Open the bookings section within the administration area. | All relevant bookings are displayed with accommodation, customer and date information. | TODO | ![US22 Booking List Test](file) | TODO |
| US23 | Administrator | As an administrator, I want to access a dashboard showing units, upcoming bookings, registered customers, unread enquiries, currently unavailable units and bookings per unit this month so that I can quickly monitor the glampsite. | Log in to the administration area and open the dashboard. | The dashboard displays accurate information for units, upcoming bookings, registered customers, unread enquiries, unavailable units and bookings per unit for the current month. | TODO | ![US23 Dashboard Test](file) | TODO |
| US24 | Administrator | As an administrator, I want to be able to search customers by email or name so that I can quickly find customer information. | Enter a customer's name or email address into the customer search function. | Customers matching the search criteria are displayed. | TODO | ![US24 Customer Search Test](file) | TODO |
| US25 | Administrator | As an administrator, I want each booking to automatically be assigned a unique booking reference number so that bookings can be easily identified. | Create a new booking and view the booking details. | A unique booking reference number is automatically generated and assigned to the booking. | TODO | ![US25 Booking Reference Test](file) | TODO |
| US26 | Administrator | As an administrator, I want to be able to search bookings by booking reference so that I can quickly find a specific reservation. | Enter a valid booking reference into the booking search function. | The booking matching the reference number is displayed. | TODO | ![US26 Booking Search Test](file) | TODO |
| US27 | Administrator | As an administrator, I want to be able to see booking statistics by unit so that I can understand booking trends. | Open the booking statistics section and view statistics for each unit. | Booking statistics are displayed accurately for each accommodation unit. | TODO | ![US27 Booking Statistics Test](file) | TODO |
| US28 | Administrator | As an administrator, I want to be able to temporarily block out dates by unit for maintenance or private use so that unavailable dates cannot be booked. | Block selected dates for a specific accommodation unit and attempt to make a booking for those dates. | The selected dates are shown as unavailable and customers cannot book the unit during the blocked period. | TODO | ![US28 Blocked Dates Test](file) | TODO |
| US29 | Administrator | As an administrator, I want to be able to set different prices for different units and different dates, such as holiday seasons, so that I can manage seasonal pricing. | Configure different prices for units and date periods and check the booking calendar/pricing. | The correct price is displayed for the selected unit and dates. | TODO | ![US29 Seasonal Pricing Test](file) | TODO |
| US30 | Administrator | As an administrator, I want to view registered customers so that I can access and manage customer accounts and contact information. | Open the customer management section. | A list of registered customers is displayed with relevant account and contact information. | TODO | ![US30 Customer Management Test](file) | TODO |
| US31 | Administrator | As an administrator, I want to filter bookings by date, accommodation and status so that I can quickly find specific bookings. | Apply different booking filters. | The booking list updates to display only bookings matching the selected filters. | TODO | ![US31 Booking Filtering Test](file) | TODO |

# Manual Testing – Features

Each major feature was manually tested to ensure that it works as intended across different user roles, devices and scenarios.

| Feature | Test | Expected Result | Actual Result | Screenshot | Pass/Fail |
|---|---|---|---|---|---|
| Navigation | Click each navigation link from the homepage. | Each link directs the user to the correct page or section. | TODO | ![Navigation Test](file) | TODO |
| Responsive Navigation | View the navigation on desktop, tablet and mobile screen sizes. | Navigation remains usable and displays correctly at different screen sizes. | TODO | ![Responsive Navigation Test](file) | TODO |
| Homepage | Load the homepage. | Homepage loads successfully with all content, images and navigation displayed correctly. | TODO | ![Homepage Test](file) | TODO |
| Accommodation Listings | Open the accommodation section. | All three accommodation units are displayed with correct information. | TODO | ![Accommodation Listings Test](file) | TODO |
| Accommodation Details | Select an individual accommodation unit. | The correct accommodation details, facilities, pricing and photographs are displayed. | TODO | ![Accommodation Details Test](file) | TODO |
| Accommodation Images | Open accommodation photographs/gallery. | Images load correctly and are displayed clearly. | TODO | ![Accommodation Images Test](file) | TODO |
| Availability Calendar | Open the availability calendar. | Calendar displays available and unavailable dates correctly. | TODO | ![Availability Calendar Test](file) | TODO |
| Availability Calendar | Select dates containing an existing booking. | Dates that are already booked are shown as unavailable. | TODO | ![Booked Dates Test](file) | TODO |
| Availability Calendar | Select dates outside existing bookings. | Available dates can be selected for booking. | TODO | ![Available Dates Test](file) | TODO |
| Live Pricing | Select different accommodation and dates. | The displayed price updates correctly according to the selected accommodation and dates. | TODO | ![Live Pricing Test](file) | TODO |
| Minimum Stay | Attempt to book fewer nights than the configured minimum stay. | The system prevents the booking and displays an appropriate message. | TODO | ![Minimum Stay Error Test](file) | TODO |
| Minimum Stay | Attempt to book the minimum number of nights. | The booking can proceed successfully. | TODO | ![Minimum Stay Success Test](file) | TODO |
| Booking Validation | Select a departure date before the arrival date. | The system prevents an invalid booking and displays an appropriate error message. | TODO | ![Date Validation Test](file) | TODO |
| Booking Validation | Attempt to book dates that overlap an existing booking. | The system prevents the overlapping booking. | TODO | ![Booking Overlap Test](file) | TODO |
| Customer Registration | Register using valid customer information. | A new customer account is successfully created. | TODO | ![Registration Test](file) | TODO |
| Customer Registration | Attempt to register with invalid or incomplete information. | Validation messages are displayed and the account is not created until valid information is provided. | TODO | ![Registration Validation Test](file) | TODO |
| Customer Login | Log in using valid customer credentials. | Customer is successfully authenticated and redirected to the appropriate page. | TODO | ![Customer Login Test](file) | TODO |
| Customer Login | Attempt to log in using incorrect credentials. | Login fails and an appropriate error message is displayed. | TODO | ![Invalid Login Test](file) | TODO |
| Customer Logout | Select the logout option while logged in. | Customer is securely logged out and redirected appropriately. | TODO | ![Logout Test](file) | TODO |
| Customer Bookings | Log in and open the customer's bookings. | Only the logged-in customer's bookings are displayed. | TODO | ![Customer Bookings Test](file) | TODO |
| Booking Reference | Create a new booking. | A unique booking reference is automatically generated and displayed. | TODO | ![Booking Reference Test](file) | TODO |
| Booking Confirmation | Complete a booking successfully. | Confirmation is displayed with booking details, dates, accommodation and booking reference. | TODO | ![Booking Confirmation Test](file) | TODO |
| Profile Editing | Edit customer profile information. | Updated information is saved and displayed correctly. | TODO | ![Profile Editing Test](file) | TODO |
| Booking Modification Request | Submit a request to modify an existing booking. | The modification request is submitted successfully and confirmation is provided. | TODO | ![Booking Modification Test](file) | TODO |
| Booking Cancellation Request | Submit a request to cancel an existing booking. | The cancellation request is submitted successfully and confirmation is provided. | TODO | ![Booking Cancellation Test](file) | TODO |
| Reviews | Submit a review for an eligible accommodation unit. | Review is successfully submitted and displayed appropriately. | TODO | ![Review Test](file) | TODO |
| Review Images | Upload an image with a review. | The image uploads successfully and is displayed with the review. | TODO | ![Review Image Test](file) | TODO |
| Enquiry Form | Submit an enquiry using valid information. | Enquiry is successfully submitted and confirmation is displayed. | TODO | ![Enquiry Test](file) | TODO |
| Enquiry Validation | Submit the enquiry form with missing or invalid information. | Appropriate validation messages are displayed. | TODO | ![Enquiry Validation Test](file) | TODO |
| Admin Login | Log in using valid administrator credentials. | Administrator is authenticated and can access administrative functionality. | TODO | ![Admin Login Test](file) | TODO |
| Admin Access Control | Attempt to access administrator functionality as a normal customer or visitor. | Unauthorised users are prevented from accessing restricted functionality. | TODO | ![Admin Access Test](file) | TODO |
| Admin Dashboard | Open the administrator dashboard. | Dashboard displays units, upcoming bookings, registered customers, unread enquiries, unavailable units and bookings per unit this month. | TODO | ![Admin Dashboard Test](file) | TODO |
| Add Accommodation | Add a new accommodation unit through the administration area. | New accommodation is successfully created and appears on the website. | TODO | ![Add Accommodation Test](file) | TODO |
| Edit Accommodation | Edit an existing accommodation unit. | Changes are saved and displayed correctly on the website. | TODO | ![Edit Accommodation Test](file) | TODO |
| Manage Images | Add, edit or remove accommodation images through the administration area. | Images are successfully managed and website content updates accordingly. | TODO | ![Manage Images Test](file) | TODO |
| View Bookings | Open the administrator booking list. | Administrator can view relevant customer, accommodation, date and booking information. | TODO | ![View Bookings Test](file) | TODO |
| Modify Bookings | Edit an existing booking as an administrator. | Booking information is successfully updated. | TODO | ![Modify Booking Test](file) | TODO |
| Create Admin Booking | Create a booking on behalf of a customer. | Booking is successfully created and linked to the correct customer and accommodation. | TODO | ![Admin Booking Test](file) | TODO |
| Minimum Stay Settings | Change the minimum stay through the administration area. | The new minimum stay is applied to future booking attempts. | TODO | ![Minimum Stay Settings Test](file) | TODO |
| Customer Search | Search for a customer using their name. | Matching customers are displayed. | TODO | ![Customer Name Search Test](file) | TODO |
| Customer Search | Search for a customer using their email address. | Matching customers are displayed. | TODO | ![Customer Email Search Test](file) | TODO |
| Booking Search | Search for a booking using its booking reference. | The matching booking is displayed. | TODO | ![Booking Search Test](file) | TODO |
| Booking Filtering | Filter bookings by date. | Only bookings matching the selected date criteria are displayed. | TODO | ![Booking Date Filter Test](file) | TODO |
| Booking Filtering | Filter bookings by accommodation. | Only bookings for the selected accommodation are displayed. | TODO | ![Booking Accommodation Filter Test](file) | TODO |
| Booking Filtering | Filter bookings by status. | Only bookings matching the selected status are displayed. | TODO | ![Booking Status Filter Test](file) | TODO |
| Booking Statistics | Open booking statistics by accommodation unit. | Accurate booking statistics are displayed for each unit. | TODO | ![Booking Statistics Test](file) | TODO |
| Blocked Dates | Block dates for a specific accommodation for maintenance or private use. | Selected dates become unavailable for customer bookings. | TODO | ![Blocked Dates Test](file) | TODO |
| Seasonal Pricing | Set different prices for different dates or seasons. | The correct price is displayed for the selected accommodation and dates. | TODO | ![Seasonal Pricing Test](file) | TODO |
| Reminder Emails | Test the customer booking reminder process. | Customer receives a reminder email containing relevant stay information. | TODO | ![Reminder Email Test](file) | TODO |
| Responsive Design | Test the website at desktop, tablet and mobile widths. | Website remains functional, readable and visually consistent at different screen sizes. | TODO | ![Responsive Design Test](file) | TODO |
| Error Handling | Trigger common validation and booking errors. | User receives clear and understandable error messages. | TODO | ![Error Handling Test](file) | TODO |
| 404 Error Page | Navigate to a non-existent page. | A custom 404 page is displayed instead of an unhandled server error. | TODO | ![404 Error Test](file) | TODO |

---

# 🔦 Lighthouse

Google Lighthouse was used to assess the website's performance, accessibility, best practices and SEO.

Testing was carried out on the deployed website.

### Lighthouse Results

![Lighthouse Results](file)

| Category | Score | Notes |
|---|---|---|
| Performance | TODO | TODO |
| Accessibility | TODO | TODO |
| Best Practices | TODO | TODO |
| SEO | TODO | TODO |

### Lighthouse Improvements

Any issues identified through Lighthouse testing were reviewed and improvements were made where appropriate.

Examples may include:

- Optimising image sizes.
- Improving image alt text.
- Improving colour contrast.
- Improving page structure.
- Improving heading hierarchy.
- Removing unnecessary code.
- Improving page loading performance.

---

# 🌐 Browser Compatibility

The website was tested using multiple modern browsers to ensure consistent functionality.

| Browser | Desktop | Mobile | Result |
|---|---|---|---|
| Google Chrome | Tested | Tested | TODO |
| Microsoft Edge | Tested | Tested | TODO |
| Mozilla Firefox | Tested | Tested | TODO |
| Safari | TODO | TODO | TODO |

### Browser Testing Evidence

![Browser Compatibility Testing](file)

---

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

### Desktop

![Desktop Responsive Test](file)

### Tablet

![Tablet Responsive Test](file)

### Mobile

![Mobile Responsive Test](file)

---

# ✅ Code Validation

## HTML Validation

The website was tested using the W3C HTML Validator.

![HTML Validation](file)

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