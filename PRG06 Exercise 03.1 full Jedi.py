# We went full Jedi on this one! The result can be found underneath!
def z(agevic,agemar,agefad,ageahm):
      a = [agevic,agemar,agefad,ageahm]
      return (sum(a)/(len(a)))
#the array exist out of all the -agevic, agemar, etc- variables
#the values will be obtained at a later stage (via the user). 
agevic=int(input("enter the age Victor :"))
agemar=int(input("enter the age Marieke :"))
agefad=int(input("enter the age Fadi :"))
ageahm=int(input("enter the age Ahmed :"))
#instead of receiving the values, we have chosen to receive the values via the PC user. The code will ask for input. 

Q = z(agevic,agemar,agefad,ageahm)
print ("The average of",agevic,"and", agemar, "and", agefad,"and",ageahm,"is ",Q)
