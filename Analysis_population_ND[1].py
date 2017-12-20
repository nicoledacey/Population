Us_Population_File = open("C:\\Users\\N. Dacey\\Documents\\USPopulation.txt", "r")
file_list = Us_Population_File.read().splitlines(True)
Us_Population_File.close

def average_annual_change(list_passed):
    total = 0
    number_list = []
    for i,x in zip(list_passed,list_passed[1:]):
        number_list.append(int(x)-int(i))
    for j in number_list:
        total += int(j)
    average = total/len(file_list)
    print("The average annual change in population:",int(average))

def greatest_increase(list_passed):
    number_list = []
    large_number = None
    truth = True
    for i,x in zip(list_passed,list_passed[1:]):
        number_list.append(int(x)-int(i))
    for l in number_list:
        if truth or l > large_number:
            large_number = l
            truth = False
    print("The biggest increase with is:",large_number)

def smallest_increase(list_passed):
    number_list = []
    small_number = None
    truth = True
    for i,x in zip(list_passed,list_passed[1:]):
        number_list.append(int(x)-int(i))
    for l,k in zip(number_list,number_list[1:]):
        if truth or l < small_number:
            small_number = l
            truth = False
        else:
            if k < small_number:
                small_number = k
                truth = False
    print("The smallest increase with is:",small_number)
average_annual_change(file_list)
large_number = greatest_increase(file_list)
smallest_increase(file_list)
