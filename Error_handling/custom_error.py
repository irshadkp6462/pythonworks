def review(rating):

    if rating < 0:

        raise Exception("too low")
    
    elif rating>10:

        raise Exception("too high")
    else:

        print("done")

try:

    review(11)

except Exception as e:

    print(e)

    review(rating=int(input("enter a num between 1 - 10 ")))

finally:

    print("hii")

    print("heloo")

