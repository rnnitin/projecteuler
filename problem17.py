import requests
import time

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

urlFrmt="https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?number={num}&format=words&letter_case=lowercase&action=solve"

letterCount = 0
for num in range(1,1001):
    reqStr = urlFrmt.format(num = num)
    # print (reqStr)
    numHtml = requests.get(reqStr).text
    # print (numHtml);
    startInd = numHtml.find("<div id=\"answer\" class=\"still\"><br>") + len("<div id=\"answer\" class=\"still\"><br>")
    endInd = numHtml.find("</div>", startInd);
    numStr = numHtml[startInd:endInd]
    lenStr = len(numStr.replace(" ", ""))
    letterCount = letterCount + lenStr
    print (str(num) + " = " + numStr + " => " + str(lenStr) + " => " + str(letterCount))
    # break
    # time.sleep(1.75)
print ("letterCount = " + str(letterCount))
