def update(lst):

    print(id(lst))
    lst[1]=15
    print(id(lst))
    print('lst',lst)
lst=[10,20,30]
print(id(lst))
print("old lst",lst)
update(lst)
print("new lst",lst)


