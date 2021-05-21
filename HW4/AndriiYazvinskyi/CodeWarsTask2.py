def reverse(st):
    st = st.split(" ")
    sep = " "
    st.reverse()
    st = sep.join(st)
    return st