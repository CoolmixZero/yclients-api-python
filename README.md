# YCLIENTS API on PYTHON
Python Yclients API wrapper with ujson and httpx packages.

#3776AB

This is an updated version of this project: https://github.com/Stayermax/Python-Yclients-API

The code added 'httpx' to send requests into YCLIENTS API and 'ujson' package (because ujson and httpx faster than json and requests)

Please note that sending requests to get customer data can take time, especially if your database is quite large, since Yclients API can return only 200 results at once. Also if sending one request takes more than a few seconds, you may need to connect to another Internet network.

# Example:

    from yclients import YClientsAPI
    import pandas as pd


    TOKEN = "your_token"
    СID = 'your_company_id'
    FID = 'form id'

    api = YClientsAPI(token='your-token', company_id='company id', form_id='form id', debug=True)
                        
    login = "example@gmail.com"
    password = "password"

## Create api object
    api = YClientsAPI(token=TOKEN, company_id=СID, form_id=FID)

## Show debugging process
    api.show_debugging()

## Booking commands
### Get staff info
    all_staff = api.get_staff()
    print(all_staff)

    staff_id = all_staff['data'].get('id')

### Get services info
    services = api.get_services(staff_id=staff_id)
    print(services)

    service_id = services['data']['services'].get('id')

### Get booking dates
    booking_days = api.get_available_days(staff_id=staff_id, service_id=service_id):
    print(booking_days)

    day = booking_days['data'].get('booking_dates')  # or .get('booking_days')

### Get booking times
    time_slots = api.get_available_times(staff_id=staff_id, service_id=service_id, day=day)
    print(time_slots)

    date_time = time_slots['data'].get('time')  # or .get('datetime')

### Book
    booked, message = api.book(booking_id=0, 
                               fullname='my name', 
                               phone='53425345', 
                               email='myemail@email.com, 
                               service_id=service_id, 
                               date_time=date_time, 
                               staff_id=staff_id, 
                               comment='some comment')

## Get user token from the system
## You can save this token (like bearer token)
##   and there is no need to update it every time
    user_token = api.get_user_token(login, password)

## Update autorisation parameters of the api class with user token
    api.update_user_token(user_token)

## Shows user permissions
    api.show_user_permissions()

## Get clients list
    clients_data_list = api.get_clients_data()

## Parse clients data
    df = api.parse_clients_data(clients_data_list)
## Show id, name and number of visits for all clients
    print(df[['id', 'name', 'visits']])

## Clients ids list
    all_clients_ids = list(df['id'])

## Show all visits for client with cid
    cid = 20419758
    client_visits = api.get_visits_for_client(cid)
    print(f'Client {cid} visits')
    print(f'{pd.DataFrame(client_visits)}')

## Show all visits for all clients
    all_clients_visits = api.get_visits_data_for_clients_list(all_clients_ids)
    for cid in all_clients_visits.keys():
        print(f'Client {cid} visits')
        print(f'{pd.DataFrame(all_clients_visits[cid])}')

## Show all attended visits for client with cid
    cid = 20419758
    client_visits = api.get_attended_visits_for_client(cid)
    print(f'Client {cid} attended visits')
    print(f'{pd.DataFrame(client_visits)}')

## show attended visits information for clients:
    df = api.get_attended_visits_dates_information(all_clients_ids)
    print(f'Attended visits dataframe: {df}')

## show attended visits information for clients with at least one visit:
    print(f"Attended visits ndataframe with no gaps {df[df['visits_number']>0]}")
