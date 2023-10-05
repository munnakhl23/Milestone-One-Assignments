post_data = [
    {
        "userId": "Alex Gates",
        "id": 1,
        "title": "sunt aut facere repellat provident",
        "body": "quia et suscipit \n suscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId": "Alex Gates",
        "id": 2,
        "title": "qui est esse ",
        "body": "est rerum tempore vitae \n sequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId": "Alex Gates",
        "id": 3,
        "title": "ea molestias quasi exercitationem ",
        "body": "et iusto sed quo iure \n voluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId": "Alex Gates",
        "id": 4,
        "title": "eum et est occaecati ",
        "body": "ullam et saepe reiciendis voluptatem adipisci \n sit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId": "Alex Gates",
        "id": 5,
        "title": " nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed \n alias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    }
        ]


x = 0
while x < len(post_data):
    post_title = post_data[x]['title']
    post_data[x]['slug'] = post_title.replace(' ', '-')
    print(post_data[x])
    x += 1

statements = "i have tried many time to do this task through FOR Loop, but i couldn't"
suggestion = "So, please help me to sort it out for both task"
print(f" \n NOTE -  {statements.capitalize()}.{suggestion} ")

mentor = "MD. ABDUL AOUWAL"
pos = "THE HONOURABLE MENTOR OF THIS BATCH"
print("\n THANKS TO ",mentor.title(),"\n ", pos.lower() )


