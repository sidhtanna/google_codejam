Thousand = ["One Thousand","Two Thousand","Three Thousand","Four Thousand","Five Thousand","Six Thousand",
        "Seven Thousand","Eight Thousand","Nine Thousand","Ten Thousand"," Eleven Thousand"," Twelve Thousand"," Thirteen Thousand",
        " Fourteen Thousand"," Fifteen Thousand"," Sixteen Thousand"," Seventeen Thousand"," Eighteen Thousand"," Nineteen Thousand",
        "Twenty Thousand"]
Hundread = ["One Hundred"," Two Hundred"," Three Hundred"," Four Hundred"," Five Hundred"," Six Hundred"," Seven Hundred"," Eight Hundred"," Nine Hundred"]
Ten = ["Twenty"," Thirty"," Forty"," Fifty"," Sixty"," Seventy"," Eighty"," Ninety"]
One = ["One"," Two"," Three"," Four"," Five"," Six"," Seven"," Eight"," Nine","Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen"," Sixteen"," Seventeen"," Eighteen"," Nineteen"]

num=None
try:
    num = int(raw_input("Enter any number : "))
except Exception as e:
    print("\n\n     Error ---->  Please Enter valid numeric values...")
    exit(0)
word = ""
rem = 0

if num < 0:
    word+="Minus "
    num= abs(num)

if num > 999 and num <= 20999:
    rem = num / 1000
    word += Thousand[rem-1]+" "
    num = num%1000

if num > 100 and num <= 999:
    rem = num / 100
    word += Hundread[rem-1]+" "
    num = num%100

if num > 20 and num <= 99:
    rem = num / 10
    word +=Ten[rem-2]+" "
    num = num%10

if num > 0 and num <=19:
    word += One[num-1]

print("\n\n==========  "+word+"  =============\n\n")

