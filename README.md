![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# YCLIENTS API ![https://img.shields.io/badge/Python-3.7.5-blue](https://img.shields.io/badge/Python-3.7+-blue) 

### **Python [YCLIENTS API WRAPPER](https://github.com/CoolmixZero/yclients-api-python/blob/main/yclients.py "Opens yclients.py") with [ujson](https://pypi.org/project/ujson/ "Opens ujson documentation") and [httpx](https://www.python-httpx.org/ "Opens httpx documentation") packages:**

- This is an **updated version** of this project: https://github.com/Stayermax/Python-Yclients-API

- The code changed `httpx ⟵ requests` and `ujson ⟵ json` packages.
> `ujson` and `httpx` **faster** than `json` and `requests`

- An example of using library also implemented in the [example.py](https://github.com/CoolmixZero/yclients-api-python/blob/main/example.py "Opens example.py") file to copy.

> Please note that sending requests to get customer data can take time, especially if your database is quite large, since Yclients API can return only 200 results at once. Also if sending one request takes more than a few seconds, you may need to connect to another Internet network.

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
```python
    all_staff = api.get_staff()
    print(all_staff)

    staff_id = all_staff['data'].get('id')
```

____

<details>
<summary>Output ...</summary>
    
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
```python
    services = api.get_services(staff_id=staff_id)
    print(services)

    service_id = services['data']['services'].get('id')
```

____

<details>
<summary>Output ...</summary>
    
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
```python
    booking_days = api.get_available_days(staff_id=staff_id, service_id=service_id)
    print(booking_days)

    day = booking_days['data'].get('booking_dates')  # or .get('booking_days')
```
- ### Get booking times
```python
    time_slots = api.get_available_times(staff_id=staff_id, service_id=service_id, day=day)
    print(time_slots)

    date_time = time_slots['data'].get('time')  # or .get('datetime')
```
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
## User commands:
- ### Get USER TOKEN from the system
> You can save this TOKEN (like BEARER TOKEN) and there is no need to update it every time
```python
    login = "example@gmail.com"
    password = "password"
    
    user_token = api.get_user_token(login, password)
```
- ### Update autorisation parameters of the API class with USER TOKEN
```python
    api.update_user_token(user_token)
```
- ### Shows USER permissions
```python
    api.show_user_permissions()
```
## Client commands:
- ### Get clients list
```python
    clients_data_list = api.get_clients_data()
```
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
```python
    cid = 20419758
    client_visits = api.get_visits_for_client(cid)
    print(f'Client {cid} visits')
    print(f'{pd.DataFrame(client_visits)}')
```
- ### Show all visits for all clients
```python
    all_clients_visits = api.get_visits_data_for_clients_list(all_clients_ids)
    for cid in all_clients_visits.keys():
        print(f'Client {cid} visits')
        print(f'{pd.DataFrame(all_clients_visits[cid])}')
```
- ### Show all attended visits for client with Client_ID
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
