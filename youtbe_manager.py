import json

def save_data_helper(videos):
    with open ("youtube.txt", 'w') as file:
        json.dump(videos, file)


def load_data():
    try:
        with open ('youtube.txt', 'r') as file: 
            return json.load(file) 
    except FileNotFoundError:
        return []
    

def list_all_videos(videos):
    print("\n")
    print("*" * 100)
    # to list videos you have to use enumerate becasue you want unique index 
    for i, video in enumerate(videos, start = 1): 
        print(f"{i}. Title: {video["title"]}         Duraion: {video["time"]} minutes ") 
        ## becz ye ek dictionary hai vo thats why video["title"] ---> thi means video mein key title search karo 
    print("*" * 100)

# video append section
def add_video(videos):
    title = input("Enter video name: ")
    time = input("Enter video length in minutes: ")
    videos.append({'title' : title, 'time': time})
    save_data_helper(videos)
    print("Video added sucessfully!!!")
    print("*" * 100)
    print("\n")

# update section
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to get deleted: "))
    if  1<= index <= len(videos):
        newTitle = input("Enter new video title: ")
        newTime = input("Enter new video duration: ")
        videos[index-1] = {"title": newTitle , "time": newTime}
        save_data_helper(videos)
        print("Video updated sucessfully!!!")
        print("*" * 100)
        print("\n")

    else:
        print("Invalid index selected")

# delete function
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to get deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted sucessfully!!!")
        print("*" * 100)
        print("\n")

    else:
        print("Invalid Index passed!!!")

# exit function
def exit():
    pass    


def main():
    videos = load_data()
    while True:
        print("\n Youtube manager ")
        print("1. List all Youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit App ")
        choice = input("Enter a choice: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Enter valid choice!!!")
            


if __name__ == "__main__":
    main()