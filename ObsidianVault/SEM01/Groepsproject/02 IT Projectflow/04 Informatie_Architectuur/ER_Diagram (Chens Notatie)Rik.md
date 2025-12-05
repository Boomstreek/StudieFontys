```plantuml
@startchen
' ===========================
' METADATA
' ===========================
' Version: 1.0
' Date: 05-12-2025
' Depends on: 
' Author: Bram Wieringa
' Based on work from: Rik
' Notes: 
' ===========================

<style>
.red {
BackGroundColor #f08080
FontColor #000000
}
.blue {
BackGroundColor #00bfff
FontColor #000000
}
.green {
BackGroundColor #90ee90
FontColor #000000
}
.black {
BackGroundColor #000000
FontColor #FFFFFF
}
.grey {
BackGroundColor #A9A9A9
FontColor #000000
}
</style>

' Entities
' ===========================
' METADATA
' ===========================
entity Metadata <<black>> {
	Title_Conceptual_ERD_Chens <<grey>> {
	}
	Version_1_0 <<grey>> {
	}
	Date_05_12_2025 <<grey>> {
	}
	Author_Rik_Hoevenaars <<grey>> {
	}
}
' ===========================

entity Student <<red>> {
	naam <<blue>> {
	}
	email <<blue>> {
	}
	gas_bill_euro <<blue>> {
	}
	gas_bill_m3 <<blue>> {
	}
	electricity_bill_euro <<blue>> {
	}
	electricity_bill_kwh <<blue>> {
	}
}

entity House <<red>> {
	city <<blue>> {
	}
	street <<blue>> {
	}
	house_number <<blue>> {
	}
}

entity Room <<red>> {
	room_number <<blue>> {
	}
	room_area_m2 <<blue>> {
	}
	room_rent <<blue>> {
	}
}

entity Room_historie <<red>> {
	start_date <<blue>> {
	}
	end_date <<blue>> {
	}
}

entity Student <<red>> {
	first_name <<blue>> {
	}
	last_name <<blue>> {
	}
	email <<blue>> {
	}
	phone_number <<blue>> {
	}
	iban_number <<blue>> {
	}
}

entity Complaint <<red>> {
	description <<blue>> {
	}
	date_submitted <<blue>> {
	}
	status <<blue>> {
	}
	prioritie <<blue>> {
	}
	categorie <<blue>> {
	}
}

entity Employee <<red>> {
	first_name <<blue>> {
	}
	last_name <<blue>> {
	}
	email <<blue>> {
	}
	phone_number <<blue>> {
	}
	wage <<blue>> {
	}
	job_title <<blue>> {
	}
	start_date <<blue>> {
	}
	location <<blue>> {
	}
	manager <<blue>> {
	}
}

entity External_partner <<red>> {
	company_name <<blue>> {
	}
	email <<blue>> {
	}
	phone_number <<blue>> {
	}
	contact_person <<blue>> {
	}
}

entity Maintance <<red>> {
	task <<blue>> {
	}
	description <<blue>> {
	}
	date <<blue>> {
	}
	status <<blue>> {
	}
}

entity Cleaning <<red>> {
	task <<blue>> {
	}
	description <<blue>> {
	}
	date <<blue>> {
	}
	status <<blue>> {
	}
}

' Relationships

relationship has <<green>> {
}
relationship contains <<green>> {
}
relationship is_rented_by <<green>> {
}
relationship responsible_for <<green>> {
}
relationship managed_by <<green>> {
}
relationship has_history <<green>> {
}
relationship has_complaint <<green>> {
}
relationship handles <<green>> {
}
relationship requires_upkeep <<green>> {
}
relationship is_responsible_for <<green>> {
}
relationship needs_cleaning <<green>> {
}
relationship is_responsible_for_cleaning <<green>> {
}

' connection
House -1- has
has -N- Utility

Employee -1- responsible_for
responsible_for -N- House

House -1- contains
contains -N- Room

House -1- needs_cleaning
needs_cleaning -N- Cleaning

House -1- requires_upkeep
requires_upkeep -N- Maintance

Room -N- is_rented_by
is_rented_by -1- Student

Student -1- has_complaint
has_complaint -N- Complaint

Employee -1- handles
handles -N- Complaint

Employee -N- managed_by
managed_by -1- Employee

Maintance -N- is_responsible_for
is_responsible_for -1- Employee
is_responsible_for -1- External_partner

Student -1- is_responsible_for_cleaning
is_responsible_for_cleaning -N- Cleaning

Room -1- has_history
has_history -N- Room_historie
@endchen
```