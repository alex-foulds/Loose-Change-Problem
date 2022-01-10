#Loose change problem

def main():

    coins = [2,1,0.5,0.2,0.1,0.05,0.02,0.01];
    denomination = ["£2","£1","50p","20p","10p","5p","2p","1p"];
    finalDict = {};
    change = 0.98;

    if calculateChange(coins,denomination,finalDict,change):
        print(finalDict);



def calculateChange(coins,denomination,finalDict,change):
    try:
        for i in range(len(coins)):

            #Finding how many of each coin denomination are in the current change value
            temp = change // coins[i];
            if temp > 0:
                #Populates dictionary
                finalDict[denomination[i]] = int(temp);
                change = round(change - (temp * coins[i]),2);
            if change == 0:
                #If change has been 'given'
                return True;
            if change <= 0:
                print("'change' is a negative value");
                return False;
    except TypeError as err:
        print("Error in 'change' input. Not type int/float");
main();