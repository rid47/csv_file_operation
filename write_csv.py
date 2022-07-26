import csv

# # using writerow
# with open("test_write.csv", mode="w") as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(['ridwan', 'se', 'nov'])
#     writer.writerow(['mizan','se', 'july'])


# using DictWriter

with open('test_write2.csv', mode='w') as f:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name':'ridwan', 'dept': 'se', 'birth_month': 'july'})
    writer.writerow({'emp_name':'ridwan', 'dept': 'se', 'birth_month': 'july'})