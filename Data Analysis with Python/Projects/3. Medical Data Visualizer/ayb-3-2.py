def calc(data):
    total=sum(data)

    if total>100 or total<0:
        print(total, "Invalid Marks")
        return (total, "Invalid Marks")

    elif total>=80 and total<101:
        print(total, "A")
        return (total, "A")

    elif total>=65 and total<80:
        print(total, "B")
        return (total, "B")

    elif total>=50 and total<65:
        print(total, "D")
        return (total, "D")
    elif total<50:
        print(total, "F")
        return (total, "F")


calc(  [10, 40, 35, 15] )