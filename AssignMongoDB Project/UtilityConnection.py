from DBUtility import MongoDBConnection
import datetime
collObj = MongoDBConnection('ProjectDB','todolist_coll','mongodb://localhost:27017/').create_connection() #use atlas url
print(collObj)


#CRUD OPERATOR 
def insert_todo(**kwargs):
    if collObj is not None:
        data = kwargs
        data['createdDate'] = datetime.datetime.now()
        try:
            response = collObj.insert_one(data)
            print(f'inserted {response.acknowledged} and {response.inserted_id}')
        except Exception as e:
            print(e)



def find_todo(id=None,title=None,cardcolor=None):
    if collObj is not None:
        try:
            if id is not None:
               resultSet = collObj.find({"id" : id})
               for data in resultSet:
                   print(data)
            elif title is not None:
               resultSet = collObj.find({"title" : title})
               for data in resultSet:
                   print(data)
            else:
               resultSet = collObj.find({},{"_id": 0})
               for data in resultSet:
                   print(data)
        except Exception as e:
            print(e)
    else:
        return None


def delete_todo(id):
    if collObj is not None:
        try:
            result=collObj.delete_one({"_id" : id,})
            print(result)
            print("Record deleted")
        except Exception as e:
            print("not deleted sucessfully",e)
    
        
def update_todo(id):
    if collObj is not None:
        try:
            res=collObj.delete_one({"_id" : id,},{'$set':{"title":input(),"cardcolor":input()}})
            print(res)
            print("Record updated")
        except Exception as e:
            print("not updated sucessfully",e)
    

    

def main():
    while True:
        print("*"*30)
        print('1.insert\n 2.find\n 3.find on id\n 4. find on title\n 5.update on id\n 6. delete on id\n 7.-1 : exit\n ')
        print("*"*30)
        choice = int(input('Enter the choice: '))
        if choice == 1:
            id = int(input("enter id: "))
            title = input("enter task name: ")
            cardColor = input("Enter task status : Red , Blue , Green: ")
            isCompleted = input('Is task Completed? true / false: ')
            isCompleted = True if isCompleted == 'true' else False
            insert_todo(id = id , title = title , cardColor = cardColor, isCompleted = isCompleted)
        
        elif choice ==2:
            find_todo()
        
        elif choice ==3:
            id=int(input('enter the id: '))    
            find_todo(id=id)
       
        elif choice ==4:
            title=input('enter title: ')
            find_todo(title=title)
       
        elif choice ==5:
           id=int(input('enter id to update: '))  
           update_todo(id=id)    
       
        elif choice ==6:
            id=int(input('enter id to delete: ')) 
            delete_todo(id=id)
       
        elif choice == -1:
            break

if __name__ == '__main__':
    main()