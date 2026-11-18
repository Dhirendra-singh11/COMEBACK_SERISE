#Enter subjects seperated by commas


raw_subjects=input("Enter a subjects seperated by commas")


list_sub=raw_subjects.split(",")
print(list_sub)




#--------------------OR------------------



list_sub2=[sub.strip() for sub in raw_subjects.split(",")]
print(list_sub2)