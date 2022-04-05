# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query) #will return a list of dictionaries
        # Create an empty list to append our instances of friends
        people = []
        # Iterate over the db results and create instances of friends with cls.
        for p in results: 
            #return one row of data
            people.append(cls(p)) #cls refers to the user class, user is from the single row in for loop
        return people