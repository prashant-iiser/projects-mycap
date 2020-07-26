import csv
def write_into_csv(info_list):
    with open("student_info.csv",'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['NAME','AGE','PLACE','CONTACT NO.','EMAIL'])

        writer.writerow(info_list)

#basic administration school tool
if __name__=='__main__':
    condition=True


while(condition):
    student_info = input("enter some student information as\nName age place contact no. email address\n ")
    print(student_info)
    
    #split
    student_info_list= student_info.split(' ')
    #print("entered split up information is "+ str(student_info_list))
    print("\nthe entered information is: \n name: {}\n age:{}\n place:{}\n contact:{}\n email address:{}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
    choice_check=input("entered information is correct? (yes/no)")
    if choice_check=="yes":
        write_into_csv(student_info_list)
        condition_check=input("enter (yes/no) if you want to continue: ")
        if condition_check=="yes":
            condition=True
        elif condition_check=="no":
            condition=False
            break
    elif choice_check=="no":
        print("\nplease re-enter the information. ")
        pass
