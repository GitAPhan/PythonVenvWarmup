import dbcreds as c
import mariadb as db

# connect to database function
def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=c.user,
                          password=c.password,
                          host=c.host,
                          port=c.port,
                          database=c.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("something went wrong with the DB, please try again in 5 minutes")
    except Exception as e:
        print(e)
        print("Something went wrong!")
    return conn, cursor  

# disconnect from database function
def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except Exception as e:
        print(e)
        print('cursor close error: what happened?')

    try:
        conn.close()
    except Exception as e:
        print(e)
        print('connection close error')

# login attempt
def attempt_login(username, password):
    user = None
    conn, cursor = connect_db()

    try:
        # grabs the password from database to be compared to user input
        cursor.execute(
            "select id from owner where username =? and password=?", [username, password])
        user = cursor.fetchone()

    except db.OperationalError:
        print("something went wrong with the DB, please try again in 5 minutes")
        t.print_exc()
    except db.ProgrammingError:
        print("Error running DB Query, please file bug report")
        t.print_exc()
    except:
        print("Something went wrong!")
        t.print_exc()

    disconnect_db(conn, cursor)

    if(user == None):
        return False, None
    else:
        return True, user[0]

# show dogs
def show_user_dogs(user_id):
    dogs = []
    conn, cursor = connect_db()

    try:
        # grabs the password from database to be compared to user input
        cursor.execute(
            "select name, description from dog where owner_id=?", [user_id,])
        dogs = cursor.fetchall()

    except db.OperationalError:
        print("something went wrong with the DB, please try again in 5 minutes")
        t.print_exc()
    except db.ProgrammingError:
        print("Error running DB Query, please file bug report")
        t.print_exc()
    except:
        print("Something went wrong!")
        t.print_exc()

    disconnect_db(conn, cursor)
    print('----------------------------')

    for dog in dogs:
        print('name: ', dog[0])
        print('description: ', dog[1])
        print('----------------------------')