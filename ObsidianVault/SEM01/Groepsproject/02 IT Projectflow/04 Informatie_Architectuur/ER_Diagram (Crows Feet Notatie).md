```mermaid
erDiagram
    %% Entities
    House {
        int house_id PK
        string city
        string street
        int house_number
    }

    Utility {
        int utility_id PK
        int house_id FK
        int year
        int month
        float gas_bill_euro
        float gas_bill_m3
        float electricity_bill_euro
        float electricity_bill_kwh
    }

    Room {
        int room_id PK
        int house_id FK
        int room_number
        int room_area_m2
        float room_rent
    }

    Room_historie {
        int history_id PK
        int room_id FK
        date start_date
        date end_date
    }

    Student {
        int student_id PK
        string first_name
        string last_name
        string email
        string phone_number
        string iban_number
    }

    Complaint {
        int complaint_id PK
        int student_id FK
        int employee_id FK
        string description
        date date_submitted
        string status
        string prioritie
        string categorie
    }

    Employee {
        int employee_id PK
        int house_id FK
        string first_name
        string last_name
        string email
        int phone_number
        float wage
        string job_title
        date start_date
        string location
        int manager_id FK
    }

    External_partner {
        int partner_id PK
        string company_name
        string email
        int phone_number
        string contact_person
    }

    Maintance_task {
        int task_id PK
        int house_id FK
        string task
        string description
        date date
        string status
        int employee_id FK
        int partner_id FK
    }

    Cleaning_task {
        int cleaning_id PK
        int house_id FK
        string task
        string description
        date date
        string status
        int student_id FK
    }

    %% Relationships
    House ||--o{ Utility : "has"
    House ||--o{ Employee : "responsible_for"
    House ||--o{ Room : "contains"
    House ||--o{ Cleaning_task : "needs_cleaning"
    House ||--o{ Maintance_task : "requires_upkeep"

    Room ||--o{ Student : "is_rented_by"
    Room ||--o{ Room_historie : "has_history"

    Student ||--o{ Complaint : "has_complaint"
    Student ||--o{ Cleaning_task : "is_responsible_for_cleaning"

    Employee ||--o{ Employee : "managed_by"
    Employee ||--o{ Complaint : "handles"

    Maintance_task }o--|| Employee : "is_responsible_for"
    Maintance_task }o--|| External_partner : "is_responsible_for"
```

Taakverdeling
Waarvoor maak je deze tabel aan en verbind je niet Student aan de Taak? student - cleaning_Task

Heb alles in het engels gezet, handig om dit aan te als standaard voor je producten (Tip van Bert)

Omgezet naar Mermaid zodat het gitbaar is

Verder wat relaties tegevoegd, veel veranderd