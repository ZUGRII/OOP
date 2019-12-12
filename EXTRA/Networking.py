import urllib.request
import random
from os import system
import webbrowser


def getOS():
    print("Are you currently running Windows or Linux?\n")
    while True:
        os = input().lower()
        if os in ["w", "windows", "windows 10"]:
            system("cls")
            return "windows"
        if os in ["l", "linux", "ubuntu"]:
            system("clear")
            return "linux"
        print("\nTry again, just type the word windows or linux\n")


def clear():
    if os == "windows":
        system("cls")
    else:
        system("clear")


def generateQuestions():
    print("Please wait\n\n(if this takes longer than a minute, check your internet connection and try again)")
    url = "https://itexamanswers.net/ccna-2-v6-0-final-exam-answers-routing-switching-essentials.html"

    page = str(urllib.request.urlopen(url).read())[79533:186059]
    page = page[:67077] + " " + page[67079:]

    questions = []
    for i in range(1, 104):
        if i in [42, 51, 58, 78, 83, 85]:
            continue

        questionsource = page[page.find(">" + str(i) + ". ") + 1:page.find(">" + str(i + 1) + ". ")].replace(
            "<br />\\n", "\n")

        question = questionsource[questionsource.find(" ") + 1:questionsource.find("<")]

        if question[:5].lower() == "match" or "choose" in question.lower():
            continue

        answersource = questionsource[questionsource.find("<ul>") + 6:questionsource.find("</ul>") - 2]
        answers = []
        while len(answersource) > 5:
            if answersource[answersource.find(">") + 1] == "<":
                rightanswer = answersource[answersource.find("g>") + 2:answersource.find("</strong>")]
                if rightanswer[-1] == "*":
                    rightanswer = rightanswer[:-1]
                answers.append(rightanswer)
            else:
                answers.append(answersource[answersource.find(">") + 1:answersource.find("</li>")])
            answersource = answersource[answersource.find("</li>") + 5:]

        if questionsource.find("Explain:") != -1:
            explain = questionsource[questionsource.find("Explain:") + 18:]
            explain = explain[:explain.find("</p>")]
        else:
            explain = ""

        if questionsource.find("img class") != -1:
            imgurl = questionsource[questionsource.find("src=") + 5:questionsource.find(" alt=") - 1]
            questions.append(ImgQuestion(i, question, answers, rightanswer, explain, imgurl))
            continue

        questions.append(Question(i, question, answers, rightanswer, explain))
    clear()
    return questions


class Question(object):
    def __init__(self, number, question, answers, rightanswer, explain):
        self.number = number
        self.question = question
        self.answers = answers
        self.rightanswer = rightanswer
        self.explain = explain

    def __str__(self):
        return self.question

    def ask(self):
        correct = False
        print("{}\n\n".format(self.question))
        for i in range(0, len(self.answers)):
            print("{}) {}\n".format(i + 1, self.answers[i]))
        try:
            answer = int(input()) - 1
            if self.answers[answer] == self.rightanswer:
                print("\nCorrect!\n")
                correct = True
            else:
                print("\nIncorrect\n")
        except:
            print("Invalid input\n")
        print("Correct answer:\n{}{}".format(self.rightanswer,
                                             "\n\nExplanation:\n" + self.explain if self.explain else ""))
        input("\n\nPress enter to continue")
        clear()
        return int(correct)


class ImgQuestion(Question):
    def __init__(self, number, question, answers, rightanswer, explain, imgurl):
        Question.__init__(self, number, question, answers, rightanswer, explain)
        self.imgurl = imgurl

    def ask(self):
        webbrowser.open(self.imgurl, new=2, autoraise=True)
        return Question.ask(self)


def main():
    questions = generateQuestions()
    score = 0
    for x in questions:
        score += x.ask()

    print("You scored {} out of {}".format(score, len(questions)))


os = getOS()
main()