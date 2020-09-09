pragma solidity 0.4.22 <= 0.6.12;

contract Ebill{
    
    string Name;
    string Due_date;
    int units;
    int money;
    string addrs;
    string CustId;
    
    constructor(string newName, string new_Ddate, int newUnits, int newMoney, string newAddrs, string newCustId) public  {
    
        Name = newName;
        Due_date = new_Ddate;
        units = newUnits;
        money = newMoney;
        addrs = newAddrs;
        CustId = newCustId;
    
    
    }   
    
    function getEbill() public view returns(string,string,int,int,string,string) {
        
        return(Name,Due_date,units,money,addrs,CustId);
    
    }

}

