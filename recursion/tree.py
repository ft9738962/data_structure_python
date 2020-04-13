import turtle

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(30)
        tree(branch_len - 20) #递归调用，画右边小树
        t.left(60)
        tree(branch_len - 20) #递归调用，画左边小树
        t.right(30)
        t.backward(branch_len) #回到原点，方便递归原来层继续

if __name__ == "__main__":
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.pencolor('green')
    tree(80)
    t.hideturtle()
    turtle.done()