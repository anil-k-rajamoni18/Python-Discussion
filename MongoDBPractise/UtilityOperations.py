
from DBUtility import MongoDBConnection
import datetime

collobj = MongoDBConnection('studentData','studentCollection','mongodb://localhost:27017/').create_connection()

print(collobj)

#CRUD Operation
def insert_todo(**kwargs):
    if collobj is not None:
        data=kwargs
        data['createDate'] = datetime.datetime.now()
        try:
            response=collobj.insert_one(data)
            print(f'inserted{response.acknowledged} and {response.inserted_id} ')
        except Exception as e:
            print(e)

def find_todo(id=None,title=None,cardColor =None):
    if collobj is not None:
        try:
            if id:
                resultset = collobj.find({"id":id})
                for data in resultset:
                    print(data)
            elif title:
                resultset = collobj.find({"title":title})
                for data in resultset:
                    print(data)
            else:
                resultset = collobj.find({},{"_id":0})
                for data in resultset:
                    print(data)
           
        except Exception as e:
            print(e)
    else:
        return None 
            

def delete_todo(id):
    if collobj is not None:
        try:
            result = collobj.delete_one({"id": id})
            if result.deleted_count > 0:
                print("Delete successful.")
            else:
                print("No document found with the specified todo_id.")
        except Exception as e:
            print(e)



def update_todo(todo_id):
    updated_data = {"title": input('enter updated title name: '), "cardColor": input('enter updated cardColor: ')} 
    if collobj is not None:
        try:
           result = collobj.update_one({"id":todo_id},{'$set': updated_data})
           if result.modified_count > 0:
                    print("Update successful.")
                    updated_document = collobj.find_one({"id": todo_id})
                    return updated_document
           else:
                    print("No document found with the specified todo_id.")
                    return None
        except Exception as e:
            print(e)
            return None
    else:
        return None



def main():
    while True:
        print("*"*30)
        print("""
                    1.Insertion 
                    2.Find
                    3.Find on id
                    4.Find on title
                    5.Update on id
                    6.Delete on id
                    -1.Exit   
            """)
        print("*"*30)
        choice =  int(input("Enter the choice: "))
        if choice == 1:
            id = int(input("Enter id: "))
            title = input("Enter Task Name: ")
            cardColor = input("Enter task status : Black, Blue, green: ")
            isCompleted = bool(input("Is Task completed? true/false: "))
            isCompleted = True if isCompleted == "true" else False
                
           
            insert_todo( id =id, title=title, cardColor = cardColor, isCompleted=isCompleted )
        
        elif choice == 2:
            find_todo()
        
        elif choice == 3:
            id = int(input("Enter id: "))
            find_todo(id =id)

        elif choice == 4:
            title= input("Enter Task Name: ")
            find_todo(title = title)
        
        elif choice == 5:
            id = int(input("Enter id: "))
            update_todo(todo_id = id )
            

        elif choice == 6:
            id = int(input("Enter id: "))
            delete_todo(id=id)

        elif choice == -1:
            break

if __name__ == '__main__':
    main()