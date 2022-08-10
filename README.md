# YCLIENTS API on PYTHON
Python Yclients API wrapper with ujson and httpx packages.

<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Python</title><path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z"/></svg>

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
