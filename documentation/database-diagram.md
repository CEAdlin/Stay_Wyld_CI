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

- A customer profile belongs to one Django user; a user may have no profile.
    The one-to-one Django field makes `user_id` unique.
- `Unit.slug` is unique in Django even though the Mermaid field is shown as a
    normal attribute for parser compatibility.
- A customer can create many bookings.
- A unit can have many bookings, gallery images and blocked dates.
- A booking can have multiple modification or cancellation requests.
- The unit/date uniqueness constraint prevents duplicate blocked dates for the
  same unit.
