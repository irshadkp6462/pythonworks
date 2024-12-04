text="ABCBADSDDNSBA"

ch_frequency={ch:text.count(ch) for ch in text}

print(ch_frequency)

non_recursive=[k for k,v in ch_frequency.items() if v==1]

print(non_recursive)