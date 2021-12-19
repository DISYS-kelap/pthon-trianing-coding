class childhood_friend():

            friends=[{"school":[{"name":"kiran"},{"type":"good friend"},{"duration":"very long"},
                                {"name":"jp"},{"type":"best friend"},{"duration":"very long"},
                                {"name":"vasanth"},{"type":"good friend"},{"duration":"very long"},
                                {"name":"surya"},{"type":"good friend"},{"duration":"few years"}]}]




            college_friends=[{"college":[{"name":"anbu"},{"type":"best friend"},{"duration":"few years"},
                             {"name":"rijo"},{"type":"good friend"},{"duration":"very long"},
                             {"name":"anbu"},{"type":"best friend"},{"duration":"few years"}]}]



          
          


for i in friends:
    if (i["school"][0]["name"]=="kiran"):
        print("good friend")
        
   
    else:
        print("he is not a friend")

for j in college_friends:
    if (j["college"][0]["name"]=="anbu"):
        print("college friend")
    else:
        print("bad friend")
                        
