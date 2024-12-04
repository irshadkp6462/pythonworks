order=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]

order_summary={}

for item in order:

    if item in order_summary:

        order_summary[item]+=1

    else:

        order_summary[item]=1

print(order_summary)
