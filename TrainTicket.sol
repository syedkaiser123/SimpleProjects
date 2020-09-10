pragma solidity 0.4.22 <= 0.6.12;

contract TT{
    
    string Name;
    string Tkt_No;
    int amount;
    string Date;
    string from_Station;
    string To_station;
    
    
    constructor(string NewName, string New_tkt_no, int NewAmount, string NewDate, string NewFromStation, string NewToStation) public {
        
        
        Name = NewName;
        Tkt_No = New_tkt_no;
        amount = NewAmount;
        Date = NewDate;
        from_Station = NewFromStation;
        To_station = NewToStation;
        
        
    }
    
    function getTicketDetails() public view returns(string,string,int,string,string,string) {
        
        return(Name,Tkt_No,amount,Date,from_Station,To_station);
        
    }
    
}