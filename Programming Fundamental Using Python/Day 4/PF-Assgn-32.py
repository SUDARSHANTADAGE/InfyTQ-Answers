'''
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
}

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Also write the pytest test cases to test the program.

Note:
  1. Assume that there is always only one medical speciality which is visited by maximum number of patients.
` 2. Perform case sensitive string comparison wherever necessary.
'''


#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    l=[]
    for i in range(0,len(patient_medical_speciality_list),2):
        l.append(patient_medical_speciality_list[i])
    i1=patient_medical_speciality_list.index(max(l))
    for  k,v in medical_speciality.items():
        if k==patient_medical_speciality_list[i1+1]:
            speciality=v
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[101,"O",102,"E",302,"P",305,"P",401,"E",656,"O",987,"E"]
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
