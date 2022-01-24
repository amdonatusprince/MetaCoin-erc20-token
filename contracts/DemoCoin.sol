pragma solidity >=0.4.25 <0.7.0;

import "./ConvertLib.sol";

contract DemoCoin {
	mapping (address => uint) balances;

	event Transfer(address indexed _from, address indexed _to, uint256 _value);

	constructor() public {
		balances[tx.origin] = 10000;
	}

	function sendCoin(address receiver, uint amount) public returns(bool sufficient) {
		if (balances[msg.sender] < amount) return false;
		balances[msg.sender] -= amount;
		balances[receiver] += amount;
		emit Transfer(msg.sender, receiver, amount);
		return true;
	}

    	function getBalance(address _address) public view returns(uint) {
		return balances[_address];
	}

	function getBalanceInEth(address _address) public view returns(uint){
		return ConvertLib.convert(getBalance(_address),2);
	}
}