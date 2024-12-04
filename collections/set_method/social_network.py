user=["rahul","rohit","rishab","kohli","sanju","pandya","siraj"]

rahul_followers=["rahul","rohit","kohli","rishab"]

sanju_follower=["sanju","rohit","kohli"]

suggestion=set(user).difference(set(rahul_followers))

mutual=set(sanju_follower).intersection(set(rahul_followers))

print(mutual)

print(suggestion)

