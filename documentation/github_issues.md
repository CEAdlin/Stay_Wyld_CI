## US01: View Homepage

Priority: Must
User Type: Visitor
Labels: visitor, priority-must

### User Story

As a visitor, I want to view the homepage so that I can understand what Stay Wyld offers.

### Acceptance Criteria

- The homepage displays the Stay Wyld branding.
- The homepage explains the glamping experience.
- The homepage provides clear navigation to key areas of the website.
- The homepage is responsive on mobile, tablet and desktop devices.

### Tasks

- [ ] Create homepage template.
- [ ] Add Stay Wyld branding.
- [ ] Add introductory content.
- [ ] Add navigation.
- [ ] Make the homepage responsive.


## US02: View Accommodation Units

Priority: Must
User Type: Visitor
Labels: visitor, priority-must

### User Story

As a visitor, I want to view the available accommodation units so that I can choose somewhere suitable to stay.

### Acceptance Criteria

- Visitors can view all available accommodation units.
- Each unit displays its name and description.
- Each unit displays its key features.
- Visitors can select a unit to view more information.

### Tasks

- [ ] Create accommodation model.
- [ ] Create accommodation listing page.
- [ ] Create accommodation detail page.
- [ ] Add accommodation descriptions.
- [ ] Add accommodation features.


## US03: Submit an Enquiry

Priority: Must
User Type: Visitor
Labels: visitor, priority-must

### User Story

As a visitor, I want to submit an enquiry so that I can ask questions before booking.

### Acceptance Criteria

- Visitors can access an enquiry form.
- The form collects the visitor's name.
- The form collects an email address.
- The form allows the visitor to enter a message.
- The enquiry is submitted successfully.
- The administrator can access submitted enquiries.

### Tasks

- [ ] Create enquiry model.
- [ ] Create enquiry form.
- [ ] Create enquiry view.
- [ ] Create enquiry template.
- [ ] Add form validation.
- [ ] Store submitted enquiries.


## US04: View Availability and Prices

Priority: Must
User Type: Visitor
Labels: visitor, priority-must

### User Story

As a visitor, I want to view accommodation availability and prices so that I can decide when and where to stay.

### Acceptance Criteria

- Visitors can select arrival and departure dates.
- Available accommodation is displayed.
- Unavailable accommodation is clearly identified.
- Prices are displayed for available accommodation.
- The displayed price reflects the selected dates.

### Tasks

- [ ] Create availability logic.
- [ ] Create date selection form.
- [ ] Connect availability to bookings.
- [ ] Calculate accommodation prices.
- [ ] Display availability results.


## US05: View Accommodation Photographs

Priority: Should
User Type: Visitor
Labels: visitor, priority-should

### User Story

As a visitor, I want to view photographs of the accommodation so that I can see what the accommodation looks like before booking.

### Acceptance Criteria

- Each accommodation unit has photographs.
- Photographs are displayed clearly.
- Visitors can view multiple photographs.
- Images include appropriate alternative text.
- Images are optimised for website performance.

### Tasks

- [ ] Add image fields to accommodation model.
- [ ] Create accommodation image gallery.
- [ ] Add photographs.
- [ ] Add alternative text.
- [ ] Optimise image sizes.


## US06: Register for an Account

Priority: Must
User Type: Customer
Labels: customer, priority-must

### User Story

As a customer, I want to register for an account so that I can manage my bookings.

### Acceptance Criteria

- Customers can access a registration form.
- Customers can provide the required account information.
- Email addresses must be unique.
- Password requirements are enforced.
- Customers receive confirmation that registration was successful.

### Tasks

- [ ] Configure Django authentication.
- [ ] Create registration form.
- [ ] Create registration view.
- [ ] Create registration template.
- [ ] Add form validation.
- [ ] Test registration.


## US07: Customer Login

Priority: Must
User Type: Customer
Labels: customer, priority-must

### User Story

As a customer, I want to log in to my account so that I can access my bookings and personal information.

### Acceptance Criteria

- Customers can access a login form.
- Customers can log in using their credentials.
- Invalid credentials display an appropriate error.
- Successful login redirects the customer to their account area.
- Customers can log out.

### Tasks

- [ ] Create login view.
- [ ] Create login template.
- [ ] Configure authentication URLs.
- [ ] Add logout functionality.
- [ ] Test successful login.
- [ ] Test unsuccessful login.


## US08: Book an Available Unit

Priority: Must
User Type: Customer
Labels: customer, priority-must

### User Story

As a customer, I want to book an available accommodation unit so that I can reserve my stay.

### Acceptance Criteria

- Customers can select an available accommodation unit.
- Customers can select arrival and departure dates.
- The system checks availability before confirming a booking.
- The total booking price is displayed.
- A booking is created after successful confirmation.
- The customer receives confirmation of the booking.

### Tasks

- [ ] Create booking model.
- [ ] Create booking form.
- [ ] Create booking view.
- [ ] Check accommodation availability.
- [ ] Calculate total booking price.
- [ ] Generate booking reference.
- [ ] Display booking confirmation.


## US09: View Live Prices

Priority: Must
User Type: Customer
Labels: customer, priority-must

### User Story

As a customer, I want to see the current price for my selected dates so that I know how much my stay will cost.

### Acceptance Criteria

- Customers can select their dates.
- The system calculates the correct price.
- Seasonal pricing is applied where applicable.
- The correct accommodation price is displayed.
- The total price is clearly shown.

### Tasks

- [ ] Create pricing model.
- [ ] Add seasonal pricing logic.
- [ ] Connect pricing to accommodation.
- [ ] Calculate prices based on dates.
- [ ] Display total price.


## US10: View My Bookings

Priority: Should
User Type: Customer
Labels: customer, priority-should

### User Story

As a customer, I want to view my bookings so that I can keep track of my upcoming and previous stays.

### Acceptance Criteria

- Customers can access their bookings.
- Customers can see upcoming bookings.
- Customers can see previous bookings.
- Booking dates are displayed.
- Accommodation details are displayed.
- Booking status is displayed.

### Tasks

- [ ] Create customer booking view.
- [ ] Create booking list template.
- [ ] Filter bookings by customer.
- [ ] Display booking information.
- [ ] Test booking history.


## US11: Request Booking Modification or Cancellation

Priority: Should
User Type: Customer
Labels: customer, priority-should

### User Story

As a customer, I want to request a booking modification or cancellation so that I can change my plans.

### Acceptance Criteria

- Customers can select an existing booking.
- Customers can request a booking change.
- Customers can request a cancellation.
- The request is recorded.
- The administrator can view the request.
- The customer receives confirmation that the request was submitted.

### Tasks

- [ ] Create modification request model.
- [ ] Create cancellation request functionality.
- [ ] Create modification form.
- [ ] Store requests.
- [ ] Display request status.
- [ ] Notify administrator.


## US12: Post a Review

Priority: Could
User Type: Customer
Labels: customer, priority-could

### User Story

As a customer, I want to post a review after my stay so that I can share my experience with other visitors.

### Acceptance Criteria

- Customers can submit a review.
- Customers can provide a rating.
- Customers can provide written feedback.
- Reviews are associated with the relevant accommodation.
- Only customers who have completed a stay can submit a review.

### Tasks

- [ ] Create review model.
- [ ] Create review form.
- [ ] Create review view.
- [ ] Connect reviews to accommodation.
- [ ] Validate customer eligibility.
- [ ] Display approved reviews.


## US13: Edit Customer Profile

Priority: Could
User Type: Customer
Labels: customer, priority-could

### User Story

As a customer, I want to edit my profile so that my personal information remains up to date.

### Acceptance Criteria

- Customers can access their profile.
- Customers can update their personal information.
- Customers can update their email address.
- Customers can save changes.
- Updated information is displayed correctly.

### Tasks

- [ ] Create customer profile view.
- [ ] Create profile form.
- [ ] Add profile template.
- [ ] Add form validation.
- [ ] Test profile updates.


## US14: Receive Stay Reminder Emails

Priority: Could
User Type: Customer
Labels: customer, priority-could

### User Story

As a customer, I want to receive a reminder before my stay so that I do not forget my booking details.

### Acceptance Criteria

- Customers receive a reminder before their stay.
- The reminder contains the booking reference.
- The reminder contains accommodation details.
- The reminder contains arrival and departure dates.
- The reminder is sent automatically.

### Tasks

- [ ] Configure email functionality.
- [ ] Create reminder email template.
- [ ] Create reminder scheduling logic.
- [ ] Include booking information.
- [ ] Test reminder emails.


## US15: Administrator Login

Priority: Must
User Type: Administrator
Labels: administrator, priority-must

### User Story

As an administrator, I want to log in securely so that I can manage the website and bookings.

### Acceptance Criteria

- Administrators can access the administrator login.
- Administrators can log in using secure credentials.
- Invalid credentials are rejected.
- Only authorised administrators can access administrator functions.
- Administrators can log out.

### Tasks

- [ ] Configure administrator authentication.
- [ ] Create administrator login.
- [ ] Restrict administrator views.
- [ ] Add logout functionality.
- [ ] Test administrator permissions.


## US16: Manage Accommodation Units

Priority: Must
User Type: Administrator
Labels: administrator, priority-must

### User Story

As an administrator, I want to manage accommodation units so that I can keep the website information accurate.

### Acceptance Criteria

- Administrators can create accommodation units.
- Administrators can edit accommodation units.
- Administrators can delete accommodation units.
- Administrators can update descriptions.
- Administrators can update accommodation features.
- Changes are reflected on the website.

### Tasks

- [ ] Create accommodation model.
- [ ] Create administrator accommodation list.
- [ ] Create accommodation form.
- [ ] Add create functionality.
- [ ] Add edit functionality.
- [ ] Add delete functionality.


## US17: Manage Bookings

Priority: Must
User Type: Administrator
Labels: administrator, priority-must

### User Story

As an administrator, I want to manage bookings so that I can keep booking information accurate.

### Acceptance Criteria

- Administrators can view bookings.
- Administrators can create bookings.
- Administrators can edit bookings.
- Administrators can cancel bookings.
- Administrators can update booking status.
- Changes are saved correctly.

### Tasks

- [ ] Create administrator booking list.
- [ ] Create booking management form.
- [ ] Add create functionality.
- [ ] Add edit functionality.
- [ ] Add cancellation functionality.
- [ ] Add booking status management.


## US18: Create Booking on Behalf of Customer

Priority: Must
User Type: Administrator
Labels: administrator, priority-must

### User Story

As an administrator, I want to create a booking on behalf of a customer so that I can process bookings received through other channels.

### Acceptance Criteria

- Administrators can select an existing customer.
- Administrators can select accommodation.
- Administrators can select booking dates.
- The system checks availability.
- The booking is stored against the selected customer.
- A booking reference is generated.

### Tasks

- [ ] Create administrator booking form.
- [ ] Add customer selection.
- [ ] Add accommodation selection.
- [ ] Add availability checking.
- [ ] Generate booking reference.
- [ ] Test administrator bookings.


## US19: Set Minimum Stay

Priority: Must
User Type: Administrator
Labels: administrator, priority-must

### User Story

As an administrator, I want to set a minimum stay requirement so that I can control booking lengths.

### Acceptance Criteria

- Administrators can set a minimum number of nights.
- The minimum stay can be changed.
- The minimum stay applies to new bookings.
- Customers cannot book fewer nights than the minimum requirement.
- The system displays an appropriate message when the requirement is not met.

### Tasks

- [ ] Add minimum stay field.
- [ ] Add minimum stay validation.
- [ ] Apply minimum stay to booking forms.
- [ ] Display validation message.
- [ ] Test minimum stay rules.


## US20: Manage Accommodation Images

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to manage accommodation images so that visitors can see up-to-date photographs.

### Acceptance Criteria

- Administrators can upload images.
- Administrators can associate images with an accommodation.
- Administrators can delete images.
- Administrators can update image descriptions.
- Images are displayed on the accommodation page.

### Tasks

- [ ] Create accommodation image model.
- [ ] Add image upload functionality.
- [ ] Add image management view.
- [ ] Add image deletion functionality.
- [ ] Add image descriptions.
- [ ] Test image management.


## US21: View Customer Enquiries

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to view customer enquiries so that I can respond to visitor questions.

### Acceptance Criteria

- Administrators can access submitted enquiries.
- Enquiries display the customer's name.
- Enquiries display the customer's email address.
- Enquiries display the message.
- Enquiries display the submission date.
- Administrators can mark enquiries as handled.

### Tasks

- [ ] Create enquiry management view.
- [ ] Create enquiry list template.
- [ ] Display enquiry details.
- [ ] Add enquiry status.
- [ ] Add handled functionality.


## US22: View All Bookings

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to view all bookings so that I can monitor reservations across the business.

### Acceptance Criteria

- Administrators can view all bookings.
- Bookings display customer information.
- Bookings display accommodation information.
- Bookings display dates.
- Bookings display booking status.
- Bookings can be sorted by relevant information.

### Tasks

- [ ] Create all bookings view.
- [ ] Create bookings table.
- [ ] Display customer information.
- [ ] Display accommodation information.
- [ ] Display booking dates.
- [ ] Add sorting functionality.


## US23: View Administrator Dashboard

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to view a dashboard so that I can quickly understand the current state of the business.

### Acceptance Criteria

- Administrators can access the dashboard.
- The dashboard displays current bookings.
- The dashboard displays upcoming stays.
- The dashboard displays relevant business statistics.
- The dashboard provides links to key management areas.

### Tasks

- [ ] Create administrator dashboard.
- [ ] Add booking statistics.
- [ ] Add upcoming booking information.
- [ ] Add dashboard navigation.
- [ ] Style dashboard.
- [ ] Test dashboard.


## US24: Search Customers

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to search customers so that I can quickly find a specific customer.

### Acceptance Criteria

- Administrators can search by customer name.
- Administrators can search by email address.
- Matching customers are displayed.
- Customers with no matching results are handled appropriately.

### Tasks

- [ ] Create customer search form.
- [ ] Add search functionality.
- [ ] Display search results.
- [ ] Add no-results message.
- [ ] Test customer searches.


## US25: Generate Unique Booking Reference

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want each booking to have a unique reference so that bookings can be easily identified.

### Acceptance Criteria

- Each booking receives a unique reference.
- References are generated automatically.
- References are stored with the booking.
- References are displayed to customers.
- References are displayed to administrators.

### Tasks

- [ ] Add booking reference field.
- [ ] Create reference generation logic.
- [ ] Ensure references are unique.
- [ ] Display references on booking pages.
- [ ] Test reference generation.


## US26: Search Bookings by Reference

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to search bookings by reference so that I can quickly find a specific booking.

### Acceptance Criteria

- Administrators can enter a booking reference.
- The system searches booking references.
- Matching bookings are displayed.
- No matching booking results are handled appropriately.

### Tasks

- [ ] Create booking search form.
- [ ] Add booking reference search.
- [ ] Display matching booking.
- [ ] Add no-results message.
- [ ] Test booking reference searches.


## US27: View Booking Statistics by Unit

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to view booking statistics by accommodation unit so that I can understand which units are performing best.

### Acceptance Criteria

- Administrators can view booking statistics.
- Statistics can be viewed by accommodation unit.
- The number of bookings is displayed.
- Relevant booking information is calculated accurately.
- Statistics are easy to understand.

### Tasks

- [ ] Create statistics view.
- [ ] Calculate bookings by accommodation.
- [ ] Display statistics.
- [ ] Add suitable visual presentation.
- [ ] Test statistics calculations.


## US28: Block Dates for Maintenance or Private Use

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to block dates for maintenance or private use so that customers cannot book unavailable dates.

### Acceptance Criteria

- Administrators can select an accommodation unit.
- Administrators can select dates to block.
- Administrators can provide a reason for the blocked dates.
- Blocked dates cannot be booked by customers.
- Administrators can remove blocked dates.

### Tasks

- [ ] Create blocked dates model.
- [ ] Create blocked date form.
- [ ] Add date blocking functionality.
- [ ] Connect blocked dates to availability checking.
- [ ] Add remove functionality.
- [ ] Test blocked dates.


## US29: Manage Seasonal and Unit Pricing

Priority: Should
User Type: Administrator
Labels: administrator, priority-should

### User Story

As an administrator, I want to manage seasonal and unit pricing so that accommodation prices remain accurate throughout the year.

### Acceptance Criteria

- Administrators can set prices for accommodation units.
- Administrators can create seasonal pricing.
- Administrators can edit seasonal pricing.
- Administrators can remove seasonal pricing.
- Prices are applied correctly to bookings.

### Tasks

- [ ] Create pricing model.
- [ ] Create seasonal pricing model.
- [ ] Create pricing management form.
- [ ] Add create functionality.
- [ ] Add edit functionality.
- [ ] Add delete functionality.
- [ ] Connect pricing to booking calculations.


## US30: View Registered Customers

Priority: Could
User Type: Administrator
Labels: administrator, priority-could

### User Story

As an administrator, I want to view registered customers so that I can manage customer information.

### Acceptance Criteria

- Administrators can view registered customers.
- Customer names are displayed.
- Customer email addresses are displayed.
- Customer registration dates are displayed.
- Administrators can select a customer to view further information.

### Tasks

- [ ] Create customer management view.
- [ ] Create customer list template.
- [ ] Display customer information.
- [ ] Add customer detail view.
- [ ] Test customer management.


## US31: Filter Bookings

Priority: Could
User Type: Administrator
Labels: administrator, priority-could

### User Story

As an administrator, I want to filter bookings by date, accommodation and status so that I can quickly find specific bookings.

### Acceptance Criteria

- Administrators can filter bookings by date.
- Administrators can filter bookings by accommodation.
- Administrators can filter bookings by booking status.
- Multiple filters can be used together.
- The filtered results are displayed correctly.
- Administrators can clear the filters.

### Tasks

- [ ] Create booking filter form.
- [ ] Add date filtering.
- [ ] Add accommodation filtering.
- [ ] Add status filtering.
- [ ] Allow multiple filters.
- [ ] Add clear filters functionality.
- [ ] Test booking filters.