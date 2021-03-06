#Loose change problem

def main():

    coins = [2,1,0.5,0.2,0.1,0.05,0.02,0.01];
    denomination = ["£2","£1","50p","20p","10p","5p","2p","1p"];
    finalDict = {};
    change = 4.98;

    calculateChangeIterate(coins,denomination,finalDict,change);

    calculateChangeDivision(change);



def calculateChangeIterate(coins,denomination,finalDict,change):
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
                print(finalDict);
                return True;
            if change <= 0:
                print("'change' is a negative value");
                return False;
    except TypeError as err:
        print("Error in 'change' input. Not type int/float");


def calculateChangeDivision(change):
    #More hardcoded in the approach, but should be more time efficient
    #Doesnt print out a 'custom' sized dictionary
    finalDict={"£2": 0, "£1": 0, "50p":0, "20p":0, "10p":0, "5p":0, "2p":0, "1p":0};
    
    if change>0:
        #Approach uses the remaining values after floored division to work out the next coin values
        #Round has had to be used to avoid errors when 0.009999 would not add 1 to '1p'
        finalDict["£2"] = int(change//2);
        finalDict["£1"] = int(round(change % 2,2) // 1);
        finalDict["50p"]= int(round(change % 2 % 1,2) // 0.5);
        finalDict["20p"]= int(round(change % 2 % 1 % 0.5,2) // 0.2);
        finalDict["10p"]= int(round(change % 2 % 1 % 0.5 % 0.2,2) // 0.1);
        finalDict["5p"] = int(round(change % 2 % 1 % 0.5 % 0.2 % 0.1,2) // 0.05);
        finalDict["2p"] = int(round(change % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05,2) // 0.02);
        #Python maths results in strange error where 2p and 1p are both 2 for 0.99
        finalDict["1p"] = int(round(round(change % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05,2) % 0.02,2) //0.01);
        print(finalDict);
    else:
        print(finalDict);
main();