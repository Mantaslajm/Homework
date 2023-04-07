import random


def give_question(question_number,num1,num2):
    answer=input("Q%s: %s * %s =" %(question_number,num1,num2))
    try:
        answer=int(answer)
        return answer
    except:
        print("answer hast to be number")
        give_question(question_number,num1,num2)
        # return answer

def give_test(question_list):
    result_list=[]
    question_number=0
    for q in question_list:
        question_number+=1
        answer=give_question(question_number,q[0],q[1])
        result_list.append(answer)

    return result_list


def made_question():
    list=[]
    for x in range(10):
        r1=random.randint(0,100)
        r2=random.randint(0,100)
        q_list=[r1,r2]
        list.append(q_list)
    return list

def write_summery(question_list,answers):
    print("****Summary****")
    result=0

    for q in range(10):

        x,y=question_list[q][0],question_list[q][1]

        txt=f"Q{q+1}:{x}*{y},student answer: {answers[0]},correct answer{x*y}"
        if answers[q]==x*y:
            txt += " Correct"
            result+=1
        else:
            txt += " Incorrect"
        print(txt)
    print(f"test result:{result}/10")
    if result >=7:
        print("Tset passed")
    else:
        print("Test failed")





question_list=made_question()
print(question_list)
answers=give_test(question_list)
write_summery(question_list,answers)