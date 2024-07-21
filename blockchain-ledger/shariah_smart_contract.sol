pragma solidity ^0.8.0;

contract ShariahCompliantTransactionLedger {
    mapping (address => bool) public transactions;

    function addTransaction(address _address, bool _compliance) public {
        transactions[_address] = _compliance;
    }

    function getTransaction(address _address) public view returns (bool) {
        return transactions[_address];
    }
}
