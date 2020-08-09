def hotel_booking(arr, dept, room):
    event = [(t, 'RED') for t in arr] + [(t, "BLUE") for t in dept]
    event = sorted(event)
    
    guest = 0
    for e in event:
        if e[1] == 'RED':
            guest+=1
        else:
            guest-=1
        
        if guest > room:
            return 'Sorry the rooms are full'
    return 'Rooms available'

arr = [1, 3, 5]
dept = [2, 6, 8]
k = 1

print(hotel_booking(arr, dept, k))