'''
Since we are doing a simple loop, passing through every element just once, this is a lineal 
algorythm O(n).


---------Is it optimum?
Yes, it gives an  optimum solution.

If we go the further we can go, by definition, it will never be a situation where going less far
would give an advantatge to go to a station we can't reach going furhter. This proves that if the problem
has solution, with this algorythm finds it for sure. On the other hand, it does minimize the number of stations,
since going to the further leaves behind some stations we don't need to go; and there's no station left behind that
could led us to a station further that the one we can already reach.

'''

def gasolineres(D, lstDistances):
    jump = 0
    stations = []
    
    #We are looking, for every possible station, the further we can go
    #without passing over the limit D.
    for i in range(1, len(lstDistances)):
        #We are taking i as our furhter station.
        #If the station we are checking is unreachable
        #And the previous station is reachable
        #That means that the previous station is the further we can go. 
        if lstDistances[i] - lstDistances[jump] > D and lstDistances[i-1]-lstDistances[jump] <= D:
            jump = i-1
            stations.append(lstDistances[jump])
    
    #Our previous iteration doesn't compare the last station.
    #So we do this here.

    if lstDistances[len(lstDistances)-1]-lstDistances[jump] <= D:
        print "Route completed!"
        #If we can go to the last one, then we must add it. 
        stations.append(lstDistances[len(lstDistances)-1])
        print "We go through the stations located at the kms", stations
        print "Those are", len(stations), "of the", len(lstDistances), "we had"
        
    #If there was any problems, then notify it. 
    else:
        print "We cannot complete the route"
            
    
    

gasolineres(100, [0, 40, 100, 170, 190, 250, 260, 300])