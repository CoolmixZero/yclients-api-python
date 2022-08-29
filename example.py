from yclients import YClientsAPI

if __name__ == '__main__':
  
    # Create API object
    TOKEN = "your token"
    СID = 'your company id'
    FID = 'form id'
    
    api = YClientsAPI(token=TOKEN, company_id=СID, form_id=FID, debug=True)
    
    # Show debugging process
    api.show_debugging()
    
    
    """ BOOKING """
        
    # Get staff info
    all_staff = api.get_staff()
    print(all_staff)

    staff_id = all_staff['data'].get('id')
    
    # Get services info
    services = api.get_services(staff_id=staff_id)
    print(services)

    service_id = services['data']['services'].get('id')
    
    # Get booking dates
    booking_days = api.get_available_days(staff_id=staff_id, service_id=service_id)
    print(booking_days)

    day = booking_days['data'].get('booking_dates')  # or .get('booking_days')
    
    # Get booking times
    time_slots = api.get_available_times(staff_id=staff_id, service_id=service_id, day=day)
    print(time_slots)

    date_time = time_slots['data'].get('time')  # or .get('datetime')
    
    # Book
    booked, message = api.book(booking_id=0, 
                           fullname='my name', 
                           phone='53425345', 
                           email='myemail@email.com', 
                           service_id=service_id, 
                           date_time=date_time, 
                           staff_id=staff_id, 
                           comment='some comment')
   
  
    """ USER """
        
    # Get USER TOKEN from the system.
    login = "example@gmail.com"
    password = "password"
    
    user_token = api.get_user_token(login, password)
    # Update autorisation parameters of the API class with USER TOKEN
    api.update_user_token(user_token)
    
    # Shows USER permissions
    api.show_user_permissions()
    
    
    """ CLIENT """
    
    # Get clients list
    clients_data_list = api.get_clients_data()
    
    # Parse clients data
    df = api.parse_clients_data(clients_data_list)
    
    # Show id, name and number of visits for all clients
    print(df[['id', 'name', 'visits']])
    
    # Clients IDs list
    all_clients_ids = list(df['id'])
    
    
    """ VISITS """
    
    # Show all visits for client with Client_ID
    cid = 20419758
    client_visits = api.get_visits_for_client(cid)
    print(f'Client {cid} visits')
    print(f'{pd.DataFrame(client_visits)}')
    
    # Show all visits for all clients
    all_clients_visits = api.get_visits_data_for_clients_list(all_clients_ids)
    for cid in all_clients_visits.keys():
      print(f'Client {cid} visits')
      print(f'{pd.DataFrame(all_clients_visits[cid])}')
    
    # Show all attended visits for client with Client_ID
    cid = 20419758
    client_visits = api.get_attended_visits_for_client(cid)
    print(f'Client {cid} attended visits')
    print(f'{pd.DataFrame(client_visits)}')
    
    # Show attended visits information for clients:
    df = api.get_attended_visits_dates_information(all_clients_ids)
    print(f'Attended visits dataframe: {df}')
    
    # Show attended visits information for clients with at least one visit:
    print(f"Attended visits ndataframe with no gaps {df[df['visits_number']>0]}")
