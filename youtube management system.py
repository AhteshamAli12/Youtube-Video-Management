import sqlite3

con = sqlite3.connect("Videos.db")
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

def list_video():
    cur.execute("SELECT * FROM videos")
    data = cur.fetchall()
    for row in data:
        # print(row)
        print("{0} Name: {1} and Time: {2}".format(row[0], row[1], row[2]))

def add_video():
    name = input("Enter name: ")
    time = input("Enter time: ")
    cur.execute('''INSERT INTO videos (name, time) VALUES (?,?)''',(name, time))
    con.commit()

def delete_video():
    video_id = input("Enter Video ID: ")
    cur.execute('''DELETE FROM videos WHERE id = ?''', (video_id,))
    con.commit()

def update_video():
    video_id = input("Enter ID: ")
    new_name = input("Enter new name: ")
    new_time = input("Enter new time: ")
    cur.Update("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name,new_time,video_id))
    con,commit()

def main():
    while True:
        print("~~~~~~ youtube Management System ~~~~~~")
        print('''Choose an option:
        1. List video
        2. Add Video
        3. Delete Video
        4. Update Video
        5. Exist''')
        op = int(input("Enter Here: "))
        match op:
            case 1:
                list_video()
            case 2:
                add_video()
            case 3:
                delete_video()
            case 4:
                update_video
            case 5:
                break
            case _:
                print("Envalid Option!")
    con.close()
if __name__ == "__main__":
    main()