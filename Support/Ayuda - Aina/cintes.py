#Practica realitzada per Aina Ferra Marcus
'''
Analysis:
This method is a linear algorythm since it only looks up for every file once.
I've coded this way because we only have one file of a determinated size.
Thinking about the previous ordenation, we know that the complexity overall the programm
will be converted to (n*log(n)) at least.
We could optimize our code with divide and conquer technics, which ensure a O(logn) complexity most of the times.

If we only have one file of a determinated size and we don't care if there's still space free (even though we can't put more files in it), yes
the code should be optimus.
If we care about the free space wasted, then it isn't optimized, since we could look up for every other combination of sizes in order not to let free space.
This would mean looking over all the information before doing anything, so it wouldn't be a greedy algorythm.
'''
def cintes(K, M):
    #K is a natural number which means the capacity of the cinta.
    #M is a list of natural numbers which represent the size of the files.
    
    #First, we must sort the size of our files.
    M = sorted(M)
    #We will put the files here:
    files = []
    ocupedFiles = 0
    ocuped = 0
    i = 0
    
    for i in range(0, len(M)):
        if ocuped + M[i] <= K:
            files.append(M[i])
            ocupedFiles += 1
            ocuped += M[i]
                
    print "We've got", ocupedFiles, "files"
    print "Sizes", files
    
    
    
cintes(3, [1, 2, 3, 4])
        