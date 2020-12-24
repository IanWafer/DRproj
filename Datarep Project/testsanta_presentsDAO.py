from santaPresentsDAO import santaPresentsDAO

# Initial information to populate the table with
present1= {
    'id': 1,
    'name': 'Test 1',
    'fromAge': 5,
    'price': 20
}

present2 = {
    'id': 2,
    'name': 'Test 2',
    'fromAge': 7,
    'price': 10
}

present3 = {
    'id': 3,
    'name': 'Test 3',
    'fromAge': 12,
    'price': 35
}

present4 = {
    'id': 4,
    'name': 'Test 4',
    'fromAge': 10,
    'price': 15
}

present5 = {
    'id': 5,
    'name': 'Test 5',
    'fromAge': 8,
    'price': 20
}

#  Some test and print statements to check the code is working
print('Create')
returnvalue =  santaPresentsDAO.create(present1)
returnvalue =  santaPresentsDAO.create(present2)
returnvalue =  santaPresentsDAO.create(present3)
returnvalue =  santaPresentsDAO.create(present4)
returnvalue =  santaPresentsDAO.create(present5)
print('Get All')
returnvalue = santaPresentsDAO.getAll()
print(returnvalue)
print('Find by id')
returnvalue = santaPresentsDAO.findById(present1['id'])
print(returnvalue)
print('Update')
returnvalue = santaPresentsDAO.update(present1)
print(returnvalue)
print('Delete')
returnvalue = santaPresentsDAO.delete(present1['id'])
print(returnvalue)
