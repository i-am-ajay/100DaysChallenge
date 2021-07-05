Coffee Maker is program that will simulate the process of coffee making. But involves various sub processes.
1. A process that will make coffee. This will handle:
    * show types of coffee available
    * accept user order
    * make coffee and deliver coffee.

2. Money Manager, process that will
    * collect money,
    * check if submitted amount is enough
    * returns any due amount.


3. Logistic module
    * keep track of resources
    * update resources status

How all these modules are integrated?

1) Coffee maker will show types of coffee available. For this information it will rely on Logistic Module,
    It will get details about all the available options and will display it to user.
2) After taking user order it will further validate, if system has enough resources to make coffee, for this
    coffee maker module will get information from logistic module.
3) If system can make coffee then control will be transferred to Money Manager with details of the coffee that
    client ordered -
    * money manager will receive money.
    * Will check if amount is sufficient.
    * Will return extra amount
    * If amount is insufficient it will cancel the order otherwise it will send success status to coffee module.

 4) Once coffee maker gets approval for order processing it will start making coffee, and update resource status
    in Logistic modules.