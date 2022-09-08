![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Last Commit](https://img.shields.io/github/last-commit/CoolmixZero/yclients-api-python?style=for-the-badge)
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

# YCLIENTS API [![PyPI version](https://img.shields.io/pypi/v/yclients-api.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/yclients-api)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/yclients-api.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/yclients-api) [![Tests Passing](https://github.com/CoolmixZero/yclients-api-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/CoolmixZero/yclients-api-python/actions)

### **Python [YCLIENTS API WRAPPER](https://github.com/CoolmixZero/yclients-api-python/blob/main/yclients/yclients.py "Opens yclients.py") with [ujson](https://pypi.org/project/ujson/ "Opens ujson documentation") and [httpx](https://www.python-httpx.org/ "Opens httpx documentation") packages:**
- PyPI page of project: https://pypi.org/project/yclients-api/
- This is an **updated version** of this project: https://github.com/Stayermax/Python-Yclients-API

- The code changed `httpx ⟵ requests` and `ujson ⟵ json` packages.
  > `ujson` and `httpx` **faster** than `json` and `requests`

- An example of using library also implemented in the [example.py](https://github.com/CoolmixZero/yclients-api-python/blob/main/example.py "Opens example.py").

> Please note that sending requests to get customer data can take time, especially if your database is quite large, since YCLIENTS API can return only 200 results at once. Also if sending one request takes more than a few seconds, you may need to connect to another Internet network.
> 
# Installation:
```shell
pip install yclients-api
```
____
# Usage:
## Create API object
```python
from yclients import YClientsAPI


TOKEN = "your token"
СID = 'your company id'
FID = 'form id'

api = YClientsAPI(token=TOKEN, company_id=СID, form_id=FID, debug=True)
```
## Show debugging process
```python
api.show_debugging()
```
## Booking commands:
- ### Get staff info
  > Returns list of staff for specific service and date
```python
all_staff = api.get_staff()
print(all_staff)

staff_id = all_staff['data'].get('id')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": [
    {
      "id": "16",
      "name": "Вася",
      "bookable": true,
      "specialization": "Фельдшер",
      "position": {
        "id": 1,
        "title": "Администратор"
      },
      "show_rating": "1",
      "rating": "3",
      "votes_count": "1",
      "avatar": "https://yclients.com/images/no-master.png",
      "comments_count": "0",
      "weight": "11",
      "information": "<span></span>",
      "seance_date": 1443139200,
      "seances": []
    },
    {
      "id": "32",
      "name": "Петя",
      "bookable": false,
      "specialization": "Терапевт",
      "position": [],
      "show_rating": "1",
      "rating": "4",
      "votes_count": "1",
      "avatar": "https://yclients.com/images/no-master.png",
      "comments_count": "0",
      "weight": "8",
      "information": "<span></span>"
    }
  ],
  "meta": []
}
```
    
</details>

____

- ### Get services info
  > Returns list of services for specific staff and date
```python
services = api.get_services(staff_id=staff_id)
print(services)

service_id = services['data']['services'].get('id')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": {
    "events": [],
    "services": [
      {
        "id": 1896208,
        "title": "Мытье волос",
        "category_id": 1895571,
        "price_min": 0,
        "price_max": 0,
        "discount": 0,
        "comment": "",
        "weight": 0,
        "active": 0,
        "sex": 0,
        "image": "",
        "prepaid": "forbidden",
        "seance_length": 3600
      },
      {
        "id": 1896303,
        "title": "Окрашивание",
        "category_id": 1895574,
        "price_min": 0,
        "price_max": 0,
        "discount": 0,
        "comment": "",
        "weight": 0,
        "active": 0,
        "sex": 0,
        "image": "",
        "prepaid": "forbidden",
        "seance_length": 3600
      }
    ],
    "category": [
      {
        "id": 1895571,
        "title": "Уходы для волос",
        "sex": 0,
        "api_id": 0,
        "weight": 60
      },
      {
        "id": 1895574,
        "title": "Окрашивание волос",
        "sex": 0,
        "api_id": 0,
        "weight": 7
      }
    ]
  },
  "meta": []
}
```
    
</details>

____

- ### Get booking dates
  > Returns all available days for specific staff and service
```python
booking_days = api.get_available_days(staff_id=staff_id, service_id=service_id)
print(booking_days)

day = booking_days['data'].get('booking_dates')  # or .get('booking_days')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": {
    "booking_days": {
      "9": [
        "4",
        "5",
        "8",
        "9",
        "12",
        "13",
        "16",
        "17",
        "20",
        "21",
        "24",
        "25",
        "28",
        "29",
        "30"
      ],
      "10": [
        "1",
        "4",
        "5",
        "8",
        "9",
        "12",
        "13",
        "16",
        "17",
        "20",
        "21",
        "24",
        "25"
      ]
    },
    "booking_dates": [
      1441324800,
      1441411200,
      1441670400,
      1441756800,
      1442016000,
      1442102400,
      1442361600,
      1442448000,
      1442707200,
      1442793600,
      1443052800,
      1443139200,
      1443398400,
      1443484800,
      1443571200,
      1443657600,
      1443916800,
      1444003200,
      1444262400,
      1444348800,
      1444608000,
      1444694400,
      1444953600,
      1445040000,
      1445299200,
      1445385600,
      1445644800,
      1445731200
    ],
    "working_days": {
      "9": [
        "4",
        "5",
        "8",
        "9",
        "12",
        "13",
        "16",
        "17",
        "20",
        "21",
        "24",
        "25",
        "28",
        "29",
        "30"
      ],
      "10": [
        "1",
        "4",
        "5",
        "8",
        "9",
        "12",
        "13",
        "16",
        "17",
        "20",
        "21",
        "24",
        "25"
      ]
    },
    "working_dates": [
      1441324800,
      1441411200,
      1441670400,
      1441756800,
      1442016000,
      1442102400,
      1442361600,
      1442448000,
      1442707200,
      1442793600,
      1443052800,
      1443139200,
      1443398400,
      1443484800,
      1443571200,
      1443657600,
      1443916800,
      1444003200,
      1444262400,
      1444348800,
      1444608000,
      1444694400,
      1444953600,
      1445040000,
      1445299200,
      1445385600,
      1445644800,
      1445731200
    ]
  },
  "meta": []
}
```
    
</details>

____

- ### Get booking times
  > Returns all available times slots on specific day staff and service
```python
time_slots = api.get_available_times(staff_id=staff_id, service_id=service_id, day=day)
print(time_slots)

date_time = time_slots['data'].get('time')  # or .get('datetime')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": [
    {
      "time": "12:00",
      "seance_length": 3600,
      "datetime": 1443513600
    },
    {
      "time": "13:00",
      "seance_length": 3600,
      "datetime": 1443517200
    },
    {
      "time": "14:00",
      "seance_length": 3600,
      "datetime": 1443520800
    },
    {
      "time": "15:00",
      "seance_length": 3600,
      "datetime": 1443524400
    },
    {
      "time": "16:00",
      "seance_length": 3600,
      "datetime": 1443528000
    }
  ],
  "meta": []
}
```
    
</details>

____

- ### Book
```python
booked, message = api.book(booking_id=0, 
                           fullname='my name', 
                           phone='53425345', 
                           email='myemail@email.com, 
                           service_id=service_id, 
                           date_time=date_time, 
                           staff_id=staff_id, 
                           comment='some comment')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "record_id": 2820023,
      "record_hash": "567df655304da9b98487769426d4e76e"
    },
    {
      "id": 2,
      "record_id": 2820024,
      "record_hash": "34a45ddabdd446d5d33bdd27fbf855b2"
    }
  ],
  "meta": []
}
```
    
</details>

<details>
<summary>Payload(JSON) example ...</summary>
    
```json
{
  "phone": "79000000000",
  "fullname": "ДИМА",
  "email": "d@yclients.com",
  "code": "38829",
  "comment": "тестовая запись!",
  "type": "mobile",
  "notify_by_sms": 6,
  "notify_by_email": 24,
  "api_id": "777",
  "appointments": [
    {
      "id": 1,
      "services": [
        331
      ],
      "staff_id": 6544,
      "datetime": 1443517200,
      "custom_fields": {
        "my_custom_field": 123,
        "some_another_field": [
          "first value",
          "next value"
        ]
      }
    },
    {
      "id": 2,
      "services": [
        99055
      ],
      "staff_id": 6544,
      "datetime": 1443614400,
      "custom_fields": {
        "my_custom_field": 456,
        "some_another_field": [
          "next value",
          "last value"
        ]
      }
    }
  ]
}
```
    
</details>

____

## User commands:
- ### Get USER TOKEN from the system
  > You can save this TOKEN (like BEARER TOKEN) and there is no need to update it every time
```python
login = "example@gmail.com"
password = "password"

user_token = api.get_user_token(login, password)
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "id": 123456,
  "user_token": "wec23fh8cDfFV4432fc352456",
  "name": "Иван Попов",
  "phone": "79161001010",
  "login": "79161001010",
  "email": "test@test.com",
  "avatar": "https://assets.yclients.com/general/0/01/123456789098765_12345678909876.png"
}
```
    
</details>

____

- ### Update autorisation parameters of the API class with USER TOKEN
  > After USER TOKEN was obtained you need to include it in header of requests that you are sending
```python
api.update_user_token(user_token)
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": {
    "user_token": "4de9d8cc108c0"
  },
  "meta": []
}
```
    
</details>

____

- ### Shows USER permissions
```python
api.show_user_permissions()
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": {
    "timetable": {
      "timetable_access": true,
      "master_id": 1000238,
      "position_id": 0,
      "last_days_count": 1000,
      "schedule_edit_access": true,
      "timetable_phones_access": true,
      "timetable_transferring_record_access": true,
      "timetable_statistics_access": true
    },
    "record_form": {
      "record_form_access": true,
      "record_form_client_access": true,
      "records_autocomplete_access": true,
      "create_records_access": true,
      "edit_records_access": true,
      "edit_records_attendance_access": true,
      "records_services_cost_access": true,
      "records_services_discount_access": true,
      "record_edit_full_paid_access": true,
      "delete_records_access": true,
      "delete_customer_came_records_access": true,
      "delete_paid_records_access": true,
      "records_goods_access": true,
      "records_goods_create_transaction_access": true,
      "records_goods_create_last_days_count": -1,
      "records_goods_edit_transaction_access": true,
      "records_goods_edit_last_days_count": -1,
      "records_goods_cost_access": true,
      "records_goods_discount_access": true,
      "records_finances_access": true,
      "records_finances_last_days_count": -1,
      "records_finances_pay_from_deposits_access": true,
      "records_group_id_access": true,
      "records_group_id": 134178
    },
    "finances": {
      "finances_access": true,
      "finances_accounts_ids": [],
      "finances_transactions_access": true,
      "finances_last_days_count": -1,
      "finances_create_transactions_access": true,
      "finances_create_last_days_count": -1,
      "finances_edit_transactions_access": true,
      "finances_edit_last_days_count": -1,
      "finances_delete_transactions_access": true,
      "finances_transactions_excel_access": true,
      "finances_expenses_ids": [],
      "finances_accounts_access": true,
      "finances_accounts_banalce_access": true,
      "finances_suppliers_read_access": true,
      "finances_suppliers_create_access": true,
      "finances_suppliers_update_access": true,
      "finances_suppliers_delete_access": true,
      "finances_suppliers_excel_access": true,
      "finances_expenses_read_access": true,
      "expenses_read_access": true,
      "finances_expenses_create_access": true,
      "expenses_create_access": true,
      "finances_expenses_update_access": true,
      "expenses_update_access": true,
      "finances_expenses_delete_access": true,
      "expenses_delete_access": true,
      "finances_kkm_transactions_access": true,
      "kkm_transactions_accounts_access": true,
      "finances_kkm_settings_read_access": true,
      "kkm_settings_reed_access": true,
      "finances_kkm_settings_update_access": true,
      "kkm_settings_update_access": true,
      "finances_settings_invoicing_read_access": true,
      "settings_invoicing_read_access": true,
      "finances_settings_invoicing_update_access": true,
      "settings_invoicing_update_access": true,
      "finances_options_read_access": true,
      "options_read_access": true,
      "finances_options_update_access": true,
      "options_update_access": true,
      "finances_salary_schemes_access": true,
      "finances_salary_calc_access": true,
      "finances_salary_not_limitation_today_access": true,
      "finances_payroll_calculation_create_access": true,
      "finances_payroll_calculation_create_not_limitation_today_access": true,
      "finances_salary_access_master_checkbox": true,
      "finances_salary_access_master_id": 1000237,
      "get_salary_access_master_id": 1000237,
      "finances_salary_master_not_limitation_today_access": true,
      "finances_payroll_calculation_create_by_master_access": true,
      "calculation_create_by_master_not_limitation_today_access": true,
      "finances_period_report_access": true,
      "finances_period_report_excel_access": true,
      "finances_year_report_access": true,
      "finances_year_report_excel_access": true,
      "finances_print_check_access": true,
      "finances_z_report_access": true,
      "finances_z_report_no_limit_today_access": true,
      "finances_z_report_excel_access": true
    },
    "clients": {
      "clients_access": true,
      "client_phones_access": true,
      "clients_phones_email_access": true,
      "clients_card_phone_access": true,
      "clients_delete_access": true,
      "clients_excel_access": true,
      "excel_access": true,
      "client_comments_list_access": true,
      "client_comments_add_access": true,
      "client_comments_own_edit_access": true,
      "client_comments_other_edit_access": true,
      "client_files_list_access": true,
      "client_files_upload_access": true,
      "client_files_delete_access": true,
      "clients_visit_master_id": 0,
      "get_visit_master_id": 0
    },
    "dashboard": {
      "dashboard_access": true,
      "dash_access": true,
      "dash_phones_access": true,
      "dash_records_access": true,
      "dash_records_last_days_count": -1,
      "dash_records_excel_access": true,
      "dash_records_phones_access": true,
      "dash_message_access": true,
      "dash_message_excel_access": true,
      "dash_message_phones_access": true,
      "dash_reviews_access": true,
      "dash_reviews_delete_access": true,
      "dashboard_calls_access": true,
      "dashboard_calls_excel_access": true,
      "dashboard_calls_phones_access": true
    },
    "notification": {
      "notification": true,
      "web_push": true,
      "web_phone_push": true,
      "notification_sms_ending_license": true,
      "notification_sms_low_balance": true,
      "notification_email_ending_license": true
    },
    "loyalty": {
      "loyalty_access": true,
      "has_loyalty_access": true,
      "loyalty_cards_manual_transactions_access": true,
      "has_loyalty_cards_manual_transactions_access": true,
      "loyalty_certificate_and_abonement_manual_transactions_access": true
    },
    "storages": {
      "storages_access": true,
      "storages_ids": [],
      "storages_transactions_access": true,
      "storages_last_days_count": -1,
      "storages_move_goods_access": true,
      "storages_create_transactions_access": true,
      "storages_create_last_days_count": -1,
      "storages_create_transactions_buy_access": true,
      "storages_create_transactions_sale_access": true,
      "storages_edit_transactions_access": true,
      "storages_edit_last_days_count": -1,
      "storages_edit_transactions_buy_access": true,
      "storages_edit_transactions_sale_access": true,
      "storages_delete_transactions_access": true,
      "storages_transactions_excel_access": true,
      "storages_transactions_types": [],
      "storages_inventory_access": true,
      "storages_inventory_create_edit_access": true,
      "storages_inventory_delete_access": true,
      "storages_inventory_excel_access": true,
      "storages_remnants_report_access": true,
      "storages_remnants_report_excel_access": true,
      "storages_sales_report_access": true,
      "storages_sales_report_excel_access": true,
      "storages_consumable_report_access": true,
      "storages_consumable_report_excel_access": true,
      "storages_write_off_report_access": true,
      "storages_write_off_report_excel_access": true,
      "storages_turnover_report_access": true,
      "storages_turnover_report_excel_access": true,
      "storages_goods_crud_access": true,
      "storages_goods_create_access": true,
      "storages_goods_update_access": true,
      "storages_goods_title_edit_access": true,
      "storages_goods_category_edit_access": true,
      "storages_goods_selling_price_edit_access": true,
      "storages_goods_cost_price_edit_access": true,
      "storages_goods_units_edit_access": true,
      "storages_goods_critical_balance_edit_access": true,
      "storages_goods_masses_edit_access": true,
      "storages_goods_comment_edit_access": true,
      "storages_goods_archive_access": true,
      "storages_goods_delete_access": true
    },
    "settings": {
      "settings_access": true,
      "settings_basis_access": true,
      "settings_information_access": true,
      "users_access": true,
      "delete_users_access": true,
      "create_users_access": true,
      "edit_users_access": true,
      "limited_users_access": false,
      "settings_services_access": true,
      "settings_services_create_access": true,
      "services_edit": true,
      "settings_services_edit_title_access": true,
      "settings_services_relation_category_access": true,
      "settings_services_edit_price_access": true,
      "settings_services_edit_image_access": true,
      "settings_services_edit_online_seance_date_time_access": true,
      "settings_services_edit_online_pay_access": true,
      "settings_services_edit_services_related_resource_access": true,
      "settings_positions_read": true,
      "settings_positions_create": true,
      "settings_positions_delete": true,
      "edit_master_service_and_duration": true,
      "tech_card_edit": true,
      "services_delete": true,
      "settings_master_access": true,
      "master_create": true,
      "master_edit": true,
      "master_delete": true,
      "settings_master_dismiss_access": true,
      "schedule_edit": true,
      "settings_notifications_access": true,
      "settings_email_notifications_access": true,
      "settings_template_notifications_access": true,
      "webhook_read_access": true
    },
    "other": {
      "stat_access": true,
      "billing_access": true,
      "send_sms": true,
      "auth_enable_check_ip": false,
      "auth_list_allowed_ip": []
    }
  },
  "meta": []
}
```
    
</details>

____

## Client commands:
- ### Get clients list
  > YCLIENTS API can't return all clients at once and returns in groups of **maximum size of 200**. Those groups are called pages and you can choose how many clients it will return
```python
clients_data_list = api.get_clients_data()
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": [
    {
      "name": "Петров",
      "id": 2
    },
    {
      "name": "Сидоров",
      "id": 3
    },
    {
      "name": "Иванов",
      "id": 1
    }
  ],
  "meta": {
    "total_count": 908
  }
}
```
    
</details>

____

- ### Parse clients data
```python
df = api.parse_clients_data(clients_data_list)
```  
- ### Show ID, name and number of visits for all clients
```python
print(df[['id', 'name', 'visits']])
```
- ### Clients IDs list
```python
all_clients_ids = list(df['id'])
```
## Visits commands:
- ### Show all visits for client with Client_ID
  > YCLIENTS API can't return all visits at once and returns in groups of **maximum size of 200**. Those groups are called pages and you can choose how many visits it will return
```python
cid = 20419758
client_visits = api.get_visits_for_client(cid)
print(f'Client {cid} visits')
print(f'{pd.DataFrame(client_visits)}')
```

____

<details>
<summary>Response ...</summary>
    
```json
{
  "success": true,
  "data": [
    {
      "id": 2,
      "company_id": 4564,
      "staff_id": 9,
      "services": [
        {
          "id": 1,
          "title": "Наращивание волос",
          "cost": 100,
          "manual_cost": 100,
          "cost_per_unit": 100,
          "discount": 0,
          "first_cost": 100,
          "amount": 1
        }
      ],
      "goods_transactions": [],
      "staff": {
        "id": 9,
        "name": "Оксана",
        "specialization": "наращивание волос",
        "position": {
          "id": 1,
          "title": "Администратор"
        },
        "avatar": "http://yclients.com/images/no-master-sm.png",
        "avatar_big": "http://yclients.com/images/no-master.png",
        "rating": 0,
        "votes_count": 0
      },
      "date": 1547654400,
      "datetime": 1547622000,
      "create_date": "2019-01-16T20:35:11+0900",
      "comment": "не записывать",
      "online": false,
      "visit_attendance": 0,
      "attendance": 0,
      "confirmed": 1,
      "seance_length": 3600,
      "length": 3600,
      "sms_before": 0,
      "sms_now": 0,
      "sms_now_text": "",
      "email_now": 0,
      "notified": 0,
      "master_request": 0,
      "api_id": "",
      "from_url": "",
      "review_requested": 0,
      "visit_id": "8262996",
      "created_user_id": 1073232,
      "deleted": false,
      "paid_full": 0,
      "prepaid": false,
      "prepaid_confirmed": false,
      "last_change_date": "2019-01-16T20:35:15+0900",
      "custom_color": "",
      "custom_font_color": "",
      "record_labels": [],
      "activity_id": 0,
      "custom_fields": [],
      "documents": [
        {
          "id": 8172893,
          "type_id": 7,
          "storage_id": 0,
          "user_id": 746310,
          "company_id": 4564,
          "number": 4163,
          "comment": "",
          "date_created": 1530615600,
          "category_id": 0,
          "visit_id": 3,
          "record_id": 2,
          "type_title": "Визит"
        }
      ],
      "sms_remain_hours": 5,
      "email_remain_hours": 1,
      "bookform_id": 0,
      "record_from": "",
      "is_mobile": 0,
      "is_sale_bill_printed": false,
      "consumables": [],
      "finance_transactions": []
    },
    {
      "id": 9,
      "company_id": 4564,
      "staff_id": 49,
      "services": [],
      "goods_transactions": [],
      "staff": {
        "id": 49,
        "name": "Сергей",
        "specialization": "стилист",
        "position": {
          "id": 1,
          "title": "Администратор"
        },
        "avatar": "http://yclients.com/images/no-master-sm.png",
        "avatar_big": "http://yclients.com/images/no-master.png",
        "rating": 0,
        "votes_count": 0
      },
      "date": 1547654400,
      "datetime": 1547622000,
      "create_date": "2019-01-16T20:35:11+0900",
      "comment": "",
      "online": true,
      "visit_attendance": 1,
      "attendance": 1,
      "confirmed": 1,
      "seance_length": 10800,
      "length": 10800,
      "sms_before": 0,
      "sms_now": 0,
      "sms_now_text": "",
      "email_now": 0,
      "notified": 0,
      "master_request": 1,
      "api_id": "",
      "from_url": "",
      "review_requested": 0,
      "visit_id": "8262996",
      "created_user_id": 1073232,
      "deleted": false,
      "paid_full": 0,
      "prepaid": false,
      "prepaid_confirmed": false,
      "last_change_date": "2017-01-09T20:45:30+0900",
      "custom_color": "f44336",
      "custom_font_color": "#ffffff",
      "record_labels": [
        {
          "id": "67345",
          "title": "Сотрудник не важен",
          "color": "#009800",
          "icon": "unlock",
          "font_color": "#ffffff"
        },
        {
          "id": "104474",
          "title": "важная категория",
          "color": "#3b2c54",
          "icon": "odnoklassniki",
          "font_color": "#ffffff"
        }
      ],
      "activity_id": 0,
      "custom_fields": [],
      "documents": [
        {
          "id": 8172893,
          "type_id": 7,
          "storage_id": 0,
          "user_id": 746310,
          "company_id": 4564,
          "number": 4163,
          "comment": "",
          "date_created": 1530615600,
          "category_id": 0,
          "visit_id": 3,
          "record_id": 2,
          "type_title": "Визит"
        }
      ],
      "sms_remain_hours": 5,
      "email_remain_hours": 1,
      "bookform_id": 0,
      "record_from": "",
      "is_mobile": 0,
      "is_sale_bill_printed": false,
      "consumables": [],
      "finance_transactions": []
    }
  ],
  "meta": {
    "page": 1,
    "total_count": 10
  }
}
```
    
</details>

____

- ### Show all visits for all clients
```python
all_clients_visits = api.get_visits_data_for_clients_list(all_clients_ids)
for cid in all_clients_visits.keys():
    print(f'Client {cid} visits')
    print(f'{pd.DataFrame(all_clients_visits[cid])}')
```
- ### Show all attended visits for client with Client_ID
  > Attendance explanation from Yclient API:
  >> 2 - The user has confirmed the entry,
  >>> 1 - The user has arrived, the services are provided,
  >>>> 0 - the user is waiting,
  >>>>> -1 - the user did not come for a visit
```python
cid = 20419758
client_visits = api.get_attended_visits_for_client(cid)
print(f'Client {cid} attended visits')
print(f'{pd.DataFrame(client_visits)}')
```
- ### Show attended visits information for clients:
```python
df = api.get_attended_visits_dates_information(all_clients_ids)
print(f'Attended visits dataframe: {df}')
```
- ### Show attended visits information for clients with at least one visit:
```python
print(f"Attended visits ndataframe with no gaps {df[df['visits_number']>0]}")
```
