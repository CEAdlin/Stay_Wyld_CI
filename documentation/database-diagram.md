# Stay Wyld Database Diagram

This Mermaid ERD reflects the current Django models and relationships. Django's
built-in `User` model is shown alongside the project models.

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

 Each registered customer has one `CustomerProfile` linked to exactly one
 Django `User`, enforced by the one-to-one relationship. Staff and superuser
 accounts use Django's built-in `User` account for administration and are
 intentionally exempt from the customer-specific profile.
 `CustomerProfile.user_id` is therefore unique. `Unit.slug` is also unique in
 Django, although those uniqueness markers are omitted from the Mermaid field
 syntax for parser compatibility.
 An authenticated customer can have many bookings. An administrator-created
 booking may have no linked user because the customer's name, email and phone
 are stored directly on the booking.
 A unit can have many bookings, gallery images and blocked dates.
 A booking can have multiple modification or cancellation requests, each
 submitted by a customer user.
 The unique unit/date constraint prevents the same date being blocked more than
 once for a particular unit.

## Workflow Notes

- A customer booking is initially stored with a `PENDING` status. Staff can
    review it and change the status to `CONFIRMED`, `CANCELLED` or `COMPLETED`.
- Customer modification and cancellation requests are stored separately in
    `BookingChangeRequest`. Staff approval is represented by the request status
    changing from `OPEN` to `APPROVED` or the internal `REJECTED` value, which is
    displayed to users as **Declined**.
- A booking is not considered available only because it is pending. The booking
    availability logic checks date overlap and ignores cancelled bookings.
- Staff can create `UnitBlockedDate` records for maintenance or private use.
    Blocked nights are displayed as unavailable and rejected by the booking
    validation logic.
- A following booking can check in on the previous booking's checkout date,
    because the checkout date is treated as the exclusive end of the stay.
