# Stay Wyld — GitHub Issues

## US01: View Homepage

**Priority:** Must  
**User Type:** Visitor  
**Labels:** `visitor`, `priority-must`

### User Story

As a visitor, I want to view the homepage so that I can understand what the glampsite offers.

### Acceptance Criteria

- Homepage loads successfully.
- Glampsite introduction and key information are displayed.
- Main navigation is clearly visible.
- Visitors can access accommodation information.
- Page is responsive on different screen sizes.
- Images and content display correctly.

### Tasks

- [ ] Create homepage Django view.
- [ ] Create homepage template.
- [ ] Add glampsite introduction and content.
- [ ] Add main navigation.
- [ ] Add accommodation overview and links.
- [ ] Add required images.
- [ ] Add responsive styling.
- [ ] Test on desktop.
- [ ] Test on mobile.
- [ ] Test all navigation links.


## US02: View Accommodation Units

**Priority:** Must  
**User Type:** Visitor  
**Labels:** `visitor`, `priority-must`

### User Story

As a visitor, I want to view the three accommodation units so that I can decide which accommodation is suitable for me.

### Acceptance Criteria

- All three accommodation units are displayed.
- Each unit has its own information.
- Relevant features and amenities are visible.
- Photographs can be viewed.
- Visitors can navigate to availability or booking information.
- Page is responsive.

### Tasks

- [ ] Create accommodation model.
- [ ] Add the three accommodation units.
- [ ] Create accommodation list view.
- [ ] Create accommodation detail view.
- [ ] Create accommodation templates.
- [ ] Add descriptions.
- [ ] Add amenities and features.
- [ ] Add accommodation images.
- [ ] Add availability and booking links.
- [ ] Test all three units.
- [ ] Test responsive layout.


## US03: Submit an Enquiry

**Priority:** Must  
**User Type:** Visitor  
**Labels:** `visitor`, `priority-must`

### User Story

As a visitor, I want to submit an enquiry so that I can ask questions before booking.

### Acceptance Criteria

- Enquiry form is accessible.
- Visitor can enter their contact details and enquiry.
- Required fields are validated.
- Invalid submissions display appropriate errors.
- Valid enquiries are saved.
- Visitor receives confirmation after submission.
- Administrators can access submitted enquiries.

### Tasks

- [ ] Create enquiry model.
- [ ] Create enquiry form.
- [ ] Create enquiry view.
- [ ] Add enquiry URL.
- [ ] Create enquiry template.
- [ ] Add form validation.
- [ ] Save valid enquiries.
- [ ] Add confirmation message.
- [ ] Add enquiries to Django admin.
- [ ] Test valid submission.
- [ ] Test invalid submission.


## US04: View Availability and Prices

**Priority:** Must  
**User Type:** Visitor  
**Labels:** `visitor`, `priority-must`

### User Story

As a visitor, I want to see a calendar showing availability and nightly prices.

### Acceptance Criteria

- Visitor can select an accommodation.
- An availability calendar is displayed.
- Unavailable dates are clearly identified.
- Nightly prices are displayed.
- Prices reflect selected dates where applicable.
- Availability reflects existing bookings.
- Availability reflects administrator-blocked dates.

### Tasks

- [ ] Design availability calendar.
- [ ] Retrieve existing bookings.
- [ ] Retrieve blocked dates.
- [ ] Retrieve applicable prices.
- [ ] Display available dates.
- [ ] Display unavailable dates.
- [ ] Display nightly prices.
- [ ] Connect calendar to accommodation selection.
- [ ] Prevent unavailable dates from being selected.
- [ ] Test booked dates.
- [ ] Test blocked dates.
- [ ] Test seasonal pricing.


## US05: View Accommodation Photographs

**Priority:** Should  
**User Type:** Visitor  
**Labels:** `visitor`, `priority-should`

### User Story

As a visitor, I want to view accommodation photographs so that I can understand what the units and site look like.

### Acceptance Criteria

- Visitors can view photographs for each accommodation unit.
- Images are clear and appropriately sized.
- Images have appropriate alternative text.
- Images are optimised for website performance.
- Images can be updated without changing website code.

### Tasks

- [ ] Set up image storage.
- [ ] Configure Cloudinary.
- [ ] Add accommodation image fields.
- [ ] Upload initial photographs.
- [ ] Display photographs on accommodation pages.
- [ ] Add appropriate alt text.
- [ ] Test image loading.
- [ ] Test images on mobile.
- [ ] Test administrator image management.


## US06: Register for an Account

**Priority:** Must  
**User Type:** Customer  
**Labels:** `customer`, `priority-must`

### User Story

As a customer, I want to register for an account so that I can book online.

### Acceptance Criteria

- Customer can access the registration page.
- Customer can enter all required information.
- Required fields are validated.
- Duplicate accounts are handled appropriately.
- Password requirements are enforced.
- Passwords are securely stored.
- Successful registration creates a customer account.
- Customer receives appropriate confirmation.

### Tasks

- [ ] Configure Django authentication.
- [ ] Create registration form.
- [ ] Create registration view.
- [ ] Create registration template.
- [ ] Add validation.
- [ ] Handle duplicate users.
- [ ] Configure password validation.
- [ ] Add registration URL.
- [ ] Test successful registration.
- [ ] Test invalid registration.
- [ ] Test duplicate registration.


## US07: Customer Login

**Priority:** Must  
**User Type:** Customer  
**Labels:** `customer`, `priority-must`

### User Story

As a registered customer, I want to log in securely so that I can access my account and see my bookings.

### Acceptance Criteria

- Registered customers can log in.
- Invalid credentials are rejected.
- Passwords are not displayed or stored insecurely.
- Successful login provides access to customer functionality.
- Customers can log out.
- Protected pages cannot be accessed by unauthenticated users.

### Tasks

- [ ] Configure Django login.
- [ ] Create login template.
- [ ] Add login URL.
- [ ] Configure logout.
- [ ] Protect customer views.
- [ ] Add appropriate error messages.
- [ ] Test valid login.
- [ ] Test invalid login.
- [ ] Test logout.
- [ ] Test unauthorised access.


## US08: Book an Available Unit

**Priority:** Must  
**User Type:** Customer  
**Labels:** `customer`, `priority-must`

### User Story

As a customer, I want to book an available unit so that I can arrange my stay.

### Acceptance Criteria

- Customer must be logged in to make a booking.
- Customer can select an accommodation unit.
- Customer can select arrival and departure dates.
- Only available dates can be selected.
- Overlapping bookings cannot be created.
- Minimum stay requirement of two nights is enforced.
- Booking is saved to the database.
- Customer receives booking confirmation.
- Booking receives a unique reference number.

### Tasks

- [ ] Create booking model.
- [ ] Create booking form.
- [ ] Create booking view.
- [ ] Add accommodation selection.
- [ ] Add arrival and departure dates.
- [ ] Implement availability checking.
- [ ] Implement two-night minimum stay.
- [ ] Prevent overlapping bookings.
- [ ] Calculate booking price.
- [ ] Generate booking reference.
- [ ] Save booking.
- [ ] Display booking confirmation.
- [ ] Test valid booking.
- [ ] Test overlapping booking.
- [ ] Test minimum stay validation.


## US09: View Live Prices

**Priority:** Must  
**User Type:** Customer  
**Labels:** `customer`, `priority-must`

### User Story

As a customer, I want to see live prices for my selected dates.

### Acceptance Criteria

- Customer can select booking dates.
- Applicable nightly price is displayed.
- Seasonal/date-specific pricing is applied where applicable.
- Total booking price is displayed.
- Price updates when dates change.
- Price calculation is performed server-side.

### Tasks

- [ ] Create pricing model or pricing structure.
- [ ] Add seasonal pricing.
- [ ] Create price calculation logic.
- [ ] Calculate number of nights.
- [ ] Calculate booking total.
- [ ] Display nightly prices.
- [ ] Display booking total.
- [ ] Connect pricing to booking form.
- [ ] Add server-side validation.
- [ ] Test different date ranges.
- [ ] Test seasonal prices.


## US10: View My Bookings

**Priority:** Should  
**User Type:** Customer  
**Labels:** `customer`, `priority-should`

### User Story

As a customer, I want to view my bookings so that I can check my upcoming stays along with balances paid and outstanding.

### Acceptance Criteria

- Logged-in customers can view their bookings.
- Customers can only see their own bookings.
- Upcoming and previous bookings can be identified.
- Booking dates are displayed.
- Accommodation is displayed.
- Booking reference is displayed.
- Amount paid and outstanding balance are displayed.

### Tasks

- [ ] Create customer booking view.
- [ ] Create booking history template.
- [ ] Filter bookings by logged-in customer.
- [ ] Display booking details.
- [ ] Display booking reference.
- [ ] Display payment information.
- [ ] Separate upcoming and previous bookings.
- [ ] Test customer data isolation.
- [ ] Test booking information display.


## US11: Request Booking Modification or Cancellation

**Priority:** Should  
**User Type:** Customer  
**Labels:** `customer`, `priority-should`

### User Story

As a customer, I want to be able to request to modify or cancel a booking online.

### Acceptance Criteria

- Customer can request a booking modification.
- Customer can request a booking cancellation.
- Customer can provide relevant details.
- Request is associated with the correct booking.
- Administrator can view the request.
- Customer receives confirmation that the request has been submitted.

### Tasks

- [ ] Design modification/cancellation workflow.
- [ ] Create booking request model.
- [ ] Create request form.
- [ ] Create request view.
- [ ] Add modification/cancellation buttons.
- [ ] Add requests to administrator interface.
- [ ] Add request status.
- [ ] Add confirmation message.
- [ ] Test modification request.
- [ ] Test cancellation request.


## US12: Post a Review

**Priority:** Could  
**User Type:** Customer  
**Labels:** `customer`, `priority-could`

### User Story

As a customer, I would like to post a review of my glamping unit along with pictures.

### Acceptance Criteria

- Customer can submit a review after their stay.
- Customer can provide a rating.
- Customer can provide written feedback.
- Review is associated with the correct accommodation.
- Customer can upload photographs.
- Review submissions are validated.
- Administrator can manage submitted reviews.

### Tasks

- [ ] Create review model.
- [ ] Create review form.
- [ ] Add rating field.
- [ ] Add review text.
- [ ] Add image upload.
- [ ] Restrict reviews to eligible customers.
- [ ] Display approved reviews.
- [ ] Add review management to admin.
- [ ] Test review submission.
- [ ] Test image upload.


## US13: Edit Customer Profile

**Priority:** Could  
**User Type:** Customer  
**Labels:** `customer`, `priority-could`

### User Story

As a customer, I want to be able to edit my profile details so that my information remains up to date.

### Acceptance Criteria

- Logged-in customers can access their profile.
- Customers can edit permitted information.
- Profile information is validated.
- Changes are saved to the correct account.
- Customers cannot edit another customer's information.

### Tasks

- [ ] Create profile view.
- [ ] Create profile form.
- [ ] Create profile template.
- [ ] Add validation.
- [ ] Save updated information.
- [ ] Restrict profile access.
- [ ] Test profile editing.
- [ ] Test account security.


## US14: Receive Stay Reminder Emails

**Priority:** Could  
**User Type:** Customer  
**Labels:** `customer`, `priority-could`

### User Story

As a customer, I would like to receive reminder emails before my stay with any helpful information.

### Acceptance Criteria

- Customers with upcoming bookings receive reminder emails.
- Emails are sent at the appropriate time before the stay.
- Emails contain relevant booking information.
- Customer email addresses are validated.
- Email delivery failures are handled appropriately.

### Tasks

- [ ] Configure email service.
- [ ] Create reminder email template.
- [ ] Create reminder logic.
- [ ] Identify upcoming bookings.
- [ ] Schedule reminder emails.
- [ ] Include booking information.
- [ ] Test email content.
- [ ] Test email delivery.


## US15: Administrator Login

**Priority:** Must  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-must`

### User Story

As an administrator, I want to securely log in so that I can manage the website.

### Acceptance Criteria

- Administrators can securely log in.
- Administrator functionality is protected.
- Customers cannot access administrator functionality.
- Invalid credentials are rejected.
- Administrators can log out.

### Tasks

- [ ] Configure administrator authentication.
- [ ] Configure staff/superuser permissions.
- [ ] Protect administrator pages.
- [ ] Configure administrator URLs.
- [ ] Test administrator login.
- [ ] Test invalid credentials.
- [ ] Test customer access restrictions.
- [ ] Test logout.


## US16: Manage Accommodation Units

**Priority:** Must  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-must`

### User Story

As an administrator, I want to add and edit accommodation units so that the website information remains up to date.

### Acceptance Criteria

- Administrator can create accommodation units.
- Administrator can edit accommodation units.
- Required fields are validated.
- Changes are saved to the database.
- Updated information appears on the website.
- Administrator can manage all three units.

### Tasks

- [ ] Create accommodation model.
- [ ] Configure Django admin.
- [ ] Add required accommodation fields.
- [ ] Create accommodation records.
- [ ] Implement create functionality.
- [ ] Implement edit functionality.
- [ ] Add validation.
- [ ] Test creating an accommodation.
- [ ] Test editing an accommodation.
- [ ] Test updated information on website.


## US17: Manage Bookings

**Priority:** Must  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-must`

### User Story

As an administrator, I want to view and modify bookings so that I can manage reservations.

### Acceptance Criteria

- Administrator can view bookings.
- Booking details are clearly displayed.
- Administrator can modify permitted booking details.
- Changes are saved correctly.
- Availability is revalidated after changes.
- Customer information is handled securely.

### Tasks

- [ ] Configure booking administration.
- [ ] Display booking details.
- [ ] Add booking editing.
- [ ] Validate booking changes.
- [ ] Recheck availability after changes.
- [ ] Test viewing bookings.
- [ ] Test editing bookings.
- [ ] Test availability validation.


## US18: Create Booking on Behalf of Customer

**Priority:** Must  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-must`

### User Story

As an administrator, I want to create a booking on behalf of a customer so that I can handle bookings made by phone or in person.

### Acceptance Criteria

- Administrator can select or create a customer.
- Administrator can select an accommodation unit.
- Administrator can select arrival and departure dates.
- Availability rules are enforced.
- Minimum stay requirement is enforced.
- Booking is associated with the correct customer.
- Booking receives a unique reference.

### Tasks

- [ ] Add administrator booking functionality.
- [ ] Add customer selection.
- [ ] Add accommodation selection.
- [ ] Add arrival and departure dates.
- [ ] Reuse availability validation.
- [ ] Apply minimum stay requirement.
- [ ] Calculate booking price.
- [ ] Generate booking reference.
- [ ] Save booking.
- [ ] Test administrator-created booking.


## US19: Set Minimum Stay

**Priority:** Must  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-must`

### User Story

As an administrator, I want to set a minimum stay for bookings.

### Acceptance Criteria

- Administrator can configure the minimum stay.
- Booking system applies the configured minimum stay.
- Customers cannot book below the minimum.
- Validation is performed server-side.
- Administrator-created bookings also follow the minimum stay.

### Tasks

- [ ] Create minimum-stay setting.
- [ ] Add administrator control.
- [ ] Add booking validation.
- [ ] Apply validation to customer bookings.
- [ ] Apply validation to administrator bookings.
- [ ] Add appropriate validation message.
- [ ] Test minimum stay validation.


## US20: Manage Accommodation Images

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to manage accommodation images so that website photographs can be updated without changing the code.

### Acceptance Criteria

- Administrator can upload accommodation images.
- Administrator can replace images.
- Administrator can remove images.
- Images are associated with the correct accommodation.
- Updated images appear on the website.
- Images use appropriate production storage.

### Tasks

- [ ] Configure Cloudinary.
- [ ] Create image model or image fields.
- [ ] Implement image uploads.
- [ ] Add image management to admin.
- [ ] Implement image replacement.
- [ ] Implement image removal.
- [ ] Display images on website.
- [ ] Test image management.


## US21: View Customer Enquiries

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to view customer enquiries so that I can respond to potential customers.

### Acceptance Criteria

- Administrator can view submitted enquiries.
- Customer contact information is displayed.
- Enquiry date is displayed.
- Enquiry content is displayed.
- Enquiries can be identified as read or unread.

### Tasks

- [ ] Create enquiry model.
- [ ] Add enquiries to administrator interface.
- [ ] Display customer details.
- [ ] Display enquiry content.
- [ ] Add read/unread status.
- [ ] Display enquiry date.
- [ ] Test enquiry management.


## US22: View All Bookings

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to view a list of all bookings so that I can monitor upcoming and previous stays.

### Acceptance Criteria

- Administrator can view all bookings.
- Upcoming and previous bookings can be identified.
- Booking reference is displayed.
- Accommodation is displayed.
- Customer is displayed.
- Booking status is displayed.

### Tasks

- [ ] Create administrator booking list.
- [ ] Display booking reference.
- [ ] Display customer.
- [ ] Display accommodation.
- [ ] Display booking dates.
- [ ] Display booking status.
- [ ] Display booking total.
- [ ] Test booking list.


## US23: View Administrator Dashboard

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to access a dashboard showing units, upcoming bookings, registered customers, unread enquiries, currently unavailable units and bookings per unit this month so that I can quickly monitor the glampsite.

### Acceptance Criteria

- Dashboard displays accommodation units.
- Dashboard displays upcoming bookings.
- Dashboard displays registered customers.
- Dashboard displays unread enquiries.
- Dashboard displays currently unavailable units.
- Dashboard displays bookings per unit for the current month.
- Dashboard information reflects current database data.

### Tasks

- [ ] Create dashboard view.
- [ ] Create dashboard template.
- [ ] Display accommodation count/list.
- [ ] Display upcoming bookings.
- [ ] Display customer count.
- [ ] Display unread enquiry count.
- [ ] Display unavailable units.
- [ ] Calculate bookings per unit.
- [ ] Add dashboard navigation.
- [ ] Test dashboard calculations.
- [ ] Test responsive dashboard layout.


## US24: Search Customers

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to be able to search customers by email or name so that I can quickly find customer information.

### Acceptance Criteria

- Administrator can search by customer name.
- Administrator can search by email address.
- Matching customers are displayed.
- Partial matches are supported.
- Customer search is restricted to administrators.

### Tasks

- [ ] Create customer search view.
- [ ] Create search form.
- [ ] Add name search.
- [ ] Add email search.
- [ ] Implement partial matching.
- [ ] Display search results.
- [ ] Restrict search to administrators.
- [ ] Test name search.
- [ ] Test email search.
- [ ] Test partial matching.


## US25: Generate Unique Booking Reference

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want each booking to automatically be assigned a unique booking reference number so that bookings can be easily identified.

### Acceptance Criteria

- Every booking receives a booking reference.
- Booking references are unique.
- References are generated automatically.
- Reference is stored with the booking.
- Reference is displayed to customers.
- Reference is displayed to administrators.

### Tasks

- [ ] Define booking reference format.
- [ ] Implement reference generation.
- [ ] Add database uniqueness constraint.
- [ ] Generate reference when booking is created.
- [ ] Display reference to customers.
- [ ] Display reference to administrators.
- [ ] Test reference uniqueness.
- [ ] Test administrator-created bookings.


## US26: Search Bookings by Reference

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to be able to search bookings by booking reference so that I can quickly find a specific reservation.

### Acceptance Criteria

- Administrator can enter a booking reference.
- Matching booking is displayed.
- Appropriate message is displayed when no booking is found.
- Correct booking information is displayed.
- Search is restricted to administrators.

### Tasks

- [ ] Create booking search form.
- [ ] Create search view.
- [ ] Implement booking reference lookup.
- [ ] Display matching booking.
- [ ] Add no-results handling.
- [ ] Restrict search to administrators.
- [ ] Test valid reference.
- [ ] Test invalid reference.


## US27: View Booking Statistics by Unit

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to be able to see booking statistics by unit so that I can understand booking trends.

### Acceptance Criteria

- Administrator can view booking statistics.
- Statistics are separated by accommodation unit.
- Statistics use current database data.
- Relevant time periods can be analysed.
- Statistics are presented clearly.

### Tasks

- [ ] Determine required booking statistics.
- [ ] Query booking data.
- [ ] Calculate bookings per unit.
- [ ] Calculate relevant totals.
- [ ] Create statistics view.
- [ ] Create statistics template.
- [ ] Add charts if appropriate.
- [ ] Test calculations.
- [ ] Test statistics for each accommodation.


## US28: Block Dates for Maintenance or Private Use

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to be able to temporarily block out dates by unit for maintenance or private use so that unavailable dates cannot be booked.

### Acceptance Criteria

- Administrator can select an accommodation unit.
- Administrator can specify blocked dates.
- Blocked dates cannot be booked by customers.
- Blocked dates are shown in the availability calendar.
- Existing bookings are not overwritten.
- Administrator can remove or update a date block.

### Tasks

- [ ] Create blocked-date model.
- [ ] Add accommodation relationship.
- [ ] Add start and end dates.
- [ ] Add administrator controls.
- [ ] Integrate blocked dates into availability logic.
- [ ] Display blocked dates on calendar.
- [ ] Prevent bookings during blocked dates.
- [ ] Implement editing of blocked dates.
- [ ] Implement deletion of blocked dates.
- [ ] Test date blocking.


## US29: Manage Seasonal and Unit Pricing

**Priority:** Should  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-should`

### User Story

As an administrator, I want to be able to set different prices for different units and different dates, such as holiday seasons, so that I can manage seasonal pricing.

### Acceptance Criteria

- Administrator can create pricing periods.
- Pricing periods can be associated with an accommodation unit.
- Different dates can have different nightly prices.
- Seasonal prices are applied automatically.
- Booking totals use the correct applicable price.
- Existing completed bookings are not incorrectly altered.

### Tasks

- [ ] Create pricing model.
- [ ] Add accommodation relationship.
- [ ] Add pricing start and end dates.
- [ ] Add nightly price.
- [ ] Add pricing management to admin.
- [ ] Implement applicable-price lookup.
- [ ] Integrate pricing with booking calculation.
- [ ] Handle overlapping pricing periods.
- [ ] Test standard pricing.
- [ ] Test seasonal pricing.
- [ ] Test different unit pricing.


## US30: View Registered Customers

**Priority:** Could  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-could`

### User Story

As an administrator, I want to view registered customers so that I can access and manage customer accounts and contact information.

### Acceptance Criteria

- Administrator can view registered customers.
- Customer names and contact information are displayed.
- Administrator can view individual customer information.
- Customer management is restricted to administrators.
- Customer passwords are never displayed.

### Tasks

- [ ] Create customer management view.
- [ ] Create customer list.
- [ ] Display customer contact information.
- [ ] Create customer detail view.
- [ ] Restrict access to administrators.
- [ ] Ensure passwords are never displayed.
- [ ] Test customer list.
- [ ] Test customer details.
- [ ] Test access restrictions.


## US31: Filter Bookings

**Priority:** Could  
**User Type:** Administrator  
**Labels:** `administrator`, `priority-could`

### User Story

As an administrator, I want to filter bookings by date, accommodation and status so that I can quickly find specific bookings.

### Acceptance Criteria

- Administrator can filter bookings by date.
- Administrator can filter bookings by accommodation.
- Administrator can filter bookings by status.
- Filters can be used individually.
- Filters can be combined.
- Results match the selected filters.
- Administrator can clear or reset filters.

### Tasks

- [ ] Create booking filter form.
- [ ] Add date filter.
- [ ] Add accommodation filter.
- [ ] Add status filter.
- [ ] Implement combined filtering.
- [ ] Display filtered results.
- [ ] Add reset/clear filters.
- [ ] Test date filtering.
- [ ] Test accommodation filtering.
- [ ] Test status filtering.
- [ ] Test combined filters.
- [ ] Test clearing filters.


# Won't Have in Version 1

## Online Payments

**Priority:** Won't Have

### Reason

Online payments are excluded from Version 1 because they introduce significant additional complexity and are outside the core requirements for the initial project.

### Future Consideration

- [ ] Research suitable payment provider.
- [ ] Consider payment security requirements.
- [ ] Consider deposits and outstanding balances.
- [ ] Consider payment confirmation.
- [ ] Consider refunds.
- [ ] Consider integration with the booking system.